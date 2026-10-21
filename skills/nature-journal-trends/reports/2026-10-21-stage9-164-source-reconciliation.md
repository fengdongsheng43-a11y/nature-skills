# Stage 9 — Fixed 164-sample DOI source reconciliation

**Date:** 2026-10-21. **Scope:** Water Research + Environmental Science & Technology, 2024-01-01 through 2026-10-21. Nature Water excluded; AFM not a full-journal denominator.

## Skill governance
Scientific decisions obey fork main `skills/nature-research-partner/SKILL.md` and `references/research-state-machine-and-anti-leakage.md`; bibliometric specialist scope obeys feature `skills/nature-journal-trends/SKILL.md`, `references/corpus-and-sampling.md` and `references/temporal-and-journal-inference.md`.

## Primary observations and QA
- Frozen OpenAlex indexed works: **12,936**. Baseline article_proxy: **12,033**. Verified review/synthesis/perspective exclusions: **13**, including newly publisher-confirmed ES&T Perspective DOI `10.1021/acs.est.6c03733`. Minimally corrected proxy: **12,020**. Neither term "full publisher-certified original research" nor "complete semantic census" is justified.
- Stratified fixed sample **164/164 unique DOI records have a grounded source URL**, WR 83 and ES&T 81. Previously source supported: 60. This round: 104 more. Out of the **104 new**, 96 have accessible journal/PubMed abstracts, 6 explicitly publisher Research article types, 1 explicitly publisher Perspective, and 1 DOI/title matched only to the UNSW author's official institutional publication list. Thus **163/164 have source-level content/type corroboration, 1/164 remains metadata-only**.
- The institutional metadata-only record is WR DOI `10.1016/j.watres.2026.127127`, source https://research.unsw.edu.au/people/associate-professor-min-zheng/publications . Do not claim its underlying methods or article type verified.
- All 164 fixed sample DOIs unique, URL nonblank. 104 newly matched source DOIs unique. Previous and new matches were not forced into a fabricated independent double-coder accuracy statistic.
- Separate PubMed bulk DOI metadata recovery still has NO confirmed `PUBMED_MANIFEST.json`; earlier `WORKFLOW_STATUS.json` showed snapshot restore failure and PubMed stage skipped. Individual PubMed article-page access is not bulk recovery.

## Matched YTD OpenAlex native single-primary-topic shares: minimal exclusions (2024, 2025, 2026)
- WR nitrogen/wastewater: 143/1364 (10.484%), 143/1536 (9.310%), 185/1621 (11.413%).
- WR advanced oxidation water treatment: 127/1364 (9.311%), 157/1536 (10.221%), 170/1621 (10.487%).
- WR membrane separation: 55/1364 (4.032%), 93/1536 (6.055%), 80/1621 (4.935%).
- ES&T atmosphere/aerosol: 107/1631 (6.560%), 130/1904 (6.828%), 194/2365 (8.203%).
- ES&T PFAS: 104/1631 (6.377%), 140/1904 (7.353%), 172/2365 (7.273%).
- ES&T microplastics: 110/1631 (6.744%), 147/1904 (7.721%), 163/2365 (6.892%).
- Period all years Jan1–Oct21. These are **model-primary-topic indexed publication shares**, not human-validated scientific topic shares. Compare same index snapshot and date cutoffs only.

## Challenging counterexamples
- ES&T `10.1021/acs.est.5c09128`: electro-Fenton + membrane biofouling + anammox nitrogen, belongs to multiple concept axes.
- ES&T `10.1021/acs.est.6c02708`: HPRO support-layer compaction and resistance measured experimentally; distinguish actual transport measurement vs material marketing.
- ES&T `10.1021/acs.est.4c06425`: online Dec25 2024 but issue Jan14 2025; DOI year is NOT issue year.
- WR `10.1016/j.watres.2025.125084`: online Nov30 2025 but issue Feb15 2026; avoid mixing dates.

## Claim states and stop gates
- Supported-within-boundary: counts/shares of native primary topics in frozen OpenAlex indexed article_proxy, after 13 DOI-grounded non-original exclusions.
- Evidence-incomplete: true prevalence of overlapping environmental topic processes, all-original research type denominator, multi-year rise in substantive scientific novelty.
- Not-identifiable: journal editorial preference/acceptance odds and any frontier novelty/gap without the parent's five-pass literature gate.
- STOP_CLASSIFICATION: no independently double-coded human gold labels; no probability-sampled title-negative controls; WR has 78–83% missing abstracts. 164 source corroborations do not estimate precision/recall.
- STOP_CORPUS: source-indexed OpenAlex is not verified against complete official WR and ES&T issue lists.

## P0 next
Draw reproducible probability sample of title-negative controls stratified by journal/year/native-topic, gather journal abstract/methods, independently label problem/system/process/method/evidence, adjudicate, report class-specific confusion and weighted uncertainty; then recalculate journal trend shares and indexing lag/online-vs-issue sensitivity. Keep AI methods separate from generic predictive modeling. Do not issue final topic preference rankings before this.

## User-facing deliverables (conversation files)
- `WR_EST_第九阶段_164篇来源证据与最小校正.xlsx`
- `WR_EST_第九阶段_164篇来源审计与趋势结论边界.md`
- `WR_EST_第九阶段_164篇来源证据包.zip`
The compressed evidence pack contains 104-row source list, 164-row audit ledger, source-supported minimal trend changes, provenance script, and verification status JSON; source URL per row.
