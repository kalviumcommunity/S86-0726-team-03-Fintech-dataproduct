import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///analytics.db"

engine = create_engine(DATABASE_URL)

df = pd.read_sql(
    "SELECT * FROM vw_transaction_summary",
    engine
)
print(df)

fig = px.bar(
    df,
    x="Status",
    y="transaction_count",
    title="Transaction Count by Status",
    labels={
        "Status": "Transaction Status",
        "transaction_count": "Number of Transactions"
    }
)

fig.show()