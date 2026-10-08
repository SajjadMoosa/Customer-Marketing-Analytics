USE customer_marketing_db;

SELECT
    Customer_Segment,
    COUNT(*) AS Transactions,
    COUNT(DISTINCT Customer_ID) AS Customers,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(SUM(Gross_Profit), 2) AS Gross_Profit,
    ROUND(AVG(Customer_LTV), 2) AS Avg_Customer_LTV,
    ROUND(AVG(NPS), 2) AS Avg_NPS,
    ROUND(AVG(CSAT), 2) AS Avg_CSAT
FROM customer_marketing_data
GROUP BY Customer_Segment
ORDER BY Revenue DESC;