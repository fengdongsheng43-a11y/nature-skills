# Temporal trend inference and matched journal comparisons

## Operational definitions

Let N(j,t,k) be unique eligible articles assigned to theme k in journal j
and matched period t. Let N(j,t,all) be all unique eligible articles of the
same normalized document type and period. Multi-label theme assignment is
allowed, so summing N(j,t,k) across k may exceed N(j,t,all).

Topic share p(j,t,k) = N(j,t,k)/N(j,t,all), provided denominator > 0.
An absolute rise in N can coexist with a declining share when journal output
increases. Report both; distinguish share of journal and share within a field.

For journal-vs-field comparison, choose a relevant fixed reference universe
and a matched date, type, and topic assignment system. Avoid "all science"
as a baseline for specialized journals. Consider whether the journals publish
different numbers of issues, reviews or invited thematic collections.

## Minimum useful comparisons

1. **Within journal**: monthly/quarterly or matched-year-to-date counts and
   shares; do not fit more parameters than the observations support.
2. **Across journals**: same field, article types, time basis and topic labels.
3. **Within topic**: decomposition by contribution/problem/system/measurement
   to distinguish recycled keywords from new scientific mechanisms.
4. **Special-issue sensitivity**: with and without invited themed collections.
5. **Metadata sensitivity**: online vs issue dates, revised classifications,
   missing abstracts, early indexed vs fully resolved recent months.
6. **Type sensitivity**: original research alone vs research + review.

A 36-month window is useful for observing changes but often has low power
for multi-phase predictions. For long-term emergence/saturation, include a
longer background window when warranted, clearly separated from the main
three-year analysis.

## Quantities and uncertainty

Use descriptive contrasts first:
- unique eligible article count N per period;
- topic count, topic share and percentage-point difference;
- same-window rate per month when useful;
- class and journal baseline differences;
- underlying exact counts for small/rare categories;
- classification and corpus-missingness uncertainty.

If formal models are scientifically justified, predefine model family,
exposure, time smoothness, autocorrelation/overdispersion, journal effects,
and covariates. Don't turn three annual points into a confident forecast.
Bootstrap uncertainty does not repair unmeasured missing corpus coverage.
No formal p-values are required for descriptive census differences.

Citation-related analysis must specify citation database, retrieval date,
citation window, document type and field/year normalization. Citation counts
are attention signals and lag for newly published work. Do not call an
un-normalized 2026 citation count "low quality" or compare it directly with
2024 output.

## Topic labelling

Build explicit, revisable multi-axis labels:
- scientific challenge/question;
- study system/environment;
- intervention/process or material;
- hypothesized mechanism;
- method/evidence modality;
- contribution type: discovery, explanation, method, validation,
  synthesis, engineering deployment, policy/decision;
- evidence depth: description, association, perturbational causal,
  independent replication, scale-up/field validation (do not assume higher
  tier without full text).

Two parallel approaches are useful:
(A) a human-audited hierarchical taxonomy with term synonyms;
(B) exploratory topic model or embeddings as a sensitivity discovery layer.

Report ambiguous/UNKNOWN labels; code a sample independently where possible.
Check category prevalence robustness under different taxonomies and coding
decisions. A growing keyword can reflect newly fashionable terminology,
not a change in experimental substance.

## Trend labels and rival explanations

- **persistent growth**: direction robust across plausible windows and
  definitions, not one issue spike;
- **emerging candidate**: low historical base with verified newer studies,
  reproducible growth but insufficient evidence of persistence;
- **stable/core**: prominent presence without supported sustained shift;
- **declining candidate**: falling matched-period counts/shares robust to
  indexing and label changes;
- **possibly saturated**: high overlap of incremental contributions and
  strong comparable prior art; NOT merely a high paper count;
- **indeterminate**: data/sensitivity insufficient to distinguish patterns.

For every apparent increase consider:
1. journal expansion (total article volume) rather than thematic targeting;
2. invited special issue or guest-editor effect;
3. renaming/keyword substitution or model classification drift;
4. delayed indexing or early-online carryover;
5. database coverage change;
6. field-wide growth rather than journal-specific concentration;
7. interlinked research groups producing correlated sets of papers.

Present how each rival could falsify or weaken the original interpretation.

## Stronger claim thresholds

"Trend observed in this corpus": valid denominator and stable classification.
"Journal-specific shift": matched comparator journals and robustness.
"Editorial strategy changed": documented official editorial evidence or
explicitly marked inference; publication mix alone is insufficient.
"Future growth": prospective hypothesis with stated scenarios and
out-of-time validation; never an unqualified projection.
"Research opportunity": independent science-level novelty, mechanism,
counter-evidence, tractability and a decisive test from the parent skill.

Do not infer causal editorial motives from ecological publication data.
If evidence changes a recommendation, record the shift, source and reversal
conditions.
