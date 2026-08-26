# Literature evidence gate and five-anchor coordinate system

## Purpose

The literature stage is not a decorative review step. It is a decision gate between initial idea clarification and evidence-backed scientific reasoning. Once the question is searchable, external literature evidence must be collected before the partner strengthens a mechanism, novelty claim, SOTA claim, method claim, or publication-level plan.

## Why the gate comes after initial clarification

Searching the user's first wording can reproduce the user's initial anchoring bias. First clarify the observation, system boundary, scientific contradiction, likely baseline, and the statements that actually require external verification. Then build query families around those objects.

## Mandatory search triggers

Retrieval is required when the discussion depends on:

- current SOTA or research hotspots;
- novelty, prior art, or claims that a topic is underexplored;
- mechanism precedent or competing mechanisms;
- what a characterization or experiment can legitimately prove;
- known failure modes, null results, or boundary conditions;
- current target-journal evidence standards or comparable publication architecture.

If retrieval is unavailable, state the limitation and downgrade the claim. Do not substitute memory-based certainty.

## Query decomposition

Before searching, translate the reconstructed question into query families. Typical axes include:

1. target system or material;
2. mechanism or governing process;
3. strongest baseline or current solution family;
4. measurement or causal-evidence method;
5. failure mode, contradiction, or boundary condition;
6. adjacent field using the same mechanism under another name;
7. target publication level and evidence architecture.

Do not rely on one literal keyword string. Mechanisms often appear under different terminology across fields.

## Default five-pass retrieval

### Pass 1. Landscape

Establish vocabulary, major solution families, and broad field structure. Reviews are useful here for orientation, but they are not sufficient to establish novelty or a detailed mechanism.

### Pass 2. Nearest prior art and SOTA

Find the strongest current comparator and the closest existing work. Search similarity by mechanism, material, intervention, function, and application separately so that a renamed combination does not masquerade as novelty.

### Pass 3. Mechanism and evidence standard

Find the strongest direct evidence for the governing mechanism. Separately find how the field demonstrates that mechanism experimentally. A thematically similar paper may be a poor method-evidence anchor.

### Pass 4. Counter-evidence

Actively search for null results, contradictory mechanisms, failures, boundary conditions, scale dependence, batch effects, or alternative explanations. Do not wait for counter-evidence to appear accidentally.

### Pass 5. Publication anchor

Choose a paper whose scientific argument, evidence density, figure architecture, and target readership resemble the intended publication level. Do not choose it merely for language style.

## Anchor roles

### 1. Mechanism anchor

Find the strongest direct or foundational work supporting the governing mechanism or physical principle. Prefer direct measurement over narrative similarity.

### 2. SOTA anchor

Find the strongest current method, material, model, or intervention that solves the nearest version of the problem. This is the baseline the proposed work must beat, distinguish from, or explain.

### 3. Method-evidence anchor

Find a study that shows how the key mechanism or causal claim can actually be measured. This anchor often matters more than a thematically similar paper because it defines the evidence standard.

### 4. Counter-evidence anchor

Search for a conflicting result, failure case, boundary condition, null result, or competing mechanism. If no direct counter-evidence is located, document the search boundary and use an adjacent system only with an explicit distance label.

### 5. Publication anchor

Choose a paper whose scientific argument, evidence density, figure architecture, and target readership resemble the intended publication level.

## Evidence-distance labels

Use one of:

- `direct-target-system`
- `highly-similar-system`
- `adjacent-system`
- `method-only`
- `background-only`
- `not-found`

Do not allow an adjacent-system paper to silently become direct evidence.

## Access and verification status

For every candidate source, label the strongest level actually inspected:

- `full-text verified` — the relevant methods/results/discussion were inspected directly;
- `abstract-only` — only abstract-level claims are available;
- `metadata-only` — bibliographic existence is verified but substantive claims were not inspected.

Do not extract detailed numerical values, mechanistic chains, or experimental specifics from an abstract-only or metadata-only source unless those details are explicitly present at that level.

## Search record

For each anchor record:

- search date;
- database or search tool;
- query or query family;
- inclusion boundary;
- access/verification status;
- evidence-distance label;
- what the paper supports;
- what it cannot establish;
- why it occupies this anchor role.

## Literature Evidence Brief

Before returning to mechanism design, summarize:

1. the highest-information 3–5 anchors available;
2. strongest baseline and nearest prior art;
3. supported statements;
4. contradicted or weakened statements;
5. unresolved claims and missing anchors;
6. what changed relative to the user's initial idea;
7. the next 2–4 questions that are now worth discussing.

This brief is the default handoff back to the user in `explore` mode. The next discussion should react to evidence, not simply continue the pre-search story.

## When anchors are hard to find

A missing anchor is not a reason to stop the workflow. It is a research-state observation.

Possible interpretations include:

- the mechanism is under-measured;
- the nearest literature uses a different system boundary;
- the claim is too broad and needs decomposition;
- the field lacks a decisive measurement;
- the search strategy is incomplete.

Do not infer novelty from a missing anchor alone.
