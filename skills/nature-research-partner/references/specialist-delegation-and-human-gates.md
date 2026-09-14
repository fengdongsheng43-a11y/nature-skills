# Specialist delegation and human-gate protocol

## Purpose

Keep `nature-research-partner` as the scientific decision layer while routing execution to specialist skills without losing evidence boundaries, uncertainty, or project state.

The research partner owns `why`, `what`, `whether`, and `when`. Specialist skills own `how` within their technical domain.

## Delegation cycle

Use:

`Think → Delegate → Execute → Verify → Return structured evidence → Update research state → Decide`

A specialist result does not become a project conclusion until it returns to the research partner and is interpreted against the current hypotheses, rivals, evidence requirements, and decision rules.

## Delegation brief

Before routing a non-trivial task, define as many of the following as are relevant:

- `project_id`
- `task_id`
- `decision_or_claim_id`
- `scientific_question`
- `hypothesis_contrast`
- `requested_execution`
- `required_inputs`
- `required_outputs`
- `evidence_boundary`
- `must_not_infer`
- `validation_required`
- `return_to`

Do not ask a specialist to decide a scientific claim that belongs to the research partner.

## Specialist return contract

A non-trivial specialist task should return, when applicable:

- what was executed;
- source inputs and provenance;
- direct result;
- uncertainty or error information;
- assumptions checked;
- validation performed;
- which hypothesis or claim the result informs;
- what the result supports;
- what the result contradicts;
- what remains unresolved;
- important limitations;
- candidate evidence grade and why;
- decision impact, stated conservatively.

The research partner may revise the candidate evidence grade after comparing it with the full project context.

## Examples of ownership boundaries

### Literature

Research partner owns:

- which scientific uncertainty requires external evidence;
- query families and evidence roles;
- what would count as mechanism, SOTA, counter-evidence, or publication anchors.

`nature-academic-search` owns:

- search execution;
- metadata verification;
- source discovery;
- documented retrieval boundary.

`nature-reader` / `nature-paper-card` own:

- full-text or structured evidence extraction from located sources.

The research partner then decides what the literature changes.

### Statistics

Research partner owns:

- scientific claim;
- experimental unit;
- hypothesis contrast;
- what uncertainty matters;
- decision rule at the scientific level.

`nature-statistics` owns:

- statistical model/test selection once the inferential unit is clear;
- assumption checks;
- effect estimates and uncertainty;
- multiplicity and diagnostic handling;
- reporting of statistical limitations.

A p-value alone must never return as `mechanism supported`.

### Figures

Research partner owns:

- scientific message;
- claim represented;
- uncertainty and evidence boundary;
- relationships that must not be implied.

`nature-figure` or another figure specialist owns:

- chart/diagram form;
- layout;
- rendering;
- visual QA;
- export specifications.

An attractive figure must not upgrade the underlying evidence.

### Writing

Research partner owns:

- claim status;
- allowed strength of language;
- unresolved contradictions;
- paper-level evidence architecture.

Writing skills own:

- organization;
- wording;
- clarity;
- journal adaptation;
- prose QA.

Writing must not promote a claim beyond the current claim ledger.

## Human gates

Use human gates only for consequential research commitments. Do not turn routine analysis into an approval workflow.

### G0 — Research-direction commitment

Trigger when committing substantial project time/resources to one reconstructed scientific problem over competing directions.

### G1 — Major hypothesis commitment

Trigger when a preferred hypothesis will materially determine downstream design, expensive measurements, or project positioning.

This gate does not mean the hypothesis is assumed true; it means the project intentionally chooses to test it as a central candidate.

### G2 — High-cost or hard-to-reverse experiment

Trigger before experiments or analyses with substantial cost, scarce samples, destructive use of unique material, major outsourcing, safety implications, or strong downstream dependency.

### G3 — Central claim upgrade

Trigger when moving a central paper/project claim to a materially stronger semantic level, especially association → causation, plausibility → mechanism, or candidate novelty → priority claim.

### G4 — Abandon or pivot

Trigger before retiring a major research route when the decision would make substantial prior work inactive or redirect the project.

The record should state the strongest reason to continue as well as the reason to pivot.

### G5 — Publication-level claim freeze

Trigger when the core claims, evidence architecture, and intended publication positioning are being frozen for manuscript/proposal submission.

## Automatic work between gates

Read-only, reversible, low-cost reasoning and evidence gathering should proceed without unnecessary approval when the user's intent is clear.

Examples:

- searching literature;
- constructing rival hypotheses;
- checking mass balance;
- designing low-cost discriminating tests;
- calculating alternative statistical models;
- drafting provisional evidence tables;
- revising wording downward to match evidence.

## Gate record

For a consequential gate, record:

- gate ID;
- decision;
- alternatives considered;
- current evidence;
- strongest counterargument;
- remaining uncertainty;
- reversal condition;
- responsible project/state ID.

A gate records a decision under uncertainty; it does not convert uncertainty into truth.
