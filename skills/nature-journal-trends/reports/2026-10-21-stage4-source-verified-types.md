# Stage 4: WR × ES&T source-verified article-type correction (2026-10-21)

## Scope and source
- Governing skill: fork/main skills/nature-research-partner/SKILL.md; specialist: feature/nature-journal-trends/SKILL.md.
- Frozen original corpus: 12,936 OpenAlex source-indexed works from https://github.com/fengdongsheng43-a11y/nature-skills/actions/runs/39550517919/artifacts/12323172934, 2024-01-01 through 2026-10-21.
- Original article_proxy: 12,033; only EIGHT externally verified review/meta-analysis/synthesis records are excluded in this pass; minimal corrected article_proxy: 12,025. All other records remain unverified for exact publisher article type.
- 164 stratified title sample: previous 7 source-inspected records, now 14 unique records with source corroboration; majority remain unverified, no sample-derived sensitivity or accuracy statistic is claimed.
- 18 DOI source-judgment records cataloged, INCLUDING a title-only suspected commentary not counted among verified exclusions.
- New local reproducibility files: WR_EST_第四阶段_论文类型证据与热点最小校正.xlsx, WR_EST_第四阶段_来源核验与最小校正报告.md, stage4 source CSVs and MANIFEST.

## Known source-grounded exclusions from 12,033 proxy (8)
- 10.1016/j.watres.2024.121111 — publisher explicitly Review.
- 10.1016/j.watres.2024.121250 — publisher review/overview literature synthesis.
- 10.1016/j.watres.2025.124530 — umbrella review of meta-analyses.
- 10.1016/j.watres.2025.125126 — publisher abstract states Review.
- 10.1016/j.watres.2026.126240 — systematic literature review of 162 articles.
- 10.1021/acs.est.5c11764 — ACS labels Review.
- 10.1021/acs.est.5c10601 — ACS labels Review.
- 10.1021/acs.est.3c06177 — meta-analysis of 110 papers; ACS displays Article, but belongs to separately counted evidence-synthesis stratum when primary-empirical subset is targeted.

## Counterexamples retained in primary-research proxy
- 10.1021/acs.est.4c09088: original PFAS-alternative database construction and screening; 'Overview' in title is not proof of Review.
- 10.1021/acs.est.5c04682: original >90 structure-fire experiments.
- 10.1016/j.watres.2026.125798: source abstract confirms neural-network forecasting research.
- 10.1016/j.watres.2026.126336: source abstract confirms original predictive-model evaluation.
- 10.1021/acs.est.6c09154: nitrate **electroreduction** not biological nitrogen cycling; preserve process distinction.

## Minimal-correction percentages, Jan1-Oct21 each year; v3 TITLE proxy
| Journal | Topic | 2024 | 2025 | 2026 | Verdict |
|---|---|---:|---:|---:|---|
| WR | Water membranes | 5.4212% | 7.0312% | 4.5651% | 2025 peak |
| WR | Biological nitrogen | 8.0586% | 6.3151% | 8.0814% | 2025 trough; taxonomy not fully verified |
| WR | AI/prediction | 4.0293% | 5.0130% | 7.4028% | title-term candidate rises; real AI contributions unknown |
| ES&T | PFAS | 5.1471% | 7.1429% | 6.7145% | 2025 peak; 2026 v2/v3 sign disagreement |
| ES&T | Micro/nanoplastics | 5.1471% | 6.5651% | 5.6588% | 2025 peak |
| ES&T | Atmospheric/aerosols | 8.8235% | 7.2479% | 9.5861% | 2025 trough |

These fractions reflect only named-case corrections and do NOT validate all article types or category labels. No assertion of editorial preference, acceptance probability, novelty, or monotonic field change.

## P0 gates remaining
1. WR PubMed DOI rescue workflow .github/workflows/wr-pubmed-qa.yml updated to attempt DOI metadata publication; as of this checkpoint the PubMed manifest is NOT AVAILABLE on branch. Run success cannot be claimed.
2. Validate article types for remaining 12,025 paper proxy records or reproducible probabilistic stratified types.
3. Add source abstracts to WR missing subset; freeze same-day classification and estimate calibrated topic false-positive and false-negative rates on adequately stratified blinded sample.
4. Recompute full-year, matched-YTD and recent-index-lag sensitivity with identical denominators; only then strengthen topic-trend claims.

**Claim status:** trend percentages supported-within-boundary for 2026-10-21 frozen OpenAlex v3 title proxy only. Journal-specific preference not identifiable from published works. Publication-level science gaps require independent parent-skill literature gate.
