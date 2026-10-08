USE customer_marketing_db;

SELECT
    COUNT(*) AS Total_Transactions,
    COUNT(DISTINCT Customer_ID) AS Unique_Customers,
    MIN(Date) AS Start_Date,
    MAX(Date) AS End_Date,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(SUM(Marketing_Spend), 2) AS Total_Marketing_Spend,
    ROUND(SUM(Gross_Profit), 2) AS Total_Gross_Profit,
    SUM(Conversions) AS Total_Conversions,
    SUM(Leads) AS Total_Leads,
    SUM(Clicks) AS Total_Clicks
FROM customer_marketing_data;