import streamlit as st
import csv
from pathlib import Path
from collections import defaultdict
import plotly.graph_objects as go

st.set_page_config(
    page_title="Customer & Marketing Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer & Marketing Analytics")
st.markdown("### Marketing Performance • Customer Intelligence • Revenue Analytics")

st.caption(
    "Interactive analytics dashboard for customer behavior, campaign performance, "
    "marketing efficiency and revenue insights."
)

st.divider()

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "data" / "customer_marketing_analytics.csv"

if not CSV_FILE.exists():
    st.error("CSV file not found!")
    st.code(str(CSV_FILE))
    st.stop()

# -----------------------------
# LOAD DATA
# -----------------------------

with open(CSV_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# -----------------------------
# FILTERS
# -----------------------------

st.subheader("🔎 Dashboard Filters")
st.caption("Filter the dashboard to analyze specific markets, channels, segments and industries.")

countries = sorted(set(row["Country"] for row in data))
regions = sorted(set(row["Region"] for row in data))
channels = sorted(set(row["Acquisition_Channel"] for row in data))
segments = sorted(set(row["Customer_Segment"] for row in data))
industries = sorted(set(row["Industry"] for row in data))

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    selected_country = st.selectbox("Country", ["All"] + countries)

with col2:
    selected_region = st.selectbox("Region", ["All"] + regions)

with col3:
    selected_channel = st.selectbox("Acquisition Channel", ["All"] + channels)

with col4:
    selected_segment = st.selectbox("Customer Segment", ["All"] + segments)

with col5:
    selected_industry = st.selectbox("Industry", ["All"] + industries)

# Apply filters
filtered_data = []

for row in data:

    if selected_country != "All" and row["Country"] != selected_country:
        continue

    if selected_region != "All" and row["Region"] != selected_region:
        continue

    if selected_channel != "All" and row["Acquisition_Channel"] != selected_channel:
        continue

    if selected_segment != "All" and row["Customer_Segment"] != selected_segment:
        continue

    if selected_industry != "All" and row["Industry"] != selected_industry:
        continue

    filtered_data.append(row)

# -----------------------------
# KPI CALCULATIONS
# -----------------------------

total_revenue = sum(float(row["Revenue"]) for row in filtered_data)
total_spend = sum(float(row["Marketing_Spend"]) for row in filtered_data)
total_profit = sum(float(row["Gross_Profit"]) for row in filtered_data)
total_conversions = sum(int(float(row["Conversions"])) for row in filtered_data)
total_leads = sum(int(float(row["Leads"])) for row in filtered_data)
total_clicks = sum(int(float(row["Clicks"])) for row in filtered_data)
total_impressions = sum(int(float(row["Impressions"])) for row in filtered_data)

if total_spend > 0:
    roas = total_revenue / total_spend
else:
    roas = 0

if total_clicks > 0:
    conversion_rate = (total_conversions / total_clicks) * 100
else:
    conversion_rate = 0

# =========================
# KPI SECTION
# =========================

st.subheader("📈 Key Performance Indicators")

st.caption("Overall business, marketing and conversion performance")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "💰 Revenue",
        f"${total_revenue:,.0f}"
    )

with k2:
    st.metric(
        "📣 Marketing Spend",
        f"${total_spend:,.0f}"
    )

with k3:
    st.metric(
        "📊 Gross Profit",
        f"${total_profit:,.0f}"
    )

with k4:
    st.metric(
        "🚀 ROAS",
        f"{roas:.2f}x"
    )


k5, k6, k7, k8 = st.columns(4)

with k5:
    st.metric(
        "🎯 Conversions",
        f"{total_conversions:,}"
    )

with k6:
    st.metric(
        "👥 Leads",
        f"{total_leads:,}"
    )

with k7:
    st.metric(
        "🖱️ Clicks",
        f"{total_clicks:,}"
    )

with k8:
    st.metric(
        "📈 Conversion Rate",
        f"{conversion_rate:.2f}%"
    )

st.divider()
# =========================
# MARKETING & GEOGRAPHY
# =========================

st.subheader("📊 Marketing & Geographic Performance")
st.caption("Revenue contribution across acquisition channels and countries")

chart1, chart2 = st.columns(2)

# -------------------------
# Revenue by Acquisition Channel
# -------------------------

with chart1:

    channel_revenue = defaultdict(float)

    for row in filtered_data:
        channel = row["Acquisition_Channel"]
        revenue = float(row["Revenue"])
        channel_revenue[channel] += revenue

    sorted_channels = sorted(
        channel_revenue.items(),
        key=lambda x: x[1],
        reverse=True
    )

    channel_names = [x[0] for x in sorted_channels]
    channel_values = [x[1] for x in sorted_channels]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=channel_names,
            y=channel_values,
            text=[f"${value:,.0f}" for value in channel_values],
            textposition="auto"
        )
    )

    fig.update_layout(
        title="Revenue by Acquisition Channel",
        xaxis_title="Channel",
        yaxis_title="Revenue",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# -------------------------
# Top 10 Countries
# -------------------------

with chart2:

    country_revenue = defaultdict(float)

    for row in filtered_data:
        country = row["Country"]
        revenue = float(row["Revenue"])
        country_revenue[country] += revenue

    top_countries = sorted(
        country_revenue.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    country_names = [x[0] for x in top_countries]
    country_values = [x[1] for x in top_countries]

    fig_country = go.Figure()

    fig_country.add_trace(
        go.Bar(
            x=country_values,
            y=country_names,
            orientation="h",
            text=[
                f"${value:,.0f}"
                for value in country_values
            ],
            textposition="auto"
        )
    )

    fig_country.update_layout(
        title="Top 10 Countries by Revenue",
        xaxis_title="Revenue",
        yaxis_title="Country",
        height=450
    )

    st.plotly_chart(
        fig_country,
        use_container_width=True
    )

st.divider()
# =========================
# CUSTOMER & CAMPAIGN PERFORMANCE
# =========================

st.subheader("👥 Customer & Campaign Performance")
st.caption("Revenue performance across customer segments and marketing campaigns")

chart3, chart4 = st.columns(2)

# -------------------------
# Customer Segment
# -------------------------

with chart3:

    segment_revenue = defaultdict(float)

    for row in filtered_data:
        segment = row["Customer_Segment"]
        revenue = float(row["Revenue"])
        segment_revenue[segment] += revenue

    sorted_segments = sorted(
        segment_revenue.items(),
        key=lambda x: x[1],
        reverse=True
    )

    segment_names = [x[0] for x in sorted_segments]
    segment_values = [x[1] for x in sorted_segments]

    fig_segment = go.Figure()

    fig_segment.add_trace(
        go.Bar(
            x=segment_names,
            y=segment_values,
            text=[
                f"${value:,.0f}"
                for value in segment_values
            ],
            textposition="auto"
        )
    )

    fig_segment.update_layout(
        title="Revenue by Customer Segment",
        xaxis_title="Customer Segment",
        yaxis_title="Revenue",
        height=450
    )

    st.plotly_chart(
        fig_segment,
        use_container_width=True
    )


# -------------------------
# Campaign Performance
# -------------------------

with chart4:

    campaign_data = defaultdict(
        lambda: {
            "revenue": 0,
            "spend": 0,
            "conversions": 0
        }
    )

    for row in filtered_data:

        campaign = row["Campaign"]

        campaign_data[campaign]["revenue"] += float(
            row["Revenue"]
        )

        campaign_data[campaign]["spend"] += float(
            row["Marketing_Spend"]
        )

        campaign_data[campaign]["conversions"] += int(
            float(row["Conversions"])
        )

    sorted_campaigns = sorted(
        campaign_data.items(),
        key=lambda x: x[1]["revenue"],
        reverse=True
    )

    # Show Top 10 campaigns
    top_campaigns = sorted_campaigns[:10]

    campaign_names = [
        x[0]
        for x in top_campaigns
    ]

    campaign_revenues = [
        x[1]["revenue"]
        for x in top_campaigns
    ]

    fig_campaign = go.Figure()

    fig_campaign.add_trace(
        go.Bar(
            x=campaign_revenues,
            y=campaign_names,
            orientation="h",
            text=[
                f"${value:,.0f}"
                for value in campaign_revenues
            ],
            textposition="auto"
        )
    )

    fig_campaign.update_layout(
        title="Top 10 Campaigns by Revenue",
        xaxis_title="Revenue",
        yaxis_title="Campaign",
        height=450
    )

    st.plotly_chart(
        fig_campaign,
        use_container_width=True
    )


st.divider()
# =========================
# REVENUE TREND & MARKETING EFFICIENCY
# =========================

st.subheader("📈 Revenue Trend & Marketing Efficiency")
st.caption("Monthly revenue growth and acquisition-channel efficiency")

chart5, chart6 = st.columns(2)

# -------------------------
# Monthly Revenue Trend
# -------------------------

with chart5:

    monthly_revenue = defaultdict(float)

    for row in filtered_data:
        month = row["Date"][:7]
        revenue = float(row["Revenue"])
        monthly_revenue[month] += revenue

    sorted_months = sorted(monthly_revenue.items())

    month_names = [item[0] for item in sorted_months]
    month_values = [item[1] for item in sorted_months]

    fig_monthly = go.Figure()

    fig_monthly.add_trace(
        go.Scatter(
            x=month_names,
            y=month_values,
            mode="lines+markers",
            text=[f"${value:,.0f}" for value in month_values],
            hovertemplate="%{x}<br>Revenue: %{text}<extra></extra>"
        )
    )

    fig_monthly.update_layout(
        title="Monthly Revenue Trend",
        xaxis_title="Month",
        yaxis_title="Revenue",
        height=450
    )

    st.plotly_chart(fig_monthly, use_container_width=True)


# -------------------------
# Marketing Spend vs Revenue
# -------------------------

with chart6:

    channel_performance = defaultdict(
        lambda: {
            "spend": 0,
            "revenue": 0
        }
    )

    for row in filtered_data:

        channel = row["Acquisition_Channel"]

        channel_performance[channel]["spend"] += float(
            row["Marketing_Spend"]
        )
        channel_performance[channel]["revenue"] += float(

            row["Revenue"]
        )

    sorted_performance = sorted(
        channel_performance.items(),
        key=lambda item: item[1]["revenue"],
        reverse=True
    )

    performance_channels = [
        item[0] for item in sorted_performance
    ]

    performance_spend = [
        item[1]["spend"] for item in sorted_performance
    ]

    performance_revenue = [
        item[1]["revenue"] for item in sorted_performance
    ]

    fig_spend_revenue = go.Figure()

    fig_spend_revenue.add_trace(
        go.Bar(
            name="Marketing Spend",
            x=performance_channels,
            y=performance_spend,
            text=[f"${value:,.0f}" for value in performance_spend],
            textposition="auto"
        )
    )

    fig_spend_revenue.add_trace(
        go.Bar(
            name="Revenue",
            x=performance_channels,
            y=performance_revenue,
            text=[f"${value:,.0f}" for value in performance_revenue],
            textposition="auto"
        )
    )

    fig_spend_revenue.update_layout(
        title="Marketing Spend vs Revenue",
        xaxis_title="Acquisition Channel",
        yaxis_title="Amount",
        barmode="group",
        height=450
    )

    st.plotly_chart(
        fig_spend_revenue,
        use_container_width=True
    )

st.divider()

# =========================
# CONVERSION & CUSTOMER RETENTION
# =========================

st.subheader("🔄 Conversion & Customer Retention")
st.caption("Marketing funnel performance and customer retention health")

chart7, chart8 = st.columns(2)

# -------------------------
# Marketing Conversion Funnel
# -------------------------

with chart7:

    total_impressions = sum(
        int(float(row["Impressions"]))
        for row in filtered_data
    )

    total_clicks = sum(
        int(float(row["Clicks"]))
        for row in filtered_data
    )

    total_leads = sum(
        int(float(row["Leads"]))
        for row in filtered_data
    )

    total_conversions = sum(
        int(float(row["Conversions"]))
        for row in filtered_data
    )

    funnel_labels = [
        "Impressions",
        "Clicks",
        "Leads",
        "Conversions"
    ]

    funnel_values = [
        total_impressions,
        total_clicks,
        total_leads,
        total_conversions
    ]

    fig_funnel = go.Figure(
        go.Funnel(
            y=funnel_labels,
            x=funnel_values,
            textinfo="value+percent initial"
        )
    )

    fig_funnel.update_layout(
        title="Marketing Conversion Funnel",
        height=450
    )

    st.plotly_chart(
        fig_funnel,
        use_container_width=True
    )


# -------------------------
# Customer Retention & Churn
# -------------------------

with chart8:

    retention_values = [
        float(row["Retention_Rate_Pct"])
        for row in filtered_data
    ]

    churn_values = [
        float(row["Churn_Rate_Pct"])
        for row in filtered_data
    ]

    if retention_values:
        average_retention = (
            sum(retention_values)
            / len(retention_values)
        )
    else:
        average_retention = 0

    if churn_values:
        average_churn = (
            sum(churn_values)
            / len(churn_values)
        )
    else:
        average_churn = 0

    retention_labels = [
        "Retention Rate",
        "Churn Rate"
    ]

    retention_data = [
        average_retention,
        average_churn
    ]

    fig_retention = go.Figure()

    fig_retention.add_trace(
        go.Bar(
            x=retention_labels,
            y=retention_data,
            text=[
                f"{average_retention:.2f}%",
                f"{average_churn:.2f}%"
            ],
            textposition="auto"
        )
    )

    fig_retention.update_layout(
        title="Customer Retention vs Churn",
        xaxis_title="Customer Metric",
        yaxis_title="Percentage",
        height=450
    )

    st.plotly_chart(
        fig_retention,
        use_container_width=True
    )


st.divider()

# =========================
# CUSTOMER VALUE & SATISFACTION
# =========================

st.subheader("⭐ Customer Value & Satisfaction")
st.caption("Customer lifetime value and satisfaction indicators")

ltv_values = [
    float(row["Customer_LTV"])
    for row in filtered_data
]

nps_values = [
    float(row["NPS"])
    for row in filtered_data
]

csat_values = [
    float(row["CSAT"])
    for row in filtered_data
]

if ltv_values:
    average_ltv = sum(ltv_values) / len(ltv_values)
else:
    average_ltv = 0

if nps_values:
    average_nps = sum(nps_values) / len(nps_values)
else:
    average_nps = 0

if csat_values:
    average_csat = sum(csat_values) / len(csat_values)
else:
    average_csat = 0


value1, value2, value3 = st.columns(3)

with value1:
    st.metric(
        "💎 Average Customer LTV",
        f"${average_ltv:,.0f}"
    )

with value2:
    st.metric(
        "⭐ Average NPS",
        f"{average_nps:.1f}"
    )

with value3:
    st.metric(
        "😊 Average CSAT",
        f"{average_csat:.1f}"
    )

st.divider()
