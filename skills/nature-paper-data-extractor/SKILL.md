---
name: nature-paper-data-extractor
description: >-
  Extract structured, auditable data from academic papers for evidence synthesis, meta-analysis,
  machine learning, and reproducible research databases. Use when the user asks to batch-extract
  experimental design, treatment arms, outcomes, units, sample sizes, uncertainty, source locations,
  tables, supplementary data, or figure-derived values from papers/PDFs. Route figure/chart
  digitization to nature-figure-data-extractor rather than silently estimating values from plots.
metadata:
  author: nature-skills adaptation
  version: 0.1.0
---

# Nature Paper Data Extractor

## Purpose

Build a research-grade paper-to-database pipeline. The goal is not merely to "read papers" but to
produce structured records that remain traceable to the source and are safe for later meta-analysis
or machine-learning use.

This skill was independently adapted for `nature-skills` after reviewing the MIT-licensed
`GeederX/paper-data-extraction-skill` architecture and the batch-reading / explicit-missing-field
principles in K-Dense scientific-agent skills. Do not assume external tools or APIs are available;
use the current agent's PDF, file, Python, or local tooling when possible.

## Core rule: schema first

Before extracting many papers, define the extraction schema. At minimum distinguish:

- `paper_id` / DOI / bibliographic metadata
- `experiment_id`
- `arm_id`
- treatment and comparator identity
- sample size / replicate count when reported
- outcome name, value, unit, basis and time point
- uncertainty type and value (`SD`, `SE`, `CI`, range, not reported)
- source type (`text`, `table`, `supplement`, `figure`)
- source locator (page, section, table/figure/panel, supplementary file)
- extraction status and QA status

Never allow the schema to collapse paper, experiment and arm into one row identity when the source
contains multiple experiments or treatments.

## Evidence hierarchy

For a numeric field, prefer evidence in this order:

1. supplementary/source-data table;
2. main-text table;
3. explicit numeric statement in Results/Methods;
4. author-provided calculation or clearly reconstructable value;
5. figure digitization through `nature-figure-data-extractor`;
6. unresolved.

Do not digitize a plot when an exact table value exists.

## Missingness contract

Every requested field must end in one explicit state:

- `AVAILABLE`
- `TRUE_NOT_REPORTED`
- `SOURCE_UNAVAILABLE`
- `EXTRACTION_GAP`
- `AMBIGUOUS`
- `NOT_APPLICABLE`
- `FIGURE_DIGITIZATION_REQUIRED`

Do not use blank cells to mean all of these states.

## Extraction workflow

### 1. Freeze the research question and estimand

Define what the downstream analysis is trying to estimate before extraction. Examples:

- final total nitrogen loss / initial nitrogen;
- treatment minus control change in percentage points;
- response ratio;
- biomass yield;
- pollutant removal efficiency.

Do not mix outcomes that merely share similar labels but use different denominators or time windows.

### 2. Pilot the schema

Test the schema on 3-5 heterogeneous papers before batch extraction. Record fields that repeatedly
become ambiguous and revise the schema before scaling up.

### 3. Screen each paper

Assign one screening decision:

- `INCLUDE`
- `EXCLUDE`
- `DUPLICATE`
- `PENDING_SOURCE`

Store a short reason. Screening decisions must be auditable and reversible.

### 4. Parse study structure before values

Identify:

`paper -> experiment -> arm -> time point / measurement`

before extracting outcomes. A paper with 6 arms is still one paper for study-level independence.
Repeated time points are repeated measurements, not independent studies.

### 5. Extract exact values first

Extract tables, supplementary tables and explicit textual values before looking at figures. Preserve:

- original value;
- original unit;
- original basis;
- normalized value, only when conversion is justified;
- conversion formula and assumptions.

Never overwrite the original value with the normalized value.

### 6. Route chart-only values

If the requested value appears only in a chart, create a digitization task containing:

- paper_id
- figure_id
- panel
- page
- chart type
- target series
- x/y labels and units
- whether error bars are required
- whether axes are linear/log/dual/unknown

Then invoke `nature-figure-data-extractor`.

### 7. Source-grounded reconciliation

For high-value fields, run an independent second pass or reviewer pass. Reconcile disagreements
against the source, not by averaging two extractions.

Recommended status:

- `PASS_EXACT`
- `PASS_RECONSTRUCTED`
- `PASS_DIGITIZED`
- `PASS_WITH_WARNING`
- `FAIL`

### 8. Export analysis-ready tables

Keep at least three layers:

- `raw_extraction`: source-faithful values;
- `normalized_dataset`: converted and harmonized values;
- `qa_ledger`: provenance, warnings and decisions.

Never let downstream modeling read directly from the raw layer without the harmonization rules.

## Meta-analysis / ML safeguards

- Independent sample count is based on studies/papers as defined by design, not row count.
- Shared controls and repeated outcomes must remain identifiable.
- Do not treat missing SD/SE as zero uncertainty.
- Do not infer sample size from the number of plotted points unless the paper explicitly defines it.
- Do not convert partial pathway losses into total loss unless the mass balance is complete and valid.
- Preserve author-reported and recalculated outcomes as separate fields.
- Record measured, calculated and setpoint values as different semantic classes.

## Output contract

For each extraction run return:

1. papers screened / included / excluded / pending;
2. number of experiments and arms;
3. requested-field coverage by paper and arm;
4. exact/table/text/figure-derived counts;
5. unresolved fields and reasons;
6. duplicate and identifier QA;
7. a machine-readable dataset;
8. a provenance / QA ledger.

## Red lines

Never invent a value, SD, sample size, unit, treatment mapping, figure series identity or source page.
Never claim chart-derived numbers are author-reported exact values. Never use abstract-only evidence
for a field that requires full-text methods/results unless the user explicitly accepts that limitation.
