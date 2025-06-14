import os
import streamlit as st
import pandas as pd
from app.validator import validate_promos
from app.deployer import deploy_promos

def upload_and_preview():
    st.sidebar.markdown("### Demo Options")
    use_sample = st.sidebar.button("Load Sample Promo Data")

    df = None

    if use_sample:
        sample_path = os.path.join("data", "sample_promos.csv")
        try:
            df = pd.read_csv(sample_path)
            st.info("Loaded sample data from sample_promos.csv")
        except FileNotFoundError:
            st.error("Sample file not found. Make sure 'data/sample_promos.csv' exists.")
    else:
        uploaded_file = st.file_uploader("Upload Promo Rules CSV", type=['csv'])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)

    if df is not None:
        st.write("### Preview of Promo Rules")
        st.dataframe(df)

        is_valid, report = validate_promos(df)
        if is_valid:
            st.success("Promo rules passed validation.")
            if st.button("Deploy Promotions"):
                deploy_promos(df)
                st.success("Promotions deployed successfully.")
        else:
            st.error("Validation errors found:")
            st.json(report)