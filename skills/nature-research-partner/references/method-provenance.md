# Method provenance

This skill combines in-repository Nature Skills principles with independently reviewed ideas from public scientific-agent projects. The concepts were adapted into a new research-decision workflow rather than copied as a single upstream skill.

## In-repository foundations

### `nature-paper-card`

The existing research-idea gates contributed the principles of traceability, falsifiable hypotheses, explicit delta from prior work, validation plans, failure modes, and conservative novelty language.

### `nature-reviewer`

The reviewer skill contributed severity calibration, evidence pointers, non-invention, independent skeptical review, and the principle that strong criticism should be tied to the central case rather than to stylistic hostility.

### `nature-statistics`

The statistics skill contributed separation of experimental unit, analytical unit, measured quantity, inferential claim, uncertainty, and the rule against upgrading association to mechanism or causality.

## External inspirations reviewed on 2026-08-26

### K-Dense-AI/scientific-agent-skills — `hypothesis-generation`

Adapted concepts: freeze observation before interpretation; document evidence boundaries; generate rival explanations; distinguish claim types; derive discriminating predictions; define falsification and controls; separate planned from post-hoc analyses; update hypotheses after contrary evidence.

### K-Dense-AI/scientific-agent-skills — `experimental-design`

Adapted concepts: start from the scientific question and experimental unit; treat randomization, replication, and blocking as structural design decisions; identify nuisance variables; avoid pseudoreplication; match analysis to design.

### wanshuiyin/Auto-claude-code-research-in-sleep — `ablation-planner`

Adapted concepts: every extra experiment must state what it tests; prioritize tests that isolate a component or mechanism; identify unnecessary experiments; order experiments for early information.

### wanshuiyin/Auto-claude-code-research-in-sleep — `analyze-results`

Adapted concepts: separate observation, interpretation, implication, and next experiment. This skill adds explicit rival explanations and research-state updating.

### wanshuiyin/Auto-claude-code-research-in-sleep — `auto-review-loop`

Adapted concepts: preserve research state across iterations and use independent critical review. This skill does not copy the ML-specific reviewer backend or automatic acceptance thresholds.

## Deliberately not adopted

The skill does not adopt arbitrary numeric novelty scores, decorative probability estimates, forced hypothesis quotas, or scenario-weighting rules without scientific calibration.

The skill also does not assume that an AI reviewer is independent merely because it uses a different prompt. Independence must be described conservatively if the runtime cannot guarantee isolated contexts or model separation.


## v0.2 evidence-first routing update

The partner now treats literature retrieval as a mandatory decision gate after initial problem clarification and before literature-dependent mechanism strengthening, novelty judgment, SOTA judgment, method-validity claims, or publication-level design. This update strengthens the orchestration role of `nature-academic-search`, `nature-reader`, and `nature-paper-card`; it does not copy their implementation or duplicate their search engines.
