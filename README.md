# Customer & Marketing Analytics Dashboard

Advanced portfolio project combining **Python + MySQL + Power BI** to analyze customer behavior, marketing acquisition, campaign efficiency, revenue, profitability, retention, churn, LTV and customer experience.

## Project objective
Build an executive-ready analytics solution that answers:

- Which marketing channels generate revenue efficiently?
- Which campaigns produce the strongest ROAS?
- Which customer segments have the highest value?
- Where is churn/retention strongest or weakest?
- Which products and regions drive revenue and profit?
- How do marketing spend, conversions and revenue change over time?
- Which customers show high LTV and strong engagement?

## Tech stack
- Python — data cleaning, feature engineering and EDA
- MySQL — database storage and SQL analytics
- Power BI — executive dashboard, DAX and interactive analysis
- GitHub — portfolio documentation and source control

## Repository structure
```text
customer-marketing-analytics/
│
├── data/
│   ├── customer_marketing_analytics.csv
│   ├── DATA_DICTIONARY.md
│   └── ...
│
├── python/
│   ├── 01_clean_and_engineer.py
│   ├── 02_eda_and_insights.py
│   ├── 03_executive_summary.py
│   └── requirements.txt
│
├── mysql/
│   ├── 01_create_database_and_table.sql
│   ├── 02_analytics_queries.sql
│   └── 03_load_csv.sql
│
├── powerbi/
│   └── POWER_BI_BUILD_GUIDE.md
│
└── README.md
```

## Dataset
The included sample dataset contains 15,000 marketing/customer transactions across:
- acquisition channels
- campaigns
- customer segments
- industries
- products
- countries and regions
- devices and promotions
- impressions, clicks and leads
- conversions
- marketing spend
- revenue and gross profit
- LTV
- retention/churn
- NPS and CSAT

This is a synthetic portfolio dataset created for demonstration and learning. It should not be represented as real client/company data.

## Python workflow
1. Install dependencies:
```bash
pip install -r python/requirements.txt
```

2. Run:
```bash
python python/01_clean_and_engineer.py
python python/02_eda_and_insights.py
python python/03_executive_summary.py
```

The Python layer creates derived metrics such as:
- CTR
- lead rate
- conversion rate
- ROAS
- CAC

## MySQL workflow
1. Open MySQL Workbench.
2. Run `mysql/01_create_database_and_table.sql`.
3. Load the cleaned CSV using `mysql/03_load_csv.sql`.
4. Run `mysql/02_analytics_queries.sql`.
5. Confirm the row count is 15,000.

## Power BI workflow
Connect Power BI to:
`customer_marketing_db` → `customer_marketing`

Create DAX measures for:
- Total Revenue
- Total Spend
- Gross Profit
- ROAS
- CAC
- Customers
- Avg LTV
- Avg NPS
- Avg Churn
- Avg Retention

Recommended report pages:
1. Executive Overview
2. Marketing Performance
3. Customer Intelligence
4. Campaign & Product
5. Geography & Drillthrough
6. Product & Customer Segment Analytics
7. Executive Performance Summary
8. Business Insights & Management Actions

## Business insights framework
When writing the final portfolio case study, focus on:
1. **Acquisition efficiency** — compare spend, revenue, ROAS and CAC.
2. **Customer value** — compare LTV, revenue and retention by segment.
3. **Customer experience** — connect NPS/CSAT with customer value.
4. **Retention risk** — identify segments/geographies with higher churn.
5. **Growth opportunities** — identify strong campaigns/products and investigate why they perform well.
6. **Budget optimization** — use ROAS/CAC as evidence, while noting that attribution data does not prove incremental causality.

## Portfolio description
> Built an end-to-end Customer & Marketing Analytics solution using Python, MySQL and Power BI. The project combines marketing performance, customer segmentation, LTV, retention, churn, campaign efficiency and executive KPIs into an interactive analytics workflow.

## Important analytical note
ROAS and CAC are attribution-style metrics in this synthetic dataset. They are useful for portfolio analysis but do not by themselves establish causal or incremental marketing impact.

## License
For portfolio, learning and demonstration purposes.
