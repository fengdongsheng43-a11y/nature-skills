# Sources and design notes

This skill is an independent adaptation for `nature-skills`; it is not a verbatim copy of another repository.

Design references reviewed during development:

1. `GeederX/paper-data-extraction-skill` — MIT License. Useful architectural ideas include schema-first extraction, PDF-to-markdown preprocessing, explicit screening state, structured CSV output, and validation.
   - Repository: https://github.com/GeederX/paper-data-extraction-skill
   - License: MIT

2. `K-Dense-AI/scientific-agent-skills` — reviewed for explicit missing-field handling, source-grounded paper reading, batch extraction, and scientific-agent workflow patterns. Individual skills may carry their own licenses; no code or long-form text from those skills is bundled here.
   - Repository: https://github.com/K-Dense-AI/scientific-agent-skills

The `nature-paper-data-extractor` workflow adds domain-independent evidence states, paper/experiment/arm identity, source hierarchy, figure-digitization routing, meta-analysis/ML safeguards, and provenance/QA requirements developed from research data-extraction use cases.
