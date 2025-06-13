import streamlit as st
import pandas as pd
from app.validator import validate_promos
from app.deployer import deploy_promos

def upload_and_preview():
    uploaded_file = st.file_uploader("Upload Promo Rules CSV", type=['csv'])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of Uploaded Promo Rules:")
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
