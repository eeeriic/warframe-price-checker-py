import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

DATA_FOLDER = "data"

st.set_page_config(layout="wide")

st.title("Arcane Categories")

# Find all arcane CSV files dynamically
arcane_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv") and
                (f.startswith("wf_arcanes") or f.startswith("amp_arcanes") or f.startswith("kit_arcanes") or
                 f.startswith("mel_arcanes") or f.startswith("ope_arcanes") or f.startswith("pri_arcanes") or
                 f.startswith("sec_arcanes") or f.startswith("zaw_arcanes"))]

arcane_categories = {f.replace(".csv", ""): os.path.join(DATA_FOLDER, f) for f in arcane_files}

selected_arcane = st.selectbox("Select Arcane Category", list(arcane_categories.keys()))

# Load selected arcane CSV
df = pd.read_csv(arcane_categories[selected_arcane])

# Select and rename columns for cleaner display
df_display = df[['item_name', 'avg_price']].rename(columns={
    'item_name': 'Item Name',
    'avg_price': 'Average Price'
}).dropna()

# User choice to toggle view
view = st.radio("Choose view", ["Table", "Bar Chart"])

if view == "Table":
    st.dataframe(df_display)
else:
    df_sorted = df_display.sort_values("Average Price", ascending=True)  # ascending for horizontal bar chart (bottom to top)

    fig, ax = plt.subplots(figsize=(16, 16))

    bars = ax.barh(df_sorted["Item Name"], df_sorted["Average Price"], color="skyblue", height=0.3)

    # Add value labels on right side of bars
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0),  # 3 points horizontal offset
                    textcoords="offset points",
                    ha='left', va='center')

    ax.set_xlabel("Average Price")
    ax.set_title(f"Prices for {selected_arcane.replace('_', ' ').title()}")

    plt.tight_layout()
    st.pyplot(fig)

    # ---- Price Metrics Section ----
st.subheader("📊 Price Summary")

highest = df_display["Average Price"].max()
lowest = df_display["Average Price"].min()
average = round(df_display["Average Price"].mean(), 2)

col1, col2, col3 = st.columns(3)
col1.metric("🔺 Highest Price", f"{highest} plat")
col2.metric("🟡 Average Price", f"{average} plat")
col3.metric("🔻 Lowest Price", f"{lowest} plat")
