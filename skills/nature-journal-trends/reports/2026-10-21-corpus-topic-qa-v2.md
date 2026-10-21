# WR and ES&T publication-topic QA (2026-10-21)

OpenAlex source-indexed corpus: 12,936 works from 2024-01-01 through 2026-10-21; 12,033 tentative article_proxy records. Source: https://github.com/fengdongsheng43-a11y/nature-skills/actions/runs/39550517919

## Coverage bias
WR abstract missing: 2024 1326/1711 (77.5%), 2025 1531/1930 (79.3%), 2026 1340/1622 (82.6%).
ES&T abstract missing: 2024 14/2002 (0.7%), 2025 38/2400 (1.6%), 2026 62/2368 (2.6%).
Use title-only prevalence as a common-denominator sensitivity check; confirm with current OpenAlex primary-topic categories. These coding rules use partially overlapping inputs and do not establish independent ground truth.

## Same-direction title/native-topic shifts (percentage points)
2024 to 2025, whole years:
- WR membranes +1.75 / +1.84; microplastics +1.16 / +0.44; advanced oxidation +0.84 / +1.29.
- ES&T PFAS +1.51 / +1.13; microplastics +1.21 / +0.64.

2025 to 2026 (same Jan 1–Oct 21 cutoff):
- WR membranes -3.37 / -1.40; biological nitrogen +1.69 / +2.10.
- ES&T atmospheric aerosol +1.51 / +2.07; microplastics -0.78 / -0.84.
- WR AI/modeling title-only +2.07, no semantically equivalent native primary topic.
- ES&T PFAS title-only +0.64 versus native -0.05: not consistent.

## Verified automatic coding failure examples
- 10.1021/acs.est.5c14462 organic phosphate toxicity was incorrectly tagged phosphorus cycling.
- 10.1021/acs.est.4c00765 electrochemical N2O reduction was incorrectly tagged biological nitrogen.
- 10.1016/j.watres.2026.126959 water suspended particulate matter was incorrectly tagged atmospheric aerosols.
- 10.1016/j.watres.2025.124530 overview of meta-analyses passed tentative original-article selection.

A stratified sample of 164 works was created for a future manual source-verified audit; no human coding score is claimed.

## Gate
Do not infer sustained multi-year growth from 2024->2025 alone; many 2026 trends reversed. Do not claim editorial preference, originality, accepted-only acceptance rates or topic saturation from indexed counts. Next: publisher article-type validation, WR abstract supplementation, calibrated taxonomy, recomputation and sensitivity analysis.

Official reference: https://blog.openalex.org/same-topics-better-assignments-a-new-topic-classifier-for-openalex/
