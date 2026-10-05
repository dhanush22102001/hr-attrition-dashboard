# HR Attrition Dashboard — Insights (sample data)

> Fictional sample dataset created for portfolio demonstration. Not real employee data.

## Headline metrics
- Employees analysed: **240**
- Employees who left: **48**
- Overall attrition rate: **20.0%**

## Attrition by department
| Department | Employees | Left | Attrition % |
|---|---:|---:|---:|
| Customer Support | 48 | 14 | 29.2% |
| Sales | 62 | 18 | 29.0% |
| Human Resources | 16 | 3 | 18.8% |
| Finance | 14 | 2 | 14.3% |
| Operations | 38 | 5 | 13.2% |
| Marketing | 18 | 2 | 11.1% |
| Engineering | 44 | 4 | 9.1% |

## Attrition by tenure
| Tenure band | Employees | Left | Attrition % |
|---|---:|---:|---:|
| 0-2 yrs | 36 | 11 | 30.6% |
| 2-5 yrs | 55 | 7 | 12.7% |
| 5+ yrs | 149 | 30 | 20.1% |

## Top exit reasons
- Career growth: 19 exits
- Work-life balance: 8 exits
- Manager support: 8 exits
- Compensation: 6 exits
- Career change: 4 exits
- Relocation: 3 exits

## What this shows (how to read it in an interview)
- Attrition is concentrated in the first 2 years and in frontline-heavy teams (Sales / Customer Support).
- Low job-satisfaction (<=2) and poor work-life balance scores cluster among leavers.
- Career growth and compensation dominate stated exit reasons — pointing to progression paths and pay-band reviews as first interventions.

## Files
- `data/hr_attrition_sample.csv` — fictional employee-level dataset
- `analysis/attrition_analysis.py` — stdlib Python that computes every metric above
- `dashboard/index.html` — standalone dashboard page (open in a browser)
