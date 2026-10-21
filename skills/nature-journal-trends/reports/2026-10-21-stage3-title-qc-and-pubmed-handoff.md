# WR–ES&T third-stage journal-corpus topic QA (2026-10-21)

## Governance and frozen boundary
- Governing parent: fork main / skills/nature-research-partner/SKILL.md, verified 2026-10-21.
- Specialist: feature/nature-journal-trends/SKILL.md and references/corpus-and-sampling.md, references/temporal-and-journal-inference.md.
- Source snapshot: https://github.com/fengdongsheng43-a11y/nature-skills/actions/runs/39550517919/artifacts/12323172934, 12,936 OpenAlex works (source-indexed) / 12,033 article_proxy; 2024-01-01 through 2026-10-21. Publisher-certified original-article denominator remains NOT VERIFIED.
- Fixed stratified sample 164: each row has DOI, original and alternative title tags, source status, original-article caveats, and review priority. The 164 samples have NOT all been verified against publisher abstracts/full texts. Seven DOI cases are checked against publisher or PubMed-level evidence, not full mechanistic audit.
- WR abstract missing within article_proxy: 1,326 / 1,531 / 1,340 for years 2024/2025/2026. This invalidates unadjusted title+abstract cross-journal topical comparisons.
- 52 proxy articles have title-based publication type flags; title alone cannot exclude or certify originals.

## Sensitivity (percentage of article_proxy journal-year corpus, identical 10-21 cutoff)
| Journal | Topic | 2024 | 2025 | 2026 | Status |
|---|---|---:|---:|---:|---|
| WR | Membrane topics | 5.486 | 7.027 | 4.562 | 2025 peak, NOT persistent growth |
| WR | Biological nitrogen | 8.047 | 6.311 | 8.076 | 2025 trough, NOT monotonic growth |
| WR | AI / prediction titles | 4.023 | 5.010 | 7.398 | candidate title-label rise, model-vs-AI unresolved |
| ES&T | PFAS titles (v3) | 5.144 | 7.143 | 6.714 | 2025 peak; v2 gives opposite 2025-to-2026 sign |
| ES&T | Micro/nanoplastics | 5.205 | 6.566 | 5.659 | 2025 peak |
| ES&T | Atmospheric aerosol | 8.818 | 7.248 | 9.586 | 2025 trough |

These are descriptive, rule-based TITLE hit shares, not semantic truth, quality, acceptance likelihood, novelty or editorial intent. Term coverage and article-type precision remain uncalibrated.

## Explicitly source-inspected falsifiers for title heuristics
- https://www.sciencedirect.com/science/article/pii/S0043135424000125 (WR 2024, explicitly Review article despite article_proxy)
- https://www.sciencedirect.com/science/article/pii/S0043135425014344 (WR 2025, umbrella review)
- https://www.sciencedirect.com/science/article/pii/S0043135424001520 (WR 2024, review-like literature survey)
- https://www.sciencedirect.com/science/article/abs/pii/S0043135425020299 (WR 2025, says 'this review')
- https://pubmed.ncbi.nlm.nih.gov/41955982/ (WR 2026, original 21-day and 90-day experimental work despite 'overview')
- https://www.sciencedirect.com/science/article/pii/S0043135425004051 (WR 2025, explicitly Research article despite vague title)
- https://pubs.acs.org/doi/10.1021/acs.est.4c09088 (ES&T 2025, original database build described despite Overview title; official article type remains to check)

## Claim-state ledger
- Claim: WR membrane topic *title share* exhibits 2025 peak. State supported-within-boundary (OpenAlex article_proxy, title-only). Mechanism of change not identified. Upgrade: source types, topic audit, partial-year indexing check.
- Claim: WR AI/prediction research grew monotonically in genuine research contributions. State evidence-incomplete. Rival: increasingly model-oriented titles and inclusion of non-AI prediction.
- Claim: ES&T PFAS share kept growing through 2026. State not-identifiable due v2/v3 2026 sign conflict. Stop strengthening.
- Claim: journal editors prefer currently prevalent topics. State evidence-incomplete; no submission denominator or direct editorial selection evidence.

## Next P0 evidence gate
A DOI-matched PubMed WR metadata enrichment script and one-off Actions workflow were submitted to this branch:
- skills/nature-journal-trends/scripts/enrich_pubmed_wr.py
- .github/workflows/wr-pubmed-qa.yml
A work-flow file commit does NOT prove execution. Do not assert PubMed rescue outcomes until artifact exists with PubMed manifest, matched DOI counts and review-type status.
Afterward: check DOI identity, recover abstract coverage on missing subset where possible, reclassify reviewed work types and rerun topic shares. Validate selected topic confusion cases directly from publisher sources. New claims must pass the parent-skill challenge/update and journal-trends fail-closed gates.

## Local analysis artifacts
User-visible spreadsheet: WR_EST_第三阶段_分类校准与164篇审计.xlsx
User-visible detailed report: WR_EST_第三阶段_全刊分类校准与来源核验.md
Additional CSV in local /mnt/data/wr_est_stage3/, generated without modifying frozen OpenAlex source.
