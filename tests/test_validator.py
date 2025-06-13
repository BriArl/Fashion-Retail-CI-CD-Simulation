from app.validator import validate_promos
import pandas as pd

def test_valid_data():
    df = pd.DataFrame([
        {"promo_id": "P001", "category": "Dresses", "store": "Barcelona", "discount_percent": 20, "start_date": "2025-06-15", "end_date": "2025-06-30"}
    ])
    is_valid, errors = validate_promos(df)
    assert is_valid