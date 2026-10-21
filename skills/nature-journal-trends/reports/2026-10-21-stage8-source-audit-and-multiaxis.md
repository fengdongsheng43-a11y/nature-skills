# WR × ES&T Stage 8: frozen corpus, source audits and minimal corrections

Date: 2026-10-21. **Research decision:** do not publish the final publisher-certified original-article hot-topic ranking yet.

## Frozen data
- Actions run 39550517919, artifact 12323172934: 12,936 OpenAlex source-indexed works covering 2024-01-01 through 2026-10-21.
- Former OpenAlex-based article_proxy: 12,033 records. Previous nine source-confirmed nonoriginals; this round finds three more, making 12 confirmed exclusions and **12,021** remaining article_proxy (not a publisher-verified corpus).
- Three newly confirmed: DOI 10.1021/acs.est.4c02659 (PubMed Review, 2024), 10.1021/acs.est.6c01695 (ACS Perspective, 2026), 10.1021/acs.est.6c08923 (ACS Viewpoint, 2026).
- Fixed 164-paper stratified sample: 29 prior source-inspected, 31 newly source-inspected, **60/164** with publisher/PubMed-level source corroboration; **104** still need source review. No precision or recall estimate from this nonrandom verified subset.
- Among 31 source-inspected new samples, at least eight have different online-year and journal-issue-year; this is not a population prevalence estimate.

## Semantic counterexamples
- 10.1016/j.watres.2024.122384 electrochemical denitrification must not automatically be counted as *biological* denitrification.
- 10.1021/acs.est.5c04984 urine electrochemical ammonia recovery is not biological nitrogen removal.
- 10.1016/j.watres.2025.125211 is natural **river-network** nitrogen-cycle multi-omics; OpenAlex assigned wastewater treatment/nitrogen removal primary topic. Nitrogen cycling does not imply a wastewater study.
- 10.1016/j.watres.2024.123072 uses phosphate as an arsenic-remediation modifier; 10.1016/j.watres.2024.122901 is sludge-to-biochar phosphorus recovery/bioavailability. The two cannot be grouped solely on phosphate mentions.
- 10.1021/acs.est.5c13338 physical membrane transport model (MD/DFT) is not automatically AI.
- 10.1021/acs.est.6c03085 recycling discarded membranes is a materials life-cycle process, not membrane separation performance.
- 10.1021/acs.est.5c10262 adds DNA-SIP and kinetics to quantify comammox activity, stronger process evidence than functional-gene detection.
- 10.1016/j.watres.2026.127011 online 2026 but issue 2027, requiring published-online vs issue-year sensitivity.
- 10.1021/acs.est.4c00686 recompiles previous PFAS hormesis datasets; retained with a secondary-data ambiguity flag rather than automatically excluded because of publisher Article metadata.

## Jan 1-Oct 21 matched period: frozen OpenAlex primary-topic shares after 12 known exclusions
- WR nitrogen/wastewater: 10.484%, 9.310%, 11.413% in 2024, 2025, 2026 respectively.
- WR advanced oxidation: 9.311%, 10.221%, 10.487%.
- WR membrane: 4.032%, 6.055%, 4.935%.
- ES&T atmosphere/aerosol: 6.560%, 6.828%, 8.200%.
- ES&T PFAS: 6.377%, 7.353%, 7.270%. The 2026 fall is more obvious after removing the publisher-confirmed PFAS Perspective.
- ES&T microplastics: 6.744%, 7.721%, 6.889%.

**Claims allowed:** only within this fixed, source-indexed model and date/type proxy. **Not allowed:** editorial preference, acceptance rate, science-level novelty, calibrated true trend, or final publisher-certified original research ranking.

## P0
Source-check remaining 104 sampled papers and independent keyword-negative controls. Add publisher abstract and article category, freeze multi-axis labels (problem/system/process/method/evidence contribution), estimate category-specific recall and false-positive rate from defensible strata. WR bulk PubMed enrichment remains NOT VERIFIED: no manifest or DOI table was available at the last check; do not assume success.

The user-visible archive (2026-10-21) contains the 31 source URLs, old and revised axes, the updated 164 sample ledger, denominators, primary-topic impact and reproducibility code. Parent decision Skill in this fork main and journal-trend specialist Skill on this branch govern the claim status.
