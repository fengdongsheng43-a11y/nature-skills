# Formalization and problem reconstruction

## Purpose

Turn a vague research idea into a bounded scientific object without pretending that unknown variables are already known.

## 1. Freeze the starting statement

Write four lines before interpretation:

1. **Observed or proposed** — what was actually measured, noticed, read, or imagined.
2. **Source** — experiment, paper, figure, conversation, theory, anomaly, or intuition.
3. **Boundary** — material, organism, scale, environment, time, and conditions included.
4. **Decision** — what future choice would change if this question were answered.

If the starting point is a thought rather than an observation, label it `idea`, not `observation`.

## 2. Operationalize before optimizing

For each central term, ask whether it has an operational definition.

Examples:

- “better slow release” requires a time window, release metric, baseline, and acceptable total availability;
- “stronger mechanism” requires a specified causal chain and a measurement that can distinguish it from alternatives;
- “stable material” requires a timescale, environment, failure mode, and threshold.

Use `UNKNOWN` when the correct variable, threshold, or measurement is not yet established.

## 3. Classify the task

The project may contain more than one task type.

- **Optimization** — choose controllable variables to maximize or minimize a defined objective under constraints.
- **Causal** — estimate the effect of an intervention or exposure relative to a comparator.
- **Mechanistic** — distinguish processes that could generate the same observation.
- **Predictive** — forecast an outcome with declared generalization conditions.
- **Descriptive** — establish what exists, where, how much, or how it varies.

Do not allow an optimization layer to hide an unresolved mechanistic layer. A recipe can be optimized even when its mechanism is unknown, but the resulting paper cannot claim the unknown mechanism as demonstrated.

## 4. Mathematical object

When useful, represent the project as:

\[
\mathcal{R}=\{\Omega,X,Z,A,Y,M,H,\Theta,C,U,B,E\}.
\]

The point is not mathematical decoration. The representation forces the project to declare system boundary, controllable factors, nuisance variables, feasible interventions, responses, mechanisms, competing hypotheses, unknown parameters, constraints, uncertainty, baselines, and evidence requirements.

A valid formalization may contain many `UNKNOWN` entries.

## 5. Reconstruct the scientific contradiction

Ask questions that change the direction rather than questions that merely collect details.

Useful probes include:

- What observation contradicts the current expectation or baseline?
- Which variable would you remove first to see whether the phenomenon survives?
- Which current explanation is doing the most causal work in the story?
- What does the best existing method fail to control?
- Is the failure caused by thermodynamics, kinetics, transport, interface, biology, measurement, cost, or scale?
- If the preferred mechanism were false, what would still explain the observation?
- What answer would change the experiment or publication claim?

The result should be a one- or two-sentence scientific contradiction and a bounded question.

## 6. Avoid pseudo-formalization

Do not invent objective weights, priors, probabilities, thresholds, or scoring coefficients merely to make the problem look quantitative.

A symbolic relationship is useful when it clarifies dependencies. It is harmful when it hides the fact that the dependencies are unknown.
