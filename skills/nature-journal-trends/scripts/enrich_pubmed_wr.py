#!/usr/bin/env python3
"""DOI-matched PubMed augmentation for WR 2024-2026 journal census.

External source provides PubMed article types and abstracts when available.
Never mark every 'Journal Article' as empirically original research.
Never overwrite the frozen OpenAlex corpus or use PubMed as census denominator.
"""
import collections,csv,datetime as dt,json,os,time,urllib.parse,urllib.request,xml.etree.ElementTree as ET
from pathlib import Path

D=Path("skills/nature-journal-trends/data/enrichment")
D.mkdir(parents=True,exist_ok=True)
SRC=Path(os.getenv("CENSUS_CSV","skills/nature-journal-trends/data/latest/paper_index.csv"))
R=list(csv.DictReader(SRC.open(encoding="utf-8-sig")))
WR=[x for x in R if x["journal"]=="WR"]
assert len(R)>12000 and len(WR)>5000
DOI={x["doi"].lower():x for x in WR if x["doi"]}
HEAD={"User-Agent":"JournalTrendResearch/1.0 (metadata QA)"}
EMAIL=os.getenv("NCBI_EMAIL","")
def get(base,params):
    if EMAIL: params["email"]=EMAIL
    url=base+"?"+urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers=HEAD),timeout=100) as x:return x.read()
        except Exception as e:
            print("fetch retry",attempt,type(e).__name__,str(e)[:100],flush=True)
            if attempt==4:raise
            time.sleep(2**attempt)
    raise RuntimeError("retrieval failed")

ids=json.loads(get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",{
    "db":"pubmed","term":'"Water Res"[jour] AND ("2023/01/01"[Date - Publication] : "2027/12/31"[Date - Publication])',
    "retmax":15000,"retmode":"json"
}).decode())
total=int(ids["esearchresult"]["count"]); pmids=ids["esearchresult"]["idlist"]
if len(pmids)!=total or not (3000<=total<=15000):raise RuntimeError(f"Unexpected PubMed count: {total}, IDs {len(pmids)}")
print("PubMed records",total,flush=True)
meta={}; typecounts=collections.Counter()
for i in range(0,len(pmids),300):
    xml=get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",{
         "db":"pubmed","id":",".join(pmids[i:i+300]),"retmode":"xml"})
    root=ET.fromstring(xml)
    for art in root.findall(".//PubmedArticle"):
        idnode=art.find(".//MedlineCitation/PMID")
        pmid=idnode.text.strip() if idnode is not None and idnode.text else ""
        doi=""
        for idd in art.findall(".//PubmedData/ArticleIdList/ArticleId"):
            if idd.attrib.get("IdType")=="doi":doi=(idd.text or "").strip().lower()
        if not doi or doi not in DOI:continue
        ab=art.findall(".//Article/Abstract/AbstractText")
        abstract=" ".join(" ".join("".join(node.itertext()).split()) for node in ab)
        types=[("".join(t.itertext()).strip()) for t in art.findall(".//PublicationTypeList/PublicationType")]
        typecounts.update(types)
        meta[doi]={"pmid":pmid,"abstract":abstract,"publication_types":types}
    print("Fetched",min(i+300,total),"/",total,"matched",len(meta),flush=True)
    time.sleep(.5)
out=[];year=collections.defaultdict(collections.Counter)
for r in WR:
    d=r["doi"].lower(); m=meta.get(d,{})
    ptypes=m.get("publication_types",[])
    review=any(x.lower() in {"review","systematic review","meta-analysis"} for x in ptypes)
    abstract=m.get("abstract","")
    y=r["year"]; stat=year[y]
    stat["indexed_WR"]+=1
    if r["record_type"]=="article_proxy":stat["article_proxy"]+=1
    if r["abstract_present"]=="0":stat["openalex_abstract_missing"]+=1
    if m:stat["pubmed_doi_matched"]+=1
    if r["abstract_present"]=="0" and abstract:stat["abstract_rescued"]+=1
    if review:stat["pubmed_review_flag"]+=1
    if r["record_type"]=="article_proxy" and review:stat["review_in_article_proxy"]+=1
    out.append({"doi":d,"year":y,"record_type_openalex":r["record_type"],
        "openalex_abstract_present":r["abstract_present"],"pmid":m.get("pmid",""),
        "pubmed_abstract_present":int(bool(abstract)),"pubmed_types":"; ".join(ptypes),
        "pubmed_review_flag":int(review),"pubmed_url":("https://pubmed.ncbi.nlm.nih.gov/"+m["pmid"]+"/") if m else ""})
# Do not circulate copyrighted abstract prose: only coverage, article-type and URL metadata.
with (D/"wr_pubmed_doi_metadata.csv").open("w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
manifest={"source":"NCBI PubMed E-utilities esearch/efetch XML, DOI match to frozen OpenAlex",
          "run_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"pubmed_search_n":total,
          "matched_dois":len(meta),"WR_indexed":len(WR),"year":{y:dict(s) for y,s in sorted(year.items())},
          "abstract_text_not_exported":True,
          "limited": "A PubMed DOI-matched subset only; not complete article-type verification or a secondary WR census"}
(D/"PUBMED_MANIFEST.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
print(json.dumps(manifest,indent=2),flush=True)
