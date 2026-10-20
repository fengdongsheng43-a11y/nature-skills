---
name: nature-journal-trends
description: >-
  Evidence-grounded analysis of the last three years of leading journal research
  topics, topic evolution, actual publishing patterns, journal-specific
  contribution and evidence standards, rival-journal differences, and
  scientifically tractable opportunities. Use for 顶刊热点, 期刊偏好, 研究趋势,
  最近三年发文, journal landscape, publication trend, journal positioning,
  journal comparison, evidence-standard shifts, or research-frontier scouting.
  This is a journal-intelligence and bibliometric execution layer governed by
  the user's nature-research-partner scientific decision framework.
---

# Nature Journal Trends — Journal Evidence & Frontier Intelligence

## 0. Scientific ownership and source of truth

This skill is a specialized execution/analysis layer, NOT a replacement for
nature-research-partner. At the start of consequential work, load the **current**
scientific decision framework from:

- Repository: fengdongsheng43-a11y/nature-skills
- Branch: main
- File: skills/nature-research-partner/SKILL.md

Do not substitute the upstream Yuan1z0825/nature-skills repository, infer that
the fork file is absent from an upstream 404, or fall back to remembered rules
while describing them as freshly checked. Read the parent skill's conditional
references when central mechanisms, novelty, scientific claims or research state
transitions are being evaluated. If access fails, report the exact failure;
proceed only with a bounded, explicitly provisional analysis.

Primary question: **What has the journal actually published, how has that
changed, what level of scientific contribution and evidence did the published
studies demonstrate, and which unresolved problems might justify new research?**

Do not optimize for a popular-looking topic. Optimize for accurate decisions.

## 1. Non-negotiable distinctions

1. **Publication mix ≠ editorial preference ≠ acceptance probability.**
   A journal's published corpus is selected output. Without submission and
   rejection denominators or editorial evidence, never infer acceptance odds.
2. **Popularity ≠ novelty ≠ scientific value.** Keyword or citation frequency
   does not demonstrate mechanistic innovation or a research gap.
3. **Publisher scope ≠ observed publishing mix.** Keep official scope,
   published corpus, editorial statements, and speculative inference separate.
4. **Published study ≠ study quality.** Publication is a selection filter, not
   proof that every claim or mechanism was established.
5. **Full-text verification ≠ abstract-only ≠ metadata-only.**
   Claim only what inspected material can establish.
6. **Recent ≠ most influential.** Citation delay and incomplete years heavily
   bias emerging-topic judgments.
7. **Cross-journal comparison requires comparable denominators.** Do not
   conflate journal size, document type, date coverage, special collections,
   indexing lag, or topic-tagging rules.
8. **No fabricated records, DOIs, metrics, acceptance/rejection rates, editor
   intentions, exact sample counts, impact factors, or journal requirements.**
9. **Trend evidence does not establish a mechanism.** A hypothesis about why a
   topic grew needs serious rival explanations and falsifying observations.
10. **Claim controls are fail-closed.** If corpus integrity, access or
    comparison validity fails, downgrade instead of compensating with narrative.
11. No invented numerical "hotness", "novelty" or journal-fit scores. A score
    is allowed only with a justified, preregistered definition and validation.
12. Never mix projects' state, evidence or hypotheses. Cross-project transfer
    requires an explicit labeled analogy or deliberate user-approved merge.

## 2. Working modes

Select the lightest mode adequate to the decision; do not demand a full census
for one navigational question.

| Mode | When | Default output |
|---|---|---|
| radar | Fast discovery of plausible developments in named journals/field | Bounded recent-paper evidence brief; provisional signals; what must be checked |
| profile | One journal's 3-year topic/evidence/format profile | Reproducible corpus + topics + contribution/evidence shifts |
| compare | Two or more journals, or adjacent journals as controls | Matched journal-by-year comparisons and discriminating differences |
| frontier | Determine whether a particular apparent hotspot is worth entering | Parent skill literature gate, nearest prior art, counter-evidence, bottleneck and P0 test |
| update | New issue, new editorial policy, updated corpus, or prior error | Delta against frozen earlier version, claim-state transitions and reversals |

A radar built on sampled papers cannot report corpus-wide topic shares. A
frontier report cannot declare novelty just because a topic is rare.

## 3. Scope and time rules

Default temporal window: **rolling 36 months ending at retrieval date**.
Also produce calendar-year summaries when coverage supports them; label
incomplete current years and use matched year-to-date comparison windows.
Never compare a 10-month current year directly to 12-month historical years
without stating/correcting the exposure difference.

Define exact journals with ISSN and publisher; distinguish parent/sister
journals. Define the unit: indexed article/work, not search hit or PDF copy.
Default primary inference corpus: original research articles. Treat reviews,
perspectives, editorials, corrections, news, protocols, and special collections
as separately reported strata. State whether online-first or issue date is
used; deduplicate DOI / work-version identities. If user requests another
universe, record and apply it consistently.

Avoid an impact-factor-only inclusion rule. Journal selection must be
transparent and appropriate to field and question.

## 4. Workflow

### Stage A — Freeze question and corpus passport

State journals, topic ontology, time window, retrieval timestamp, document
types, sources, access, reference journal(s), target decision and limitations.
Freeze search queries and inclusion/exclusion criteria BEFORE describing
frequencies. Read references/corpus-and-sampling.md.

### Stage B — Retrieve and audit actual publication records

Use publisher site and available verified scholarly sources such as OpenAlex,
Crossref, Web of Science or Scopus according to access. Reconcile ISSN,
journal title, DOI, online publication date, article type, special issue and
duplicates. Keep source-specific coverage; missing data are visible.
Use nature-academic-search for discovery or bibliographic verification when
available; do not claim that a GitHub SKILL by itself retrieves data.

Stop quantitative inference for serious unmeasured coverage or type bias.
A useful partial qualitative report is still permissible with a boundary.

### Stage C — Measure topic and contribution patterns

Create reproducible topic taxonomy with multi-label assignment where needed.
Separate scientific problem, target system, mechanism, method, application,
study type, and evidence maturity. Keywords are weak proxies: validate labels
against titles/abstracts and sampled full texts. Report both raw counts and
journal/year-normalized shares with explicit denominators. Read
references/temporal-and-journal-inference.md.

Where data support it, use title/abstract embeddings or bibliometrix to
support classification; never treat unsupervised cluster names as ground truth.
Blind/double coding and ambiguity audits should be used for consequential
comparisons. Report unknown/unclassified share.

### Stage D — Identify trend signals without hype

Check within-journal changes, matched-calendar-period change, prevalence
relative to relevant comparator journals, and persistence across windows.
Examine sensitivity to vocabulary, multi-label versus exclusive labels,
reviews/special issues, online-versus-issue dating and missing records.

Categorize as: persistent growth, emerging candidate, stable/core,
possibly saturated, declining candidate, or indeterminate; attach evidence
and uncertainty. "Saturated" requires nearest-prior-art density and
contribution-overlap examination, NOT high publication count alone.
"Emerging/declining" quadrants of thematic maps are descriptive constructs,
not automatically time-series proof.

### Stage E — Journal-specific publishing signals

Three distinct evidence streams:

- OFFICIAL: verified current Aims & Scope, article types, editorial comments,
  author/reviewer guidelines (date and live URL).
- OBSERVED: verified published papers, study architectures, required-looking
  evidence patterns, title/abstract conventions and contribution classes.
- REJECTION: only supported official policies, editorials, or well-labeled
  weak anecdotal signals; avoid treating survivor samples as reject data.

Compare the target journal to at least one relevant rival when asserting a
**journal-specific** preference; use the same time/discipline/format strata.
Test a proposed signal on held-out in-journal and out-of-journal examples.
Never invent a desk-reject threshold. Read
references/journal-preference-and-evidence-bar.md.

### Stage F — Frontier and gap audit (mandatory for research decisions)

Invoke parent nature-research-partner literature-evidence gate:

1. Landscape;
2. nearest prior art / SOTA;
3. mechanism + method-evidence standard;
4. counter-evidence / failure / boundary condition;
5. publication-level anchor.

Map recurring, unresolved, important and tractable bottlenecks across
**independent** studies. Generate serious rival hypotheses, discriminating
predictions, death conditions, and smallest P0 decisive tests. Adjacent-system
evidence remains adjacent. Do not infer "unexplored" from zero hits.

### Stage G — Decision and communication

Every consequential signal/claim records provenance, journal/date/source
boundary, access level, denominator when quantitative, competing explanation,
allowed wording, forbidden upgrade, confidence basis and reversal condition.
Prioritize possible research actions by decisive testability and project
constraints rather than a cosmetic weighted score.

Use templates/journal-trend-report.md to report:

- what changed, measured how, in what corpus;
- how the target differs from rival journal(s);
- what evidence rigor actually supports;
- what remains unresolved, not merely underrepresented;
- which P0 observation/test could disprove the opportunity;
- what evidence would change the recommendation.

### Stage H — Update and retain state

For repeat analyses, preserve frozen prior corpus/query version, corrections,
changed assignments, journal policy changes, new articles and changed claims.
Distinguish genuine shift from data refresh, lag and revised classification.
When central scientific claims change, apply the parent's claim-state machine.

## 5. Minimum evidence and claim gates

| Intended conclusion | Minimum supporting evidence | If missing |
|---|---|---|
| "These papers were published" | DOI/publisher or authoritative identifier + verified journal/date/type | unverified candidate |
| "Topic X rose within journal" | audited corpus, consistent labels, time-aligned denominators and sensitivity | possible signal in inspected sample |
| "Journal A publishes more X than B" | matched journal/year/document-type corpus and classification | unadjusted observed difference only |
| "Journal A prefers X" | observed differential **plus** editorial evidence where obtainable, or label as limited inferred signal | observed publishing mix, NOT editorial intent |
| "Evidence standard shifted" | comparable full-text studies across time + explicit claim-to-evidence coding | hypothesis, not established journal requirement |
| "Topic X is saturated" | dense nearest prior art + little defensible remaining problem in a bounded search | high publication activity only |
| "X is a novel gap" | dedicated multi-family prior-art search, independent recurrence and counter-evidence audit | candidate underexplored question |
| "X should become our project" | parent-skill bottleneck audit, serious rivals, death condition and feasible P0 | conditional watchlist |

For any missing record or evidence role use UNKNOWN / NOT FOUND, not a plausible
substitute. Explicitly disclose access status and search boundaries.

## 6. Delegation and tool boundary

- Parent nature-research-partner: scientific contradictions, strongest
  baselines, causal claims, rivals, P0 prioritization, hypothesis/claim states.
- Nature-academic-search: multi-source discovery, verified records and DOI QA.
- Nature-literature-pipeline: incremental monitoring and deduplicated archive.
- Nature-paper-card / nature-reader: full-text evidence-chain extraction.
- bibliometrix / bibliometric tools: implementation, plots, science mapping.
- This skill: corpus definitions, longitudinal and journal comparisons,
  interpretation boundaries, editorial-signal discrimination, report decision.
- None of these are presumed installed simply because a GitHub path exists.
  If a tool cannot run, use a transparent manual/fallback workflow.

When using third-party methods, respect their license and avoid asserting
their heuristics have been validated for environmental journals.

## 7. Built-in QA before releasing a trend judgment

1. Was the retrieval date and search boundary recorded?
2. Is the primary unit a unique paper? Are DOI/early-online duplicates handled?
3. Are corpus coverage, exclusions and article types audited?
4. Are incomplete years compared fairly?
5. Is each quantitative claim reproducible from counts and denominators?
6. Are topic labels stable under plausible alternative classification?
7. Are original research, reviews and special issues separated?
8. Are publication-mix results separated from editor preference/acceptance?
9. Is a claimed journal-specific trait different from a relevant rival?
10. Are important studies inspected beyond metadata where necessary?
11. Are negative examples, counterevidence and rival interpretations visible?
12. Did an alleged research gap survive parent-skill five-pass search?
13. Does any proposed project expose a death condition and P0 test?
14. Did we avoid invented citation statistics, IF values and fabricated trends?
15. Would new evidence cause a stated decision change?

If a required item fails, state the failing gate and release only the bounded
portion of the answer.

## 8. Related references

- references/corpus-and-sampling.md — source identity, time windows and corpus QA.
- references/temporal-and-journal-inference.md — indicators, trend inference, robustness.
- references/journal-preference-and-evidence-bar.md — journal signals, rival tests, evidence maturity.
- templates/journal-trend-report.md — reproducible output and claim ledger.

Version: 0.1.0 (research design specification; not yet benchmarked on a live journal corpus).
