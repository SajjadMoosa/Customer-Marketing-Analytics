USE customer_marketing_db;

CREATE OR REPLACE VIEW vw_customer_marketing AS
SELECT
    Transaction_ID,
    Date,
    Customer_ID,
    Age,
    Gender,
    Country,
    Region,
    Industry,
    Customer_Segment,
    Acquisition_Channel,
    Campaign,
    Product,
    Device,
    Promotion,
    Impressions,
    Clicks,
    Leads,
    Conversions,
    Marketing_Spend,
    Revenue,
    Gross_Profit,
    COGS,
    Retention_Rate_Pct,
    Churn_Rate_Pct,
    Customer_LTV,
    NPS,
    CSAT,
    Touchpoints,
    Customer_Status,

    CASE
        WHEN Marketing_Spend > 0
        THEN Revenue / Marketing_Spend
        ELSE 0
    END AS ROAS,

    CASE
        WHEN Clicks > 0
        THEN (Conversions / Clicks) * 100
        ELSE 0
    END AS Conversion_Rate_Pct,

    CASE
        WHEN Impressions > 0
        THEN (Clicks / Impressions) * 100
        ELSE 0
    END AS CTR_Pct

FROM customer_marketing_data;