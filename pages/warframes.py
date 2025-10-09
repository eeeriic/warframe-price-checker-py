import streamlit as st
import pandas as pd
import os

DATA_FOLDER = "data"
IMG_FOLDER = "img"

st.set_page_config(layout="wide")

st.title("Warframes Prime Sets and Parts")

# Load datasets
sets_path = os.path.join(DATA_FOLDER, "wf_sets.csv")
df_sets = pd.read_csv(sets_path)

# Select only the columns you want, rename for nicer headers
df_display = df_sets[['item_name', 'avg_price']].rename(columns={
    'item_name': 'Item Name',
    'avg_price': 'Average Price'
})

st.header("Warframe Prime Sets")
st.dataframe(df_display)

# ---- Price Metrics Section ----
st.subheader("📊 Price Summary")

highest = df_display["Average Price"].max()
lowest = df_display["Average Price"].min()
average = round(df_display["Average Price"].mean(), 2)

col1, col2, col3 = st.columns(3)
col1.metric("🔺 Highest Price", f"{highest} plat")
col2.metric("🟡 Average Price", f"{average} plat")
col3.metric("🔻 Lowest Price", f"{lowest} plat")