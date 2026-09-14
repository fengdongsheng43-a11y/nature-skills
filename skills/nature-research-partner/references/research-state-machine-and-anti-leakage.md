# Research state machine and anti-leakage protocol

## Purpose

Turn scientific reasoning rules into explicit state constraints so unsupported interpretations cannot silently become stronger claims downstream.

This protocol separates five linked objects:

1. `Observation` — what was measured, reported, or directly retrieved.
2. `Hypothesis` — a candidate explanation that can be strengthened, weakened, rejected, superseded, or remain unresolved.
3. `Evidence` — an observation or source linked to a specific claim or hypothesis with provenance and proximity.
4. `Claim` — a statement the project may eventually communicate in a paper, proposal, presentation, or decision.
5. `Decision` — a research action chosen under the current evidence state.

A hypothesis state and a claim state are not the same thing. A hypothesis can be strengthened without a manuscript-level mechanism claim becoming supportable.

## Hypothesis states

Allowed states:

- `active`
- `strengthened`
- `weakened`
- `rejected`
- `superseded`
- `unresolved`

Every state transition must record:

- previous state;
- new state;
- evidence that triggered the change;
- strongest surviving rival;
- whether a declared death condition was crossed;
- what future evidence could reverse the transition.

Do not use `strengthened` when the new result is equally compatible with the named rival.

## Claim states

Allowed states:

- `proposed` — a candidate statement worth testing, not yet evidence-qualified;
- `evidence-incomplete` — relevant evidence exists but the required evidential conditions are not yet satisfied;
- `supported-within-boundary` — the available evidence supports the exact bounded wording and named alternatives have been adequately addressed for that wording;
- `contradicted` — current evidence materially conflicts with the claim;
- `not-identifiable` — the current design or measurement cannot distinguish the claim from serious alternatives;
- `retired` — the claim should no longer drive design or communication unless new evidence reopens it.

Avoid generic `supported` without a boundary. Scientific support is always conditional on the system, measurement, design, and alternatives actually tested.

## Fail-closed anti-leakage rules

When a required evidential condition is missing, the claim must remain at or be downgraded to the strongest defensible state. Do not allow fluent prose to bypass the state constraint.

### Novelty

A claim using `novel`, `first`, `unexplored`, `unprecedented`, or an equivalent priority statement requires a dedicated prior-art search with a documented search boundary and nearest prior art.

Without that search, allowed wording is limited to forms such as:

- `not located within the documented search boundary`;
- `appears underrepresented in the searched literature`;
- `novelty remains unverified`.

### Mechanism

A claim using `demonstrates mechanism`, `is driven by`, `mediates`, `causes`, or an equivalent causal-mechanistic statement requires, when scientifically applicable:

- at least one named serious rival;
- a discriminating prediction that differs between the focal mechanism and that rival;
- evidence from a design or perturbation that can actually discriminate them;
- no triggered death condition;
- valid measurement of the claimed mediator or mechanistic state.

If these conditions are absent, keep the claim at `evidence-incomplete` or `not-identifiable` and downgrade wording to association, consistency, or plausibility as appropriate.

### Causality

Association, temporal ordering, feature importance, correlation, ordination, enrichment, or predictive accuracy alone cannot upgrade a causal claim.

### Proxy and construct

A proxy cannot be written as the underlying construct unless validation or a justified measurement model supports the mapping.

### Performance and mechanism

A performance gain cannot, by itself, upgrade a mechanistic claim. A simpler baseline that reproduces the gain is a death condition for necessity-based innovation claims.

### Evidence proximity

Evidence graded `C`, `D`, or `E` cannot be narrated as if it were project-level direct evidence. Source prestige does not change evidence proximity.

### Missing evidence

Empty direct-evidence fields must remain explicitly empty. Do not fill them with adjacent-system papers, narrative plausibility, or target-journal precedent.

## Claim upgrade checklist

Before upgrading a central claim to `supported-within-boundary`, check:

1. Is the exact claim operationally defined?
2. Is the system boundary explicit?
3. Are the strongest relevant baseline and rival visible?
4. Are the supporting observations direct enough for this wording?
5. Does the design distinguish the focal explanation from the serious rival?
6. Are measurement validity and calibration adequate?
7. Have known confounders, batch effects, transport limitations, and simpler explanations been addressed when relevant?
8. Has a death condition been declared and not crossed?
9. Is uncertainty represented in the wording?
10. Would a skeptical expert agree that the wording is no stronger than the design?

If any required answer is `no`, do not upgrade.

## Claim wording control

For central claims, maintain three fields when useful:

- `allowed_wording_current`
- `forbidden_wording_current`
- `upgrade_requirements`

This is especially useful when drafting manuscripts or proposals from an evolving research state.

## Project isolation

Every hypothesis, claim, evidence item, experiment, and decision must belong to a declared project or research-state identifier when multiple projects are active.

Do not import an active hypothesis or claim from another project merely because the material, organism, method, or application looks similar. Cross-project information may enter only as literature/background evidence with an explicit distance label unless the user intentionally merges the projects.

## Historical integrity

Never delete a rejected or superseded central hypothesis merely to simplify the story. Preserve the dated transition and reason for rejection. Historical records are for audit and learning; only the current active state should drive new design.
