CREATE DATABASE IF NOT EXISTS customer_marketing_db;
USE customer_marketing_db;

DROP TABLE IF EXISTS customer_marketing;

CREATE TABLE customer_marketing (
    Transaction_ID VARCHAR(30) PRIMARY KEY,
    Date DATE,
    Customer_ID VARCHAR(30),
    Age INT,
    Gender VARCHAR(20),
    Country VARCHAR(80),
    Region VARCHAR(50),
    Industry VARCHAR(60),
    Customer_Segment VARCHAR(30),
    Acquisition_Channel VARCHAR(50),
    Campaign VARCHAR(80),
    Product VARCHAR(80),
    Device VARCHAR(30),
    Promotion VARCHAR(30),
    Impressions INT,
    Clicks INT,
    Leads INT,
    Conversions INT,
    Marketing_Spend DECIMAL(14,2),
    Revenue DECIMAL(14,2),
    Gross_Profit DECIMAL(14,2),
    COGS DECIMAL(14,2),
    Retention_Rate_Pct DECIMAL(6,2),
    Churn_Rate_Pct DECIMAL(6,2),
    Customer_LTV DECIMAL(14,2),
    NPS INT,
    CSAT DECIMAL(4,2),
    Touchpoints INT,
    Customer_Status VARCHAR(20),
    INDEX idx_date (Date),
    INDEX idx_channel (Acquisition_Channel),
    INDEX idx_customer (Customer_ID),
    INDEX idx_segment (Customer_Segment)
);
