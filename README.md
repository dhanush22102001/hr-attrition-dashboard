# HR Attrition Dashboard

A People Analytics portfolio project: an attrition dashboard built from a fictional 240-employee dataset, showing the metrics an HR team actually reviews — overall attrition, attrition by department and tenure, and exit-reason patterns.

> **Data honesty:** every row is fictional sample data generated for this portfolio. The methods (attrition %, department/tenure cuts, exit-reason analysis) mirror real HR reporting.

## Headline findings (from the sample data)

- **20.0%** overall attrition (48 of 240 employees)
- Highest attrition: **Customer Support 29.2%** and **Sales 29.0%**; lowest: **Engineering 9.1%**
- **First 2 years are the risk window:** 30.6% attrition vs 12.7% at 2–5 years
- Top exit reason: **Career growth** (19 exits), then work-life balance and manager support

## What's inside

| File | What it is |
|---|---|
| `data/hr_attrition_sample.csv` | Fictional employee-level dataset (department, role, tenure, salary, satisfaction, work-life balance, performance, overtime, attrition, exit reason) |
| `analysis/attrition_analysis.py` | Standard-library Python that computes every metric on this page |
| `analysis/insights.md` | Written insights — how each metric is calculated and how to talk through it |
| `dashboard/index.html` | Standalone dashboard page — open it in any browser |

## Run the analysis

```bash
python3 analysis/attrition_analysis.py
```

## Skills demonstrated

HR Analytics · People Analytics · Python · Data Visualization · Dashboard design · Excel/Power BI-style KPI reporting (attrition rate, department mix, tenure bands, exit reasons)

## Next steps

- Rebuild the same metrics as a Power BI report (`.pbix`) with slicers for department and tenure
- Add a monthly attrition trend view and a "flight risk" scoring cut
- Swap the fictional CSV for an anonymised real export and rerun — the script doesn't change
