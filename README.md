# Airline Data Analytics (Flight Network & Profitability Analysis)

An end-to-end commercial aviation analytics platform analyzing revenue, profitability, passenger volume, fleet economics, cost drivers, seasonality, and geographic network performance across 7,974 flight operations originating from Dubai International Airport (`DXB`).

---

## Verified Baseline Benchmarks
- **Total Flights**: 7,974
- **Total Passengers**: 2,031,928
- **Total Revenue**: $2,371,756,240.42
- **Total Cost**: $1,796,275,579.39
- **Total Profit**: $575,480,660.99
- **Profit Margin %**: 24.26%

---

## Project Structure
```
AIRLINE_DATA_ANALYTICS/
├── data/
│   ├── raw/
│   ├── processed/
│   └── lookup/
├── notebooks/
│   └── airline_eda.ipynb
├── sql/
│   ├── create_tables.sql
│   └── business_analysis.sql
├── powerbi/
│   ├── powerbi_dashboard_specification.md
│   └── power_query_script.m
├── outputs/
│   ├── charts/
│   ├── reports/
│   └── dashboard/
├── scripts/
├── README.md
└── requirements.txt
```

---

## How to Run
```bash
pip install -r requirements.txt
python scripts/generate_dataset.py
python scripts/data_cleaning.py
python scripts/build_dashboard_data.py
python scripts/generate_charts.py
python scripts/build_eda_notebook.py
```
Open `outputs/dashboard/index.html` in your web browser!
