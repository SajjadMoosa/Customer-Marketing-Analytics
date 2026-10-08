USE customer_marketing_db;

SELECT
    Customer_Status,
    COUNT(DISTINCT Customer_ID) AS Customers,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(AVG(Customer_LTV), 2) AS Avg_LTV,
    ROUND(AVG(Retention_Rate_Pct), 2) AS Avg_Retention,
    ROUND(AVG(Churn_Rate_Pct), 2) AS Avg_Churn
FROM customer_marketing_data
GROUP BY Customer_Status
ORDER BY Revenue DESC;