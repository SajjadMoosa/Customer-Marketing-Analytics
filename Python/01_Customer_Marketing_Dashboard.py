import streamlit as st
import pandas as pd
from pathlib import Path

# ============================================================
# CUSTOMER & MARKETING ANALYTICS DASHBOARD
# ============================================================

st.set_page_config(
    page_title="Customer & Marketing Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer & Marketing Analytics")
st.caption("Customer, Marketing & Revenue Performance Dashboard")

# ============================================================
# FIND DATA FILE
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

possible_files = [
    BASE_DIR / "data" / "customer_marketing_analytics.csv",
    BASE_DIR / "customer_marketing_analytics.csv"
]

CSV_FILE = None

for file in possible_files:
    if file.exists():
        CSV_FILE = file
        break

# ============================================================
# CHECK CSV
# ============================================================

if CSV_FILE is None:

    st.error("❌ Customer Marketing CSV file was not found.")

    st.write("Expected location:")

    st.code(
        str(BASE_DIR / "data" / "customer_marketing_analytics.csv")
    )

    st.stop()

# ============================================================
# LOAD DATA
# ============================================================

try:

    df = pd.read_csv(CSV_FILE)

except Exception as e:

    st.error("❌ Error loading CSV file.")
    st.exception(e)
    st.stop()

# ============================================================
# DATA INFORMATION
# ============================================================

st.success("✅ Dataset loaded successfully!")

st.info(
    f"File: {CSV_FILE.name} | "
    f"Rows: {len(df):,} | "
    f"Columns: {len(df.columns):,}"
)

# ============================================================
# DATE
# ============================================================

if "Date" in df.columns:

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

# ============================================================
# KPI CALCULATIONS
# ============================================================

def total(column):
    if column in df.columns:
        return df[column].sum()
    return 0


def average(column):
    if column in df.columns:
        return df[column].mean()
    return 0


total_revenue = total("Revenue")
marketing_spend = total("Marketing_Spend")
gross_profit = total("Gross_Profit")
impressions = total("Impressions")
clicks = total("Clicks")
leads = total("Leads")
conversions = total("Conversions")

average_ltv = average("Customer_LTV")
average_nps = average("NPS")
average_csat = average("CSAT")
average_retention = average("Retention_Rate_Pct")
average_churn = average("Churn_Rate_Pct")

# ============================================================
# MARKETING METRICS
# ============================================================

roas = (
    total_revenue / marketing_spend
    if marketing_spend != 0
    else 0
)

ctr = (
    clicks / impressions * 100
    if impressions != 0
    else 0
)

conversion_rate = (
    conversions / leads * 100
    if leads != 0
    else 0
)

profit_margin = (
    gross_profit / total_revenue * 100
    if total_revenue != 0
    else 0
)

# ============================================================
# KPI CARDS
# ============================================================

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"${total_revenue:,.0f}"
)

col2.metric(
    "Marketing Spend",
    f"${marketing_spend:,.0f}"
)

col3.metric(
    "Gross Profit",
    f"${gross_profit:,.0f}"
)

col4.metric(
    "ROAS",
    f"{roas:.2f}x"
)

col5, col6, col7, col8 = st.columns(4)

col5.metric(
    "Impressions",
    f"{impressions:,.0f}"
)

col6.metric(
    "Clicks",
    f"{clicks:,.0f}"
)

col7.metric(
    "Leads",
    f"{leads:,.0f}"
)

col8.metric(
    "Conversions",
    f"{conversions:,.0f}"
)

# ============================================================
# MARKETING METRICS
# ============================================================

st.subheader("Marketing Performance")

m1, m2, m3, m4 = st.columns(4)

m1.metric(
    "CTR",
    f"{ctr:.2f}%"
)

m2.metric(
    "Conversion Rate",
    f"{conversion_rate:.2f}%"
)

m3.metric(
    "Profit Margin",
    f"{profit_margin:.2f}%"
)

m4.metric(
    "Customer LTV",
    f"${average_ltv:,.0f}"
)

# ============================================================
# CUSTOMER METRICS
# ============================================================

st.subheader("Customer Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Retention Rate",
    f"{average_retention:.2f}%"
)

c2.metric(
    "Churn Rate",
    f"{average_churn:.2f}%"
)

c3.metric(
    "NPS",
    f"{average_nps:.1f}"
)

c4.metric(
    "CSAT",
    f"{average_csat:.1f}"
)

# ============================================================
# DATA PREVIEW
# ============================================================

st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# ============================================================
# DATASET SUMMARY
# ============================================================

st.subheader("Dataset Information")

info1, info2, info3 = st.columns(3)

info1.metric(
    "Rows",
    f"{len(df):,}"
)

info2.metric(
    "Columns",
    f"{len(df.columns):,}"
)

info3.metric(
    "Missing Values",
    f"{df.isnull().sum().sum():,}"
)

# ============================================================
# CUSTOMER SEGMENT
# ============================================================

if "Customer_Segment" in df.columns:

    st.subheader("Revenue by Customer Segment")

    segment = (
        df.groupby("Customer_Segment")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(segment)

# ============================================================
# ACQUISITION CHANNEL
# ============================================================

if "Acquisition_Channel" in df.columns:

    st.subheader("Revenue by Acquisition Channel")

    channel = (
        df.groupby("Acquisition_Channel")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(channel)

# ============================================================
# MONTHLY REVENUE
# ============================================================

if "Date" in df.columns and "Revenue" in df.columns:

    st.subheader("Monthly Revenue")

    monthly = (
        df.dropna(subset=["Date"])
        .set_index("Date")["Revenue"]
        .resample("ME")
        .sum()
    )

    st.line_chart(monthly)

# ============================================================
# COUNTRY
# ============================================================

if "Country" in df.columns:

    st.subheader("Revenue by Country")

    country = (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(country)

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.success(
    "Customer & Marketing Analytics Dashboard is running successfully."
)