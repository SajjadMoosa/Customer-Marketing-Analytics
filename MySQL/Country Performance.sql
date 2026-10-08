USE customer_marketing_db;

SELECT
    Country,
    COUNT(*) AS Transactions,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(SUM(Gross_Profit), 2) AS Gross_Profit,
    SUM(Conversions) AS Conversions
FROM customer_marketing_data
GROUP BY Country
ORDER BY Revenue DESC;