USE customer_marketing_db;

SELECT
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    ROUND(SUM(Marketing_Spend), 2) AS Marketing_Spend,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(SUM(Gross_Profit), 2) AS Gross_Profit,
    SUM(Impressions) AS Impressions,
    SUM(Clicks) AS Clicks,
    SUM(Leads) AS Leads,
    SUM(Conversions) AS Conversions,
    ROUND(
        SUM(Revenue) / NULLIF(SUM(Marketing_Spend), 0),
        2
    ) AS ROAS
FROM customer_marketing_data
GROUP BY DATE_FORMAT(Date, '%Y-%m')
ORDER BY Month;