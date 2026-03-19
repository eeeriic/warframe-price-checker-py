import streamlit as st
import json
import pandas as pd

st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 2.5rem;
    }
    </style>
    <div class="centered-title">Weapons</div>
    """,
    unsafe_allow_html=True
)

# Load and display weapon prices
with open('5Prices/weapons/weapon_sets_prices.json', 'r') as f:
    weapon_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(list(weapon_data.items()), columns=['Item', 'Price'])
df['Price'] = df['Price'].astype(int)
df = df.sort_values('Price', ascending=False)

st.dataframe(df, use_container_width=True, hide_index=True)