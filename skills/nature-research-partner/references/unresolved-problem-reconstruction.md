# Unresolved problem reconstruction

## Purpose

Turn literature retrieval into scientific problem discovery. The aim is not to collect statements that a topic is “underexplored,” but to identify problems that recur across independent studies, remain unresolved at the current search boundary, matter scientifically, and can be attacked by the present project.

## Three evidence levels

### 1. Author-stated gap
A single paper states a limitation, unknown, or future direction. Record it, but do not promote it to a field gap without independent convergence.

### 2. Cross-study recurring problem
Independent groups report the same unexplained phenomenon, performance limitation, contradictory result, or inability to control/predict an outcome. This is stronger than repeated wording in reviews.

### 3. Mechanistically persistent bottleneck
The recurring problem can be traced to a deeper obstacle such as non-identifiable mechanisms, coupled variables, missing measurements, unresolved thermodynamic-versus-kinetic control, scale dependence, hidden transport limitations, biological feedback, or an experimental design that cannot distinguish competing causes.

## Qualification rule

Use the intersection:

`G = R ∩ U ∩ I ∩ T`

- `R — Recurring`: more than one independent research group encounters the problem.
- `U — Unresolved`: the latest credible SOTA still lacks a robust solution or explanation within the documented search boundary.
- `I — Important`: solving it changes mechanism understanding, design rules, prediction, or a meaningful decision.
- `T — Tractable`: decisive tests are feasible with available or realistically accessible resources.

Do not manufacture numeric scores unless criteria are calibrated. Use structured judgments with evidence pointers.

## Search protocol

For each candidate problem, search in at least four directions when relevant:

1. direct target-system studies reporting the phenomenon or limitation;
2. recent SOTA studies claiming to solve or control it;
3. reviews/perspectives summarizing why it remains difficult;
4. contradictory or adjacent-system studies that may dissolve the apparent gap.

Prefer convergence across independent groups. Repeated papers from one group count as a research program, not independent confirmation.

## Root-cause decomposition

For each recurring problem, ask sequentially:

1. Is the apparent problem real, or a measurement/definition artifact?
2. Is it caused by thermodynamic feasibility or phase/speciation constraints?
3. Is equilibrium inaccessible because kinetics or nucleation barriers dominate?
4. Are mass transfer, diffusion, pore structure, or interface accessibility controlling?
5. Are multiple variables coupled so the effect is not identifiable?
6. Does biological regulation or feedback change the boundary conditions?
7. Does the field measure only endpoints when the missing information is pathway-resolved?
8. Is the obstacle principally scale, heterogeneity, cost, instrumentation, or reproducibility rather than mechanism?

Do not force this order when irrelevant; it is a fault-isolation scaffold.

## Problem card

Record:

- `Problem ID`
- `Recurring observation/failure`
- `Independent evidence`
- `Current SOTA / attempted solutions`
- `What remains unresolved`
- `Root-cause candidates`
- `Why previous approaches cannot resolve it`
- `Importance if solved`
- `Tractability for this project`
- `Candidate leverage point`
- `Death condition`
- `Status`

Allowed status:

- `established unresolved bottleneck`
- `probable unresolved problem`
- `candidate gap`
- `resolved / not a gap`
- `important but currently intractable`
- `low-value gap`

## Decision rule

A major project should normally be built around a problem that is both persistent and discriminable. Prefer a bottleneck where one or a small number of experiments can distinguish why prior work fails.

Do not select a problem simply because it can be published. Select it because resolving its uncertainty would change what the field should believe or do.
