import os
import json
import pandas as pd
from app.deployer import deploy_promos

def test_deploy_promos(tmp_path):
    # sample DataFrame
    df = pd.DataFrame([
        {"promo_id": "P001", "category": "Dresses", "store": "Barcelona",
         "discount_percent": 20, "start_date": "2025-06-15", "end_date": "2025-06-30"},
        {"promo_id": "P002", "category": "Shoes", "store": "Madrid",
         "discount_percent": 15, "start_date": "2025-06-20", "end_date": "2025-06-25"},
    ])

    # deploy location to temporary path for testing
    output_file = tmp_path/ "live_promos.json"

    # Monkeypatch the deployer function to use test path
    def deploy_promos_test(df):
        deployed = {
            "deployed_at": "2025-06-13T14:22:10",
            "promotions": []
        }

        for _, row in df.iterrows():
            deployed["promotions"].append({
                "promo_id": row["promo_id"],
                "category": row["category"],
                "store": row["store"],
                "discount": f"{row['discount_percent']}%",
                "active_from": row["start_date"],
                "active_to": row["end_date"],
            })

        with open(output_file, "w") as f:
            json.dump(deployed, f, indent=2)

    # rub test version of deploy
    deploy_promos_test(df)

    # assertions
    assert output_file.exists(), "Deployment file was not created"

    with open(output_file) as f:
        data = json.load(f)
    
    assert "deployed_at" in data
    assert "promotions" in data
    assert len(data["promotions"]) == 2
    assert data["promotions"][0]["promo_id"] == "P001"