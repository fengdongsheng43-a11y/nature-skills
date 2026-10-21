#!/usr/bin/env python3
# WR/ES&T all-indexed source corpus; NOT a publisher-original-articles census.
import collections, csv, datetime as dt, hashlib, json, os, re, sys, time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

SOURCES={"WR":"S52566953","EST":"S13479253"}
START=dt.date(2024,1,1)
END=dt.date.fromisoformat(os.getenv("CENSUS_END_DATE","2026-10-21"))
BASE=Path("skills/nature-journal-trends/data")
OUT=BASE/"latest"
FIELDS="id,doi,title,publication_date,type,primary_topic,primary_location,abstract_inverted_index,is_retracted"
TAXONOMY={
 "PFAS":r"\bpfas\b|\bpfos\b|\bpfoa\b|per[- ]?and polyfluoroalkyl|perfluoroalkyl|fluorotelomer",
 "Micro-nanoplastics":r"micro[- ]?plastics?|nano[- ]?plastics?|micro[- ]?nanoplastics?",
 "Antibiotics-AMR":r"antibiotic|pharmaceutical|antimicrobial resistan|antibiotic resistan|resistance gene|\bARGs?\b",
 "Biological nitrogen":r"nitrif|denitrif|anammox|nitrogen removal|nitrogen cycling|nitrous oxide|\bn2o\b|ammonia oxid|nitrite oxid",
 "Phosphorus & eutrophication":r"phosphor|phosphate|struvite|nutrient recover|eutrophi|harmful algal bloom",
 "Advanced oxidation":r"peroxymonosulfate|persulfate|advanced oxidation|photocataly|photo[- ]?fenton|electrocataly|electrooxid|fenton",
 "Adsorption-materials":r"adsorp|sorbent|metal[- ]organic framework|\bMOF\b|single[- ]atom catalyst|biochar|hydrochar|activated carbon",
 "Membranes & desalination":r"membrane|nanofiltration|ultrafiltration|reverse osmosis|desalination|membrane distill",
 "Disinfection & DBPs":r"disinfection|disinfectant|chloramin|chlorinat|disinfection by[- ]products?|\bDBPs?\b",
 "Toxicity & exposure":r"toxicolog|toxicity|human exposure|bioaccumul|ecotox|risk assessment",
 "Atmosphere & aerosols":r"atmospher|aerosol|particulate matter|\bpm2[.]?5\b|air quality|air pollution",
 "Soils, aquifers, remediation":r"groundwater|soil pollut|soil contamin|subsurface|aquifer|bioremediat|soil remediat",
 "GHG & climate":r"greenhouse gas|carbon dioxide|\bCO2\b|methane|\bCH4\b|climate change|carbon footprint|carbon emission",
 "Microbiome & omics":r"microbiom|metagenom|metatranscriptom|microbial communit|microbial ecolog|metaproteom|microbial network",
 "AI & modelling":r"machine learning|deep learning|artificial intelligence|large language model|neural network|random forest|\bXGBoost\b|digital twin",
 "Resource recovery":r"resource recover|nutrient recover|recover(?:y|ing) of phosphorus|struvite|circular economy|upcycl|valorization",
}
RX={k:re.compile(v,re.I) for k,v in TAXONOMY.items()}
REVIEW_RX=re.compile(r"\b(review|meta.analysis|bibliometric|scoping review|systematic review|perspective)\b",re.I)
EXCLUDE_RX=re.compile(r"^(editorial|correction|corrigendum|erratum|retraction|comment(?:ary)?|reply to|letter to|publisher.s note)\b",re.I)

def request(q):
    key=os.getenv("OPENALEX_API_KEY","")
    if key:q["api_key"]=key
    url="https://api.openalex.org/works?"+urlencode(q)
    for i in range(7):
        try:
            with urlopen(Request(url,headers={"Accept":"application/json","User-Agent":"Journal-Trend-Census/2.0"}),timeout=55) as r:
                return json.load(r)
        except (URLError,HTTPError,TimeoutError,ValueError) as e:
            if isinstance(e,HTTPError) and e.code in (400,401,403,404):
                raise RuntimeError("OpenAlex HTTP "+str(e.code)+" on "+url.split("&api_key=")[0]) from e
            if i==6:raise RuntimeError("OpenAlex retrieval failed: "+str(e)) from e
            time.sleep(min(2**i,35))
    raise RuntimeError("unreachable")

def abstract(index):
    if not isinstance(index,dict):return ""
    parts=[]
    for word,pos in index.items():
        parts.extend((int(i),word) for i in pos)
    return " ".join(word for i,word in sorted(parts))

def doi(x):
    return re.sub(r"^https?://(?:dx\.)?doi\.org/","",str(x or "").lower().strip())

def article_class(r):
    typ=(r.get("type") or "").lower()
    name=r.get("title") or ""
    if r.get("is_retracted"):return "retracted"
    if typ!="article":return typ or "unknown"
    if EXCLUDE_RX.search(name):return "suspect_nonoriginal"
    if REVIEW_RX.search(name):return "suspect_review"
    return "article_proxy"

def cut(y):
    last=dt.date(y,12,31)
    return min(last,END) if y==END.year else last

def ym_day(d):
    return d.month,d.day

def writecsv(file,header,rows):
    with open(file,"w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=header,extrasaction="ignore");w.writeheader();w.writerows(rows)

def main():
    if END<START or END.year>2030:raise RuntimeError("Invalid date")
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"COMPLETE.json").unlink(missing_ok=True)
    rows=[];audits=[];raw_bytes=hashlib.sha256();unique=set()
    for journal,source in SOURCES.items():
        for year in range(START.year,END.year+1):
            first=dt.date(year,1,1);last=cut(year)
            filt=f"primary_location.source.id:{source},from_publication_date:{first},to_publication_date:{last}"
            n=None;results=[];page=1
            while True:
                o=request({"filter":filt,"page":page,"per_page":100,"select":FIELDS})
                if n is None:
                    n=(o.get("meta") or {}).get("count")
                    if not isinstance(n,int) or n<200 or n>10000:raise RuntimeError(f"{journal}/{year}: suspicious API count={n}")
                part=o.get("results",[])
                if not isinstance(part,list) or not part:raise RuntimeError(f"{journal}/{year} missing page={page}")
                results+=part
                print(f"{journal} {year}: {len(results)}/{n}",flush=True)
                if len(results)>=n:break
                page+=1
                time.sleep(.17)
            if len(results)!=n:raise RuntimeError(f"Count mismatch {journal}/{year}: {len(results)} != {n}")
            observed=set()
            for x in results:
                p=x.get("primary_location") or {}
                sid=str((p.get("source") or {}).get("id") or "").rsplit("/",1)[-1]
                if sid!=source:raise RuntimeError(f"Foreign journal source {journal}/{year}")
                key=doi(x.get("doi")) or x.get("id")
                if key in observed:raise RuntimeError(f"Duplicate within journal-year: {key}")
                observed.add(key)
                if (journal,key) in unique:raise RuntimeError(f"Repeated paper across years: {key}")
                unique.add((journal,key))
                date=x.get("publication_date")
                if not date or not (str(first)<=date<=str(last)):raise RuntimeError(f"Invalid publication_date {date}")
                a=abstract(x.get("abstract_inverted_index"))
                t=x.get("title") or ""
                text=t+" "+a
                theme=[k for k,rx in RX.items() if rx.search(text)]
                tp=x.get("primary_topic") or {}
                rows.append({"journal":journal,"year":year,"date":date,"doi":key if doi(x.get("doi")) else "",
                  "openalex_id":x.get("id") or "","title":t,"record_type":article_class(x),
                  "primary_topic_id":str(tp.get("id") or "").rsplit("/",1)[-1],
                  "primary_topic_name":tp.get("display_name") or "",
                  "abstract_present":int(bool(a)),"themes":";".join(theme),
                  "title_only_themes":";".join([k for k,rx in RX.items() if rx.search(t)])})
                encoded=(json.dumps(x,ensure_ascii=False,sort_keys=True)+"\n").encode("utf-8")
                raw_bytes.update(encoded)
            audits.append({"journal":journal,"year":year,"api_count":n,"downloaded":len(results),
              "source":source,"date_min":str(first),"date_max":str(last),"pages":page})
    corpus_file=OUT/"paper_index.csv"
    writecsv(corpus_file,list(rows[0]),rows)
    group=collections.defaultdict(list)
    for r in rows:
        group[r["journal"],r["year"]].append(r)
    auditrows=[];topicrows=[];themerows=[]
    for a in audits:
        j,y=a["journal"],a["year"]
        group_rows=group[j,y]
        proxy=[r for r in group_rows if r["record_type"]=="article_proxy"]
        ytd=[r for r in proxy if ym_day(dt.date.fromisoformat(r["date"]))<=ym_day(END)]
        counts=collections.Counter()
        topics=collections.Counter()
        title_counts=collections.Counter()
        for r in proxy:
            counts.update(r["themes"].split(";") if r["themes"] else [])
            title_counts.update(r["title_only_themes"].split(";") if r["title_only_themes"] else [])
            if r["primary_topic_id"]:topics[r["primary_topic_id"],r["primary_topic_name"]]+=1
        den=len(proxy)
        auditrows.append({**a,"article_proxy":den,"same_cutoff_article_proxy":len(ytd),
          "missing_abstract":sum(not r["abstract_present"] for r in proxy),
          "missing_doi":sum(not r["doi"] for r in group_rows),
          "missing_primary_topic":sum(not r["primary_topic_id"] for r in proxy),
          "excluded_or_suspected":len(group_rows)-den,
          "classification_warning":"article_proxy != publisher original research"})
        for theme in TAXONOMY:
            n=counts[theme]
            themerows.append({"journal":j,"year":y,"theme":theme,"n":n,"denominator":den,
                  "share_pct":round(n*100/den,3) if den else None,
                  "title_only_n":title_counts[theme]})
        for (tid,label),n in topics.items():
            topicrows.append({"journal":j,"year":y,"topic_id":tid,"topic":label,
              "n":n,"denominator":den,"share_pct":round(n*100/den,3)})
    writecsv(OUT/"corpus_audit.csv",list(auditrows[0]),auditrows)
    writecsv(OUT/"theme_counts.csv",list(themerows[0]),themerows)
    writecsv(OUT/"native_topic_counts.csv",["journal","year","topic_id","topic","n","denominator","share_pct"],topicrows)
    trend=[]
    for j in SOURCES:
        for left,right,mode in [(2024,2025,"full_year"),(2025,END.year,"matched_ytd"),(2024,END.year,"matched_ytd")]:
            if left==right or (j,left) not in group or (j,right) not in group:continue
            def filtered(y):
                items=[r for r in group[j,y] if r["record_type"]=="article_proxy"]
                if mode=="matched_ytd":
                    items=[r for r in items if ym_day(dt.date.fromisoformat(r["date"]))<=ym_day(END)]
                return items
            x,y=filtered(left),filtered(right)
            if not x or not y:raise RuntimeError("Empty comparator")
            for theme in TAXONOMY:
                nx=sum(theme in r["themes"].split(";") for r in x)
                ny=sum(theme in r["themes"].split(";") for r in y)
                px=100*nx/len(x);py=100*ny/len(y)
                trend.append({"journal":j,"earlier":left,"later":right,"window":mode,"theme":theme,
                  "n_earlier":nx,"den_earlier":len(x),"pct_earlier":round(px,3),
                  "n_later":ny,"den_later":len(y),"pct_later":round(py,3),
                  "change_pp":round(py-px,3)})
    writecsv(OUT/"trend_comparisons.csv",list(trend[0]),trend)
    s=["# WR × ES&T — OpenAlex current-classifier journal census",
      "",f"Retrieved: {dt.datetime.now(dt.timezone.utc).isoformat()} | End date: {END}",
      "","> Corpus is all retrievable OpenAlex source-indexed records, not publisher-certified original research. Article_proxy excludes obvious nonresearch but is not authoritative.",
      "", "## Corpus QA",
      "|Journal|Year|API works|Article proxy|Missing abstract (proxy)|Missing DOI (all)|","|---|---:|---:|---:|---:|---:|"]
    for a in auditrows:
        s.append(f"|{a['journal']}|{a['year']}|{a['api_count']}|{a['article_proxy']}|{a['missing_abstract']}|{a['missing_doi']}|")
    for j in SOURCES:
        s+=["",f"## {j}: largest increases 2024→2025 (publication share, pp)"]
        rank=sorted((r for r in trend if r["journal"]==j and r["window"]=="full_year"),key=lambda x:x["change_pp"],reverse=True)
        for r in rank[:7]:
            s.append(f"- {r['theme']}: {r['n_earlier']}/{r['den_earlier']} ({r['pct_earlier']}%) → {r['n_later']}/{r['den_later']} ({r['pct_later']}%): {r['change_pp']:+.3f} pp")
        s+=["",f"### {j}: 2026 matched-year-to-date increases"]
        rank=sorted((r for r in trend if r["journal"]==j and r["earlier"]==2025 and r["later"]==2026 and r["window"]=="matched_ytd"),key=lambda x:x["change_pp"],reverse=True)
        for r in rank[:7]:
            s.append(f"- {r['theme']}: {r['pct_earlier']}% → {r['pct_later']}% ({r['change_pp']:+.3f} pp)")
    s+=["","## Caveats","- Multi-label keyword extraction is preliminary and requires stratified manual precision/recall audit.",
        "- Topic classifier was updated in October 2026; this report uses one contemporaneous snapshot.",
        "- Do not infer novelty or editorial acceptance preference from publication shares.",
        "- Indexing lag may affect the 2026 estimate; OpenAlex publisher source assignments may differ from official publisher journals.",
        "- Actual source-verified research Article classification and special-issue stratification remain separate work.",
        "","## Provenance",f"OpenAlex query sources: {SOURCES}; raw records SHA256: {raw_bytes.hexdigest()}"]
    (OUT/"REPORT.md").write_text("\n".join(s)+"\n",encoding="utf-8")
    marker={"status":"INDEXED_CORPUS_ACQUIRED","journal_sources":SOURCES,"start":str(START),"end":str(END),
       "retrieved_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
       "total_records":len(rows),"raw_records_sha256":raw_bytes.hexdigest(),
       "qa":"All API page counts matched; record source/year validated; DOI/ID duplicates checked",
       "limitations":"OpenAlex source-indexed corpus; original-research publisher verification and classification precision not established"}
    (OUT/"COMPLETE.json").write_text(json.dumps(marker,indent=2)+"\n",encoding="utf-8")
    print("CENSUS COMPLETE:",len(rows),json.dumps({k:marker[k] for k in ["status","raw_records_sha256"]}))
if __name__=="__main__":
    try:main()
    except Exception as e:
        print("CENSUS INCOMPLETE; do not release trend conclusions:",repr(e),file=sys.stderr)
        raise
