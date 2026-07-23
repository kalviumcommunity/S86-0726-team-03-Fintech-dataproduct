import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine("sqlite:///analytics.db")

# Load transaction summary from SQL view
transaction_summary = pd.read_sql(
    "SELECT * FROM vw_transaction_summary",
    engine
)

# Extract values
total_transactions = transaction_summary["transaction_count"].sum()
#Here as the SQL view here does not give the total count and its give the indivudail success and failure count we need to add this for getting the total cnt.

total_amount = transaction_summary["total_amount"].sum()
#Here as the SQL view here does not give the total amt and its give the indivudail success and failure amt we need to add this for getting the total amt.


successful_transactions = transaction_summary.loc[
    transaction_summary["Status"] == "SUCCESS",
    "transaction_count"
].iloc[0]

failed_transactions = transaction_summary.loc[
    transaction_summary["Status"] == "FAILED",
    "transaction_count"
].iloc[0]

success_rate = (
    successful_transactions / total_transactions
) * 100


# Dashboard title
st.title("Fintech Payment Analytics Dashboard")

# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Total Transactions",
        f"{total_transactions:,}"
    )

with col2:
    st.metric(
        "Total Amount",
        f"₹{total_amount:,.2f}"
    )

with col3:
    st.metric(
        "Successful Transactions",
        f"{successful_transactions:,}"
    )

with col4:
    st.metric(
        "Failed Transactions",
        f"{failed_transactions:,}"
    )

with col5:
    st.metric(
        "Success Rate",
        f"{success_rate:.1f}%"
    )