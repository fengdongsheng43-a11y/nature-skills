# Corpus and sampling contract

## Purpose

Give journal-trend claims a reproducible denominator. This file is loaded for
profile, compare, frontier (when frequencies are discussed), and full updates.
The corpus is not a convenience list of papers found through ranked web search.

## A. Corpus passport (freeze before counting)

Record at least:

- Analysis ID, analyst, retrieval time and timezone;
- focal journal(s), publisher, ISSN/eISSN and journal identity notes;
- research question and intended inference (description / trend / comparison);
- rolling-window start and end date; calendar-year and matched-YTD design;
- chosen date field: published-online, published-print or issue/volume date;
- data sources, precise API/query/export, access and retrieval log;
- indexed fields available: title, abstract, DOI, publication dates, article
  type, issue/collection tags, keywords, references, affiliations;
- inclusion/exclusion criteria and how ambiguous article types are handled;
- article identity/dedup method and unresolved collisions;
- missing DOI, abstract, type and date counts;
- data coverage limits, known index lag, inaccessible paywalled material;
- frozen data version, code/version and provenance of manual corrections.

A single database query does not ensure coverage. Cross-check publisher issue
lists and unique DOI coverage, especially online-first publications.

## B. Correct unit and boundaries

Preferred unit is a distinct publisher-recognized scholarly work/article.
A DOI, repository preprint, author accepted manuscript, online-first record
and final issue record referring to the same work are not independent outputs.

Preserve raw records, then build a canonical paper table with:

    work_id
    doi
    source_ids
    journal_title
    issn
    publisher
    title
    abstract
    publication_date_selected
    date_type
    publication_year
    article_type_raw
    article_type_normalized
    special_issue_flag
    special_issue_label
    original_research_flag
    access_status
    retrieval_source
    retrieval_timestamp
    duplicate_family
    inclusion_status
    exclusion_reason

If metadata are missing, leave explicit UNKNOWN. Never infer article type or
journal based on arbitrary title keywords alone when a publisher source can
clarify it.

## C. Time-window protocol

Default rolling 36-month window ending at the retrieval date. To evaluate
journal annual trends also construct:

1. full completed calendar years, each Jan 1–Dec 31;
2. current year Jan 1–retrieval date explicitly marked partial;
3. historical matched year-to-date periods, same calendar cutoff;
4. a sensitivity view excluding recent months susceptible to indexing lag,
   if evidence indicates delayed coverage.

Keep one consistent primary date; inspect how results change under the
alternate online vs issue date where meaningful. Record selection before
seeing the desired trend. Never mix dates silently.

If comparing rates (papers per month), note varying month/day lengths and
late-indexing risk. Raw year-to-date growth alone is not evidence of editorial
shift.

## D. Articles and exclusions

For the primary profile:

- Primary: research article and empirically original article equivalents;
- Separate: reviews, perspectives, methods papers if distinct, editorials,
  opinion, commentary, news, book review, correction, retraction;
- Separate or flag: special issues, themed collections, invited articles;
- Keep: negative-result and replication papers if within the chosen article
  class; do not privilege fashionable or highly cited titles.

Do not collapse an interdisciplinary article's multiple themes into a single
journal identity without documenting the assignment rule.

## E. Census vs samples

**Census**: a defensible near-complete list of eligible works for the
specified journal and period, with a coverage audit. Counts and proportions
describe that corpus directly; their major uncertainty arises from coverage,
classification and boundary assumptions, not arbitrary sampling error.

**Probability sample**: inclusion design and sampling weights are documented;
sampling uncertainty must be reported where used.

**Purposive or convenience sample**: useful for qualitative signal discovery,
NOT for quantitative topic prevalence, journal-wide claims or editor preference.
Call findings "within the inspected papers".

**Rapid radar**: identify and inspect concrete papers with DOI/source links;
it is not a census and MUST NOT be represented as one.

For full-text mechanism/evidence coding, stratified sampling should cover
journal, year, article type, topic and contribution category when they are
decision relevant. Declare selection procedure and missing-full-text bias.
Do not impose one universal minimum sample size: adequacy depends on study
heterogeneity, magnitude, rarity, certainty requested and data coverage.

## F. Coverage and dedup checks

- Verify ISSN and journal identity, especially renamed or sibling journals.
- Reconcile source counts and inspect discrepancies with publisher listings.
- Deduplicate DOI case-insensitively; normalize prefixes/URLs.
- For no-DOI records, compare title, authors, date, volume and publisher link;
  preserve ambiguous records for manual review.
- Remove corrected records from title-topic counts only under stated policy;
  retain correction/retraction flags to audit claim quality.
- Calculate source coverage and missingness by journal/year/document type,
  not as one pooled percentage.
- Maintain raw-to-canonical record mapping and exclusion reasons.
- Record special-issue composition by year; do not assume thematic collections
  express permanent preference.
- Avoid merging Web of Science/Scopus/OpenAlex counts as additive counts.
  Resolve work-level overlap first.

## G. Stop gates

- STOP_CORPUS: no reproducible search boundary, article identity or period.
- STOP_COVERAGE: missing/indexed content plausibly reverses the target trend.
- STOP_TIME: incomplete years compared with non-matched full years.
- STOP_SAMPLE: convenience sample used to claim prevalence/percentage.
- STOP_ACCESS: required full-text evidence is not actually accessible.

A STOP does not prevent a useful exploratory brief. It blocks the particular
quantitative or causal claim whose gate failed.

## H. Source and reproducibility manifest

Deliver a readable table and machine-readable data when possible:

- source/provider, query, scope, retrieval time and coverage;
- imported count, excluded count, duplicate count, unique eligible count;
- unique paper IDs/DOIs and unresolved identification cases;
- dataset hash or immutable snapshot identifier;
- coder/model names, classification rules, version and review status;
- public/private access limits and lawful usage boundaries.

Every denominator in the report must be computable from the frozen
canonical table and its explicit filters.