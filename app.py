import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="RetentionIQ",
    page_icon="📊",
    layout="wide"
)

st.title("📊 RetentionIQ")
st.subheader("Customer Churn Prediction & Retention Dashboard")

uploaded_file = st.file_uploader(
    "Upload the Telco Customer Churn CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    churned_customers = (df["Churn"] == "Yes").sum()
    churn_rate = (df["Churn"] == "Yes").mean() * 100

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Customers", len(df))
    col2.metric("Churned Customers", churned_customers)
    col3.metric("Churn Rate", f"{churn_rate:.1f}%")

    st.subheader("Data Preview")
    st.dataframe(df.head(20))

else:
    st.info("Upload the Telco Customer Churn CSV file to view the dashboard.")