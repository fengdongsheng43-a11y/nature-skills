# Nature Research Partner evaluation protocol

## Goal

Test whether the skill actually prevents the scientific failure modes it claims to prevent.

The evaluation is not a style benchmark. A response can be fluent and still fail if it strengthens an unsupported claim, ignores a serious rival, recommends low-information work, or lets one project's state leak into another.

## Evaluation dimensions

Score each case on these dimensions:

1. `state_legality` — hypothesis and claim states remain consistent with available evidence.
2. `anti_leakage` — unsupported claims do not silently strengthen downstream.
3. `rival_quality` — serious rivals are generated when scientifically warranted, not as ceremonial alternatives.
4. `evidence_boundary` — direct, adjacent, abstract-only, metadata-only, and speculative evidence are not conflated.
5. `decision_relevance` — next actions are chosen for information gain or decision impact rather than characterization volume.
6. `death_condition_use` — central claims expose falsifying outcomes and are actually downgraded if those outcomes occur.
7. `specialist_boundary` — technical execution is delegated without transferring scientific decision ownership.
8. `project_isolation` — unrelated active project states do not contaminate the current project.
9. `wording_control` — language strength matches the claim state.
10. `negative_evidence_update` — null, contradictory, and mechanism-killing results change the active research state.

## Pass conditions

A case passes only if all case-specific hard-fail conditions are avoided.

Do not average away a critical failure. For example, a beautiful experimental plan still fails if it labels an unverified mechanism as demonstrated.

## Recommended comparison

When testing a new version:

- run the same cases under the prior released version and candidate version;
- record material differences in scientific decisions, not only wording;
- preserve failed examples;
- add a regression case whenever a real project exposes a new failure mode.

## Evidence of verification

For each verification pass, record:

- skill version / commit;
- model/host if relevant;
- date;
- case IDs run;
- pass/fail;
- exact failure mode;
- whether the failure is in the core protocol, a reference, routing, or a specialist skill.

This directory should evolve from synthetic cases toward real, de-identified project failures whenever possible.
