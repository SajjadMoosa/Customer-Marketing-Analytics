USE customer_marketing_db;

SELECT
    Acquisition_Channel,
    COUNT(*) AS Transactions,
    ROUND(SUM(Marketing_Spend), 2) AS Marketing_Spend,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(SUM(Gross_Profit), 2) AS Gross_Profit,
    SUM(Conversions) AS Conversions,
    ROUND(
        SUM(Revenue) / NULLIF(SUM(Marketing_Spend), 0),
        2
    ) AS ROAS
FROM customer_marketing_data
GROUP BY Acquisition_Channel
ORDER BY Revenue DESC;