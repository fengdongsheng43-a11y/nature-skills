# Technology-to-scientific-contradiction reconstruction

## Purpose and trigger

Use this protocol when a researcher presents several techniques, devices, additives, pretreatments, optimization recipes, or practical failures and asks **what scientific contradiction or unresolved bottleneck they reveal**.

This is a discovery aid, not a novelty engine. Multiple technologies having drawbacks does **not** establish a shared causal bottleneck, tradeoff, field gap, or new mechanism. The output initially has `candidate contradiction` status, not `established unresolved bottleneck`.

Integrate with:
- `formalization-and-problem-reconstruction.md` for system boundaries, variables, inferential units;
- `literature-coordinate-system.md` and the five-pass literature gate for prior art;
- `unresolved-problem-reconstruction.md` for `Recurring ∩ Unresolved ∩ Important ∩ Tractable`;
- `mechanism-and-rival-reasoning.md` for serious rivals;
- `evidence-architecture-and-experiment-priority.md` for P0 experiments;
- `research-state-machine-and-anti-leakage.md` for hypothesis/claim state control.

## A. Start with the real-world job, not a preferred material

Freeze:
1. **System boundary:** target matrix/organism/process, location or source, operating conditions and timeframe; distinguish different process stages and sample types.
2. **Primary job:** what useful function or outcome must be achieved, in what units and time window?
3. **Non-negotiable constraints:** safety, resource recovery, cost, material lifetime, energy/water, performance, sample and instrumentation availability.
4. **Evidence state:** direct measurements, reported literature results, project ideas and unknowns. Mark unmeasured fields `UNKNOWN`.
5. **Best existing method:** the strongest credible comparator under comparable operating conditions, not a weak blank control.

Ask first whether the problem is merely a poor implementation, a noncompetitive device, or an actual unresolved process limitation.

## B. Reverse-engineer each technique

For every credible incumbent and proposed technique, fill a compact technology ledger:

| Field | Test question |
|---|---|
| Target failure | What observed/established condition motivates the technique? |
| Intervention | What physical, chemical, biological or operational variable does it actually change? |
| Intended effect | What function or outcome should improve, and by what plausible chain? |
| Displaced constraint | What new limitation or resource burden could it introduce? |
| Rival explanation | Could the claimed benefit arise from a simpler variable or measurement artifact? |
| Best baseline | What established technique could produce the same effect? |
| Direct measurements | What measurements verify target-variable change, not just an endpoint proxy? |
| Failure/death test | What result would show the technique is unnecessary or ineffective? |

Separate `documented effect`, `known principle applied to the system`, and `speculated consequence` per row. Do not infer the actual direction of effects from technique names or ingredient properties.

## C. Abstract the functions; do not average together the technologies

Strip brand/device/additive names. Extract a minimal set of shared **functional requirements**, such as:
- useful input availability and delivery (light, nutrient, electron donor, reactive species);
- inhibitory exposure and chemical speciation;
- mass-transfer, kinetics, and interfacial accessibility;
- physical integrity, safe lifetime, recoverability;
- actual productive conversion/recovery rather than apparent concentration removal.

Represent outcomes separately. Examples: concentration removal `≠` conserved mass recovery; adsorbed/retained `≠` bioavailable; total metal `≠` isolated site `≠` catalytically accessible site.

If interventions target fundamentally different objectives or matrices, do **not** force a single common problem. Retain several bounded candidates or conclude `no useful common contradiction identified`.

## D. Map candidate couplings with evidence labels

For each pair of requirements, ask:
1. Can improving X worsen Y through a specified mechanism?
2. Does the effect depend on initial chemistry, flux, time, location, or control regime?
3. Is the tradeoff unavoidable, avoidable by a simple baseline, or only hypothesized?
4. Is a third variable jointly driving both effects?
5. Are the two quantities causally linked, or merely correlated because a technique changes both?

Write each link as:
`intervention → directly altered state → proposed mediator → measured outcome`.

Tag each arrow `measured here`, `direct prior art`, `adjacent principle`, or `hypothesis`. Identify feedback separately from simple two-way effects: feedback requires time-ordered mutual influence and an intervention showing the return path, not just two correlated responses.

Use conservation and speciation, equilibria, kinetics, transport and biological response as **competing** root-cause classes. Do not automatically assign every failure to an elaborate coupling.

## E. Form a *candidate* contradiction and attack it

Template:

> Under [bounded system], improving [functional requirement A] by [intervention] may impair [requirement B] through [specified mediator], so [decision-relevant outcome] could fail to improve despite [proxy or technical improvement]. The strongest alternative is [simple rival], and [test] can distinguish them.

State exactly which part is observed and which is proposed.

Run three adversarial checks:

1. **Necessity:** If the simplest established alternative solves the practical problem at comparable cost and operating conditions, is a new device or mechanism still necessary?
2. **Novelty:** Have independent studies already characterized the tradeoff or resolved it with an incumbent technology? Use the mandatory five-pass literature gate before any field-level claim.
3. **Identifiability:** Could the current design distinguish the claimed coupling from pH, temperature, batch, composition, mass-transfer, measurement, or other plausible changes caused by the intervention?

A system having multiple simultaneous limitations is not automatically evidence they interact.

## F. Distinguish five conclusion levels

1. **Technology disadvantage:** one option has a measurable drawback; no common scientific problem implied.
2. **Plausible functional tradeoff:** physics/chemistry suggests A may compete with B; no target-system demonstration.
3. **Observed conditional conflict:** appropriate matched experiments show A improves while B deteriorates or overall benefit collapses.
4. **Discriminated mechanism:** intervention/controls distinguish the proposed mediator from serious rivals, with valid direct measurements.
5. **Persistent cross-study unresolved bottleneck:** independent primary studies show recurrence; current SOTA does not adequately resolve it; solving it matters and is tractable.

Levels 1–4 do not automatically imply level 5. Label a proposed gap `candidate gap` unless `Recurring ∩ Unresolved ∩ Important ∩ Tractable` is supported within the documented search boundary.

A statistical interaction is evidence of effect modification under the design, **not** automatic proof of the hypothesized mediation mechanism.

## G. Choose a minimal discriminating test before inventing a material

Prioritize:
- **P0 measurement-validity check:** does the intervention change the *actual* limiting variable and is the response measured as intended?
- **P0 rival-separation:** manipulate the two candidate limits independently when possible (e.g. small factorial with matched composition and procedural controls); test the interaction against simple single-factor explanations.
- **P1 mediator and recovery test:** track time, space, mass balance/speciation; suppress or restore the proposed mediator where feasible.
- **P2 best-incumbent comparison and transfer:** compare with the strongest existing solution at matched scale, throughput and exposure; test on independent batches/sites if generality matters.

State independent experimental unit, replicates, controls, direct versus proxy measures, falsifying outcomes, nuisance factors, cost and decision rule.

If P0 shows only one ordinary factor limits performance, target that factor with the simplest feasible method. **Do not proceed to complex materials engineering solely because a device idea already exists.**

If a new material is justified, require a measurable increment versus an adequate simple baseline, including operating lifetime, regeneration, safety, total water/energy consumption and mass/resource recovery when relevant.

## H. Cross-site data and generalization gate

Multiple sites can expose heterogeneity but cannot by themselves identify causal limits or prove which intervention works.

- Keep raw manure wastewater, digestate, lagoon effluent and treated effluent in distinct strata unless comparable provenance is established.
- Validate units, sampling date/season, methods, dilution, detection limits and nested site/time replicates.
- A site-level snapshot of water quality is **not** an intervention-response dataset.
- Avoid machine learning with inflated effective sample size; for small site counts favor interpretable comparisons, uncertainty and purposive validation experiments.
- Define held-out site/batch tests before claiming transferable decision rules.
- Do not equate a water-quality cluster with a causal process class until intervention data support it.

## I. Explicit rival predictions and death conditions

For each central idea specify at least:
- preferred hypothesis and its discriminating prediction;
- strongest simple rival and what it predicts;
- a measurement-artifact or design-confounding rival;
- result that kills the coupling, the necessity of the new technique, or its alleged superiority;
- next research decision for positive, negative **and indeterminate** outcomes.

Maintain `Observation → Interpretation → Rival → Evidence grade → Hypothesis state → Claim state → Decision`; do not silently promote a teaching example into a verified project mechanism.

## J. Default response: Scientific contradiction card

When multiple solutions are supplied, return a concise structured result, not a long catalog:

1. **System and job:** target, constraints and current evidence/unknowns.
2. **Technique-to-constraint table:** incumbent/proposed methods, direct variables, side effects, strongest baseline.
3. **Candidate contradiction:** one bounded conditional statement with arrows labeled by evidence state.
4. **Serious rivals:** one simpler mechanism, one measurement/confounding alternative, and relevant counter-evidence.
5. **Literature/gap status:** documented five-pass search boundary and `Recurring ∩ Unresolved ∩ Important ∩ Tractable` verdict.
6. **Smallest P0:** matched intervention, measured mediator, outcome, negative pattern, decision rule.
7. **Decision:** keep, narrow, test, use simpler baseline, defer, or retire; permitted claim wording.

If the user asks how the inference was made, expose the steps and explicitly identify the first speculative arrow.

## K. Cross-domain illustrations (hypothetical, not project evidence)

- **Dark/high-ammonia wastewater + algae:** surface culture might increase photon delivery; photosynthetic carbon uptake might alter pH and NH3 exposure; diffusion barriers might also restrict nutrients. Test received light, pH/TAN/NH3 exposure and *assimilated* nitrogen independently. Prior art may already solve no-dilution cultivation; `no dilution` alone is not innovation.
- **P recovery:** strong mineral immobilization can reduce soluble losses and also reduce later accessible P. Separate initial mass retention, chemical form, and time-dependent biological availability; identify the specific condition where their relationship changes rather than restating the general tradeoff.
- **Bio-derived Fe single-atom catalysts:** total Fe capture can increase without increasing isolated or accessible sites. Compare the strongest chemical precursor baseline; distinguish living regulation, ligand chemistry, pyrolysis restructuring and catalytic leaching. Biological origin alone is not necessity or novelty.

These examples illustrate the reasoning **protocol**, not validated mechanisms or cross-project evidence.
