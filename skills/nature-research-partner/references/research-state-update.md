# Research state update

## Purpose

Maintain one current research state while preserving the history of why earlier ideas were changed or rejected.

## State files

Recommended current records:

- `PROJECT_CONTEXT.md`
- `RESEARCH_CONTRACT.md`
- `LITERATURE_COORDINATE.md`
- `HYPOTHESIS_LEDGER.md`
- `EVIDENCE_LEDGER.md`
- `DECISION_LOG.md`
- `MASTER_FRAMEWORK.md`

## Update protocol

When new data or literature arrive:

1. Freeze the new observation without interpretation.
2. Record provenance, date, sample, method, units, uncertainty, exclusions, and preprocessing when available.
3. Map the observation to predictions already recorded before seeing the result.
4. Add plausible post-hoc interpretations separately and label them exploratory.
5. Compare the result against named rivals.
6. Update evidence proximity and claim status.
7. Update the decision only after documenting the strongest counterargument.
8. Record the next action and what uncertainty it is intended to reduce.

## Hypothesis states

Use:

- `active`
- `strengthened`
- `weakened`
- `rejected`
- `superseded`
- `unresolved`

Do not delete old states. Add a dated transition and the evidence that caused it.

## Decision record

Every major decision should contain:

- decision;
- date;
- current evidence;
- strongest counterargument;
- remaining uncertainty;
- reason for the chosen route;
- what future result would reverse the decision.

## Belief updating without fake Bayesianism

Bayesian language is useful when priors, likelihoods, and evidence models are explicit. Do not fabricate posterior probabilities merely to look quantitative.

When formal Bayesian updating is not justified, use directional updates tied to predictions: `strengthened`, `weakened`, `unchanged`, or `unresolved`.

## Project hygiene

Only the current active state should drive new design. Historical ideas may be reconsidered only when new evidence or constraints materially change the reason they were previously rejected.
