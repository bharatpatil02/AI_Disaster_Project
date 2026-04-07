import streamlit as st
import pandas as pd

df = pd.read_csv("data/predictions.csv")

st.set_page_config(
    page_title="AI Disaster Dashboard",
    layout="wide",
    page_icon="🌍"
)

st.title("🌍 AI-Driven Disaster Prediction & Alert System")

# Top metrics
col1, col2, col3 = st.columns(3)

col1.metric("🌊 Flood Alerts", 1)
col2.metric("🔥 Wildfire Alerts", 1)
col3.metric("🌡 Heatwave Alerts", 1)

st.write("---")

# Prediction data
st.subheader("📊 Live Prediction Data")
st.dataframe(df, use_container_width=True)

# Alerts
st.subheader("🚨 Active Alerts")

for _, row in df[df["Severity"] == "High"].iterrows():
    st.error(
        f"⚠ {row['Disaster_Type']} HIGH risk in "
        f"{row['Region']} | Probability: {row['Probability']}"
    )

# Chart
st.subheader("📈 Severity Distribution")
st.bar_chart(df["Severity"].value_counts())

