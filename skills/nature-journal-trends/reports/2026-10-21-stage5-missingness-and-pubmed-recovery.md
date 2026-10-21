# Stage 5 — WR × ES&T missing-abstract and keyword-detection audit (2026-10-21)

## Frozen contract
- Parent: fengdongsheng43-a11y/nature-skills main / skills/nature-research-partner/SKILL.md.
- Specialist: feature/nature-journal-trends / skills/nature-journal-trends/SKILL.md.
- Dataset: GitHub Actions run 39550517919, artifact 12323172934; 12,936 source-indexed OpenAlex works, article_proxy n=12,033; 2024-01-01 through 2026-10-21. Original publisher research-article census remains NOT VERIFIED.
- This stage audited missingness and labeling; it did NOT modify the frozen article denominator or release a finalized topic ranking.

## Six journal-year missingness results
| Journal | Year | article_proxy | abstracts | missing | missing % | No-title-label papers rescued by abstract *among abstract-available only* |
|---|---:|---:|---:|---:|---:|---:|
| WR | 2024 | 1,711 | 385 | 1,326 | 77.50 | 132 |
| WR | 2025 | 1,930 | 399 | 1,531 | 79.33 | 122 |
| WR | 2026 YTD | 1,622 | 282 | 1,340 | 82.61 | 95 |
| ES&T | 2024 | 2,002 | 1,988 | 14 | 0.70 | 637 |
| ES&T | 2025 | 2,400 | 2,362 | 38 | 1.58 | 905 |
| ES&T | 2026 YTD | 2,368 | 2,306 | 62 | 2.62 | 790 |

The matched abstract-available subset is non-random and cannot be used to extrapolate a missing-abstract topical correction without validating the selection mechanism.

## Topic-specific labeling discordance
Among WR 2025 papers whose OpenAlex current primary topic equals the following:
| Native topic | n | Abstract available % | Same-topic title keyword detected % |
|---|---:|---:|---:|
| Membrane Separation Technologies | 114 | 12.28 | 91.23 |
| Microplastics and Plastic Pollution | 101 | 19.80 | 87.13 |
| PFAS research | 53 | 20.75 | 66.04 |
| Wastewater Treatment and Nitrogen Removal | 180 | 20.00 | 50.00 |
| Advanced oxidation water treatment | 202 | 11.39 | 33.17 |

These percentages are **not empirical recall**, because OpenAlex primary topics are machine-assigned and share title evidence with the keyword classification. The two coding systems have different semantic boundaries. They are discrepancies worth inspection.

A total of 172 journal × year × native-topic groups (at least 15 records each) were analyzed. In 1,861 records the title keyword did not reproduce the mapped native topic; these are unresolved coding disagreements, NOT independently confirmed errors.

## 164-source sample
- WR 83; ES&T 81; 2024/2025/2026 51/59/54.
- Only 14 have directly traceable external source corroboration, with 150 remaining source-unverified. No precision/recall estimate is justified.
- Stage4 source-confirmed minimal exclusion of 8 synthesis/review cases is a separate result; this stage neither deletes nor redefines that denominator.

## PubMed rescue diagnosis and repair
The first structured result at 2026-10-21T10:17Z reported restore_outcome=failure, pubmed_outcome=skipped, manifest_exists=false. The failure is at frozen artifact restoration, **not a PubMed DOI negative result**.

On the separate feature branch, changed workflow .github/workflows/wr-pubmed-qa.yml to restore the exact frozen artifact using official actions/download-artifact@v4 with run-id=39550517919, name=wr-est-census-2026-10-21, and explicit verification of 12,936 rows before DOI matching. The workflow also publishes explicit status even if later stages fail. Do NOT claim rescue success until both restored snapshot integrity and PUBMED_MANIFEST.json/DOI table are verified.

## Claim ledger
- Claim: title-based WR membrane topic grew monotonically through 2026: contradicted within frozen title coding; 2025 was higher than 2026. Do not imply a scientific mechanism for the temporal difference.
- Claim: actual topic frequency equals title-only hit share: contradicted by abstract-available subset and native-title inconsistencies; require source-based calibrated coding.
- Claim: classification topic mismatch count = labeling error count: NOT IDENTIFIABLE; both classifiers have different concepts and neither is source-truth.
- Claim: official journal original article shares are known: evidence-incomplete due the article_proxy/classification uncertainty.
- Claim: journal editorial acceptance preference established: not identifiable without submission/rejection denominator.

## P0 next
Recover abstract coverage and DOI-matched article types; stratify by journal/year/topic and original article status; adjudicate the 164 sample from accessible original abstracts/methods plus a random no-keyword sample; estimate topic-specific false positive/negative rates with sources and provenance; rerun trends and 2026 lag sensitivity. Avoid premature prioritization based on prevalence alone.

## Independent fallback workflow (separate snapshot, not the frozen census)
- Added `.github/workflows/wr-pubmed-selfcontained.yml` on the same development branch; combines a fresh OpenAlex census with PubMed DOI cross-check in **one** Actions job, eliminating cross-run artifact dependency.
- Fresh retrieval is **not** assumed identical to run 39550517919. The workflow exports an INDEPENDENT_STATUS.json with new row count and raw-record hash alongside the old frozen row/hash, before any cross-snapshot comparison.
- The new workflow file being present proves only deployment; DOI rescue is **not** complete until PUBMED_MANIFEST.json and row-linked DOI table exist and are checked. It does not retroactively repair the 2026-10-21 original corpus.
- In type-suspect queue n=52, 45 titles contain 'synthesis' and 6 contain 'overview'. Those strings are often part of experimental research titles; they are risk flags, **not** basis for automatic deletion.
