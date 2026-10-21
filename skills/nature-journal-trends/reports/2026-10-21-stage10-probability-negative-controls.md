# Stage 10 — Probability-sampled title-negative controls (2026-10-21)

Scope: WR and ES&T, frozen OpenAlex source-indexed corpus, 2024-01-01 to 2026-10-21.

## Governing framework
- Scientific decision Skill (fork/main): skills/nature-research-partner/SKILL.md, including claim-state control.
- Bibliometric execution Skill (feature branch): skills/nature-journal-trends/SKILL.md and its corpus/temporal references.
- No novelty, mechanism or editor preference claim is based on counts alone.

## Frozen data and new verified types
- Original indexed work records: 12,936, original raw records SHA256: 9fc682a90215596d04a05f2ef49b714448b6bb5403c4d2f068bef1284e7f8ca8.
- Preliminary article_proxy: 12,033.
- Previous publisher/source-supported nonoriginal exclusions: 13.
- Three new publisher-confirmed nonoriginal exclusions: WR DOI 10.1016/j.watres.2026.126451 (Review), ES&T 10.1021/acs.est.5c02912 (Perspective), ES&T 10.1021/acs.est.5c18400 (Viewpoint).
- Total confirmed exclusions: 16; minimally adjusted article_proxy: 12,017. Not a full publisher-certified original research universe.

## Probability sampling, actually executed
- Explicit theme families (7): WR biological nitrogen, advanced oxidation, membrane separation, AI/ML methods; ES&T PFAS, air/aerosols, micro/nanoplastics.
- Time: 2024/2025/2026, Jan1-Oct21.
- Three non-overlapping strata inside each theme-year: frozen old title-positive, title-negative/native OpenAlex primary topic support, title-negative/native other.
- SRSWOR per theme × year × stratum, fixed RNG seed 20261021, up to five per stratum, full census when stratum N<=5.
- 21 theme-year groups, 63 cells, 311 theme-paper draws, 309 distinct DOIs. Every sample stores stratum-N, sample-n, probability n/N and inverse-probability weight N/n.
- Some publications may appear more than once for different themes; the direct observation unit is theme-paper classification, not duplicated corpus output.
- Fully executable Python scripts and original-row hashes supplied in the conversation stage10 audit bundle.

## Source-level pilot
- 27/311 sampled judgments have one-pass publisher/PubMed-backed source coding; 19 judged relevant to their predeclared themes, 8 not relevant.
- The 27 were prioritized for difficult title-negative/native-topic-supported cases and other contrasting types, so **19/27 is NOT a prevalence, accuracy, precision, or recall estimate**. Only one nonblind coding pass; no second coder or inter-rater assessment.
- 284/311 remain UNKNOWN, and entire probability sample has NOT yet passed source-audited completion.
- Representative confirmed title misses: WR AOB cross-feeding 10.1016/j.watres.2026.125714; WR PMS advanced oxidation 10.1016/j.watres.2026.125981; WR AI graph attention network 10.1016/j.watres.2026.125532; ES&T GenX PFAS 10.1021/acs.est.5c13080; ES&T aerosols from biosolid processing 10.1021/acs.est.5c08034.
- Semantic boundaries: coastal bulk plastic emissions (10.1021/acs.est.5c15230) and macro foam float habitat (10.1021/acs.est.6c02850) should not automatically be narrow micro/nanoplastic-particle investigations, unlike penguin-guano microplastic measurement (10.1021/acs.est.5c17586).

## Updated matched-year-to-date model-native shares (after 16 verified type exclusions)
WR nitrogen: 10.484%, 9.310%, 11.358% (2024/25/26); WR AOP 9.311%,10.221%,10.494%; WR membrane 4.032%,6.055%,4.938%.
ES&T aerosols: 6.560%,6.831%,8.206%; PFAS 6.376%,7.357%,7.276%; microplastics 6.744%,7.672%,6.853%.

These are **index/classifier-specific single-main-topic publication shares**, not source-calibrated true prevalence. The three DOI-confirmed exclusions cannot validate the remaining 12,017 article types.

## Fail-closed state and P0
- Sampling design: COMPLETE; source-grounded sample: PARTIAL (27/311); publisher-census QA: INCOMPLETE; recall/precision & calibrated trend: **NOT ESTIMABLE**.
- Next: finish sources and original-article codes in each probability stratum; obtain independent second coder + arbitration; calculate design-weighted sensitivity / specificity and missingness uncertainty. Extra sample sizes should follow pilot variance, not subjective source convenience.
- No final science-level hot-topic ranking, acceptance odds or novel-gaps claim before gates pass.

User deliverables in the stage10 conversation: probability sampling workbook, stage10 full methodological report and executable ZIP evidence pack.
