# Stage 7 — source-level publication type audit and trend reversal-budget checks

**Status:** completed bounded audit; NOT publisher-certified full-journal original-article census.

## Frozen baseline and governance
- Parent skill: fork `main/skills/nature-research-partner/SKILL.md`.
- Specialist: this feature branch's `skills/nature-journal-trends/SKILL.md`.
- OpenAlex frozen run 39550517919, artifact 12323172934; 12,936 works, 12,033 article_proxy.
- Nine publisher/abstract source-confirmed nonoriginals removed from the proxy: previous eight, plus `10.1016/j.watres.2024.121492`, labelled Review on ScienceDirect. Proxy after minimal exclusions: **12,024**.
- Do not silently treat this proxy as official original research. Same Jan1–Oct21 period for 2024, 2025, 2026; 2026 YTD.

## Newly source-audited challenge examples
- WR 2025 `10.1016/j.watres.2025.123172`: publisher Research article; deep multimodal learning for algae; title keyword rule had no AI label, native main topic was aquatic phytoplankton.
- ES&T 2025 `10.1021/acs.est.5c03787`: original cloud-water pesticides measurements; main topic pesticide, title lacks prior atmosphere keywords.
- ES&T 2025 `10.1021/acs.est.5c04868`: original microplastic image-method study with labelled data; multi-axes microplastics + method + machine learning.
- WR 2026 `10.1016/j.watres.2026.125833`: physic-based sampling mesh correction model, not a review.
- ES&T 2026 `10.1021/acs.est.5c17749`: 12 AFFF-soil cores at 10 installations, original PFAS fate survey.
- WR 2025 `10.1016/j.watres.2025.123263`: empirical WBE calibration with cross-country independent validation, despite suspected article-type title.
- WR 2026 `10.1016/j.watres.2026.126483`: original multi-facility fecal indicator test and proxy-failure analysis.
- WR 2026 `10.1016/j.watres.2026.126690`: publisher marks Research article, DRL urban drainage robustness.

16 DOI records externally inspected or flagged for date discrepancy in this pass; 15 newly externally corroborated works overlap the previous 164-stratum sample. Prior 14 verified + 15 newly corroborated = **29/164** with external evidence; 135 remain without external source-level corroboration. This is not a randomly audited error rate.

## Falsification budget
For a topic-share change across two years with denominators fixed, compute how few single-paper primary-topic assignments must be changed in ONE year to make the increase/decrease disappear. It is a deterministic theoretical overturn budget, not measured errors, probability or significance.

Exact Jan–Oct21 2024/2025/2026 topic shares (9-paper minimal exclusion):
- WR biological nitrogen: 10.484 / 9.310 / 11.413%; min flips 17 then 33, nonmonotonic.
- WR AOP: 9.311 / 10.221 / 10.487%; min flips 13 then **5**; 2026 rise is fragile to minor relabeling.
- WR membrane: 4.032 / 6.055 / 4.935%; min flips 28 then 18; 2025 peak.
- ES&T atmosphere/aerosol: 6.556 / 6.828 / 8.193%; min flips **5** then 26; even 2024→2025 increase is sensitive.
- ES&T PFAS: 6.373 / 7.353 / 7.306%; min flips 16 then **1**, no credible claim of sustained increase.
- ES&T microplastics: 6.740 / 7.721 / 6.883%; 16 then 16; 2025 peak.
All are OpenAlex single primary-topic shares, not manually validated environmental theme truth.

## Competing explanations
- Algorithmic primary-topic changes and missing WR abstracts vs real subject change;
- online vs issue publication dates near year boundary;
- original vs review/synthesis type misattribution;
- terminology drift and multiple scientific axes collapsed into a single topic;
- indexing lag and special-issue effect.

## Claim and Decision
- Allowed: named OpenAlex primary-topic shares and DOI-confirmed correction in this fixed indexed corpus.
- Not allowed: confirmed full original-research hotspots, editor preference, acceptance probability, novelty/saturation, forecast.
- Remaining P0: DOI-matched PubMed abstract/type manifest (still NOT VERIFIED in branch at this write), stratified source-level coding for the remaining 135/164 + random title-negative controls, then topic-specific false-positive/false-negative assessment and refreshed matched-window calculations.

Complete user-downloadable audit outputs in the 2026-10-21 conversation: `WR_EST_第七阶段_来源核验及趋势抗误差审计.xlsx`, `WR_EST_第七阶段_来源核验及趋势抗误差分析.md`, individual CSV ledgers.
