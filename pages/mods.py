import streamlit as st
import json
import pandas as pd
from pathlib import Path

st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 2.5rem;
    }
    </style>
    <div class="centered-title">Mods</div>
    """,
    unsafe_allow_html=True
)

# Load and display mod prices
script_dir = Path(__file__).parent
project_root = script_dir.parent
prices_file = project_root / "prices" / "mods" / "mod_prices.json"

with open(prices_file, 'r') as f:
    mod_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(list(mod_data.items()), columns=['Item', 'Price'])
df['Price'] = df['Price'].astype(int)
df = df.sort_values('Price', ascending=False)

st.dataframe(df, use_container_width=True, hide_index=True)