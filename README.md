# Fashion Promo CI/CD Simulation

## Overview

This project simulates a CI/CD pipeline for deploying promotional pricing rules in a fashion retail environment. It allows users to:

- Upload CSV promo rules (discounts by category/store/date)
- Validate promo logic (categories, dates, duplicates)
- Preview promos before deployment
- Deploy validated promos to a JSON file with audit logging

Built with Python, Pandas, and Streamlit for an interactive, user-friendly experience.

## Features

- CSV upload and preview of promo rules  
- Validation for categories, stores, date ranges, and duplicates  
- Deployment writes to `data/deployed/live_promos.json` with timestamp  
- Includes sample promo CSV for quick demos  
- Clear UI messages for success and validation errors

---
Live app: https://fashion-retail-ci-cd-simulation-drlamrjufhz6si3hvgblmv.streamlit.app/
