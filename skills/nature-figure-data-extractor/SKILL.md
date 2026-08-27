---
name: nature-figure-data-extractor
description: >-
  Digitize quantitative data from scientific figures and charts into auditable tabular data.
  Use when the user asks to extract numeric values from line charts, scatter plots, bar charts,
  box/violin plots, heatmaps, contour plots, stacked charts, multi-panel figures, or figures embedded
  in PDFs for meta-analysis, machine learning, or evidence databases. Prioritize exact source tables
  when available; use figure digitization only when the plotted value is not otherwise reported.
metadata:
  author: nature-skills
  version: 0.1.0
---

# Nature Figure Data Extractor

## Purpose

Convert scientific figures into traceable numeric data without pretending digitized estimates are
exact author-reported values. This skill is designed for research evidence extraction, especially
when downstream analyses include meta-analysis or machine learning.

The workflow is inspired by established plot-digitization practice (e.g. calibrated WebPlotDigitizer-
style workflows) and by the provenance / explicit-missing principles used elsewhere in `nature-skills`.
It must remain tool-agnostic: use WebPlotDigitizer, Python image analysis, manual calibration, source
data, or another reliable digitizer when available.

## First decision: should the figure be digitized?

Before extracting pixels, search the paper package for the same value in:

1. supplementary/source-data tables;
2. main-text tables;
3. explicit Results text;
4. data repository / source-data file.

If exact values exist, use them and record `source_type=exact_source`. Do not digitize merely because
the figure is visually convenient.

Digitize only when the quantitative value is otherwise unavailable or when the user explicitly asks
to validate the plotted figure against reported numbers.

## Figure-task contract

Each digitization task must record:

- `paper_id`
- DOI if known
- `figure_id`
- `panel_id`
- PDF page
- chart type
- target series / group
- x variable and unit
- y variable and unit
- axis scale (`linear`, `log10`, `ln`, `category`, `unknown`)
- axis range and tick anchors
- whether dual y-axes are present
- whether error bars are required
- extraction method
- extractor / run ID
- QA status

Never start bulk digitization with an unidentified panel or ambiguous target series.

## Supported chart classes

### A. Cartesian line/scatter plots

Preferred for quantitative digitization.

Procedure:

1. crop the exact panel;
2. identify plot-area pixel bounds;
3. calibrate x and y axes from at least two trusted anchors per continuous axis;
4. verify linear/log transform;
5. isolate each requested series;
6. extract only visually supported points;
7. convert pixels to axis coordinates;
8. visually overlay extracted points back onto the source;
9. record calibration residual or spot-check error.

For a linear axis:

`x = x0 + (px-px0)*(x1-x0)/(px1-px0)`

For a log10 axis, calibrate and interpolate in log10(value) space, then back-transform.

### B. Bar charts

Extract bar top/bottom after calibrating the quantitative axis. Keep category labels separate from
numeric coordinates. For stacked bars, extract segment boundaries before computing segment height.

Do not infer error bars unless their cap/stem can be confidently distinguished from the bar.

### C. Error bars

When required, store separately:

- central estimate
- lower endpoint
- upper endpoint
- error type (`SD`, `SE`, `CI`, `unknown`)

A digitized error-bar length is not useful for meta-analysis unless the paper identifies the error type.
If error type is unknown, preserve it as `unknown`; do not convert it to SD.

### D. Box plots

Extract only statistics visually encoded and clearly defined by the caption/method:

- median
- Q1 / Q3
- whisker endpoints
- outliers, if required

Do not assume whiskers equal min/max or 1.5×IQR without source confirmation.

### E. Heatmaps

Heatmaps require a color-to-value calibration from a visible legend/colorbar. Extract cell values only
when:

- row/column identity is unambiguous;
- the colorbar has numeric anchors;
- the palette is not categorical;
- raster quality permits discrimination.

Record digitized heatmap values as approximate unless source data are available.

### F. Dual-axis charts

Treat left and right y-axes as separate calibration systems. Every series must be assigned to one axis.
If assignment is ambiguous, stop and mark `AMBIGUOUS_AXIS_ASSIGNMENT`.

### G. Multi-panel figures

Process each panel independently. Do not calibrate panel A and reuse coordinates for panel B unless
the panels have demonstrably identical plot-area geometry and axes.

## Extraction-grade system

Assign every digitized point or series one grade:

### D1 — calibrated high confidence

- axis anchors clear;
- series identity clear;
- plot resolution adequate;
- overlay QA passes.

### D2 — calibrated moderate confidence

- minor overlap / anti-aliasing / approximate anchor location;
- usable for sensitivity analysis with warning.

### D3 — weak digitization

- dense overlap, coarse raster, unclear axis, or ambiguous point center;
- exclude from primary quantitative synthesis unless manually verified.

### D4 — not digitizable

- no valid axis calibration;
- unreadable image;
- qualitative schematic;
- ambiguous series identity;
- transformed/decorative graphic without recoverable coordinates.

Never turn D3/D4 output into precise primary data merely to increase sample size.

## Calibration QA

A digitization is incomplete until at least one QA method is run:

1. **Overlay QA** — draw extracted pixel locations on the original panel;
2. **Anchor back-check** — transformed coordinates of tick anchors reproduce their labels;
3. **Known-value check** — compare at least one plotted value to an exact value stated in text/table;
4. **Independent repeat** — second digitization of a subset;
5. **Series-count check** — extracted groups/points match caption and legend.

For repeated/bulk tasks, independently re-digitize at least a small stratified subset of panels and
report absolute/relative disagreement.

## Precision policy

Digitized precision must reflect source resolution.

Do not output excessive decimal places. If a plot visually supports roughly one decimal place, do not
report four decimals just because the transform returns them.

Keep fields:

- `value_raw_digitized`
- `value_rounded_for_use`
- `precision_note`

## Uncertainty and error propagation

Pixel-level digitization uncertainty is different from biological sampling uncertainty.

Do not treat digitization uncertainty as SD/SE of the experiment. If quantified, store separately as:

- `digitization_uncertainty`
- `digitization_uncertainty_method`

For downstream meta-analysis, the study's sampling variance still requires author-reported or validly
reconstructed uncertainty.

## Data output schema

At minimum produce one row per extracted point/category with:

- `paper_id`
- `experiment_id` if known
- `arm_id` if known
- `figure_id`
- `panel_id`
- `series_id`
- `x_label`
- `x_value`
- `x_unit`
- `y_variable`
- `y_value`
- `y_unit`
- `central_or_error_component`
- `source_type=figure_digitized`
- `digitization_grade`
- `calibration_id`
- `qa_status`
- `notes`

Also retain a calibration table containing pixel anchors and real-axis anchor values.

## Bulk paper workflow

For many papers:

1. create a figure inventory;
2. classify panels into `TABLE_VALUE_EXISTS`, `DIGITIZABLE`, `MANUAL_REVIEW`, `NOT_QUANTIFIABLE`;
3. process simple Cartesian panels first;
4. isolate complex/dual-axis/heatmap panels;
5. QA each batch before moving to the next;
6. never let a failed panel block exact-value extraction from the rest of the paper.

Recommended batch outputs:

- `figure_inventory.csv`
- `digitization_queue.csv`
- `calibration_registry.csv`
- `digitized_points.csv`
- `figure_QA.csv`
- `unresolved_figures.csv`

## Research safeguards

- A figure point is not automatically an independent biological replicate.
- Repeated time points from one arm remain dependent.
- Values read from a fitted curve must not be mislabeled as raw observations.
- Do not reverse-engineer individual-level data from summary curves unless the source explicitly
  supports it.
- Do not claim exact error bars when caps overlap or resolution is inadequate.
- Do not use OCR as the first method for point coordinates; OCR is for labels/ticks when needed.
- Preserve the original figure image/panel hash or filename when possible for reproducibility.

## Integration with nature-paper-data-extractor

`nature-paper-data-extractor` owns study structure, schema and source provenance.
This skill owns figure calibration and numeric digitization.

When returning a digitized value to the paper extractor, always include:

- figure/panel locator;
- extraction grade;
- QA status;
- whether exact source data were searched first;
- whether the value is suitable for primary analysis or sensitivity only.

## Red lines

Never fabricate points hidden by overlap. Never estimate axes from image boundaries without tick
calibration. Never mix left/right y-axis series. Never call digitized values "reported exact values".
Never use a visual guess where a reproducible calibration can be performed.
