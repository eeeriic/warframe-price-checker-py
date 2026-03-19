import streamlit as st

st.set_page_config(
    page_title="Warframe Dashboard",
    page_icon="🐤"
)

st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 2.5rem;
    }
    </style>
    <div class="centered-title">Warframe Prices Dashboard</div>
    """,
    unsafe_allow_html=True
)