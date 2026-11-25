# Lens: Data Science

For analysis, modelling, and machine-learning work — from a one-off analysis to a production model.

## How the sections read in this field

| Section | Ask it as |
|---|---|
| Context | Business or scientific domain, decision the analysis supports, data sources and their origin, prior models or analyses (**referenced works**) |
| Constraints | Data access, privacy and consent, compute budget, latency, interpretability requirements, labelling capacity, deadlines |
| Problem | The decision or question today; final objective = metric and threshold on a defined evaluation set, or the decision delivered |
| Tools | Languages, notebooks, data platforms, modelling libraries, experiment tracking, deployment and monitoring |

## Default criteria (keep, drop, or add)

1. **Target is defined** — the outcome variable or question is precise, with a baseline to beat.
2. **Evaluation is honest** — a held-out or time-split evaluation set; no leakage from it into training.
3. **Data is understood** — provenance, coverage, missingness, and known biases are documented.
4. **Metric matches the decision** — the metric reflects the real cost of errors.
5. **Results are reproducible** — code, data version, seeds, and parameters are tracked.
6. **Limits are stated** — where the model or analysis should not be used.

## Drift signals

- The metric or the evaluation set changes after results are seen.
- Features are added that would not be available at prediction time.
- Model complexity grows without a gain on the agreed metric.
- The analysis starts answering a more interesting question than the one asked.

## Typical tools

Python (pandas, scikit-learn, PyTorch), R, SQL, Jupyter, dbt, Spark, MLflow or Weights & Biases,
cloud ML platforms, dashboards.
