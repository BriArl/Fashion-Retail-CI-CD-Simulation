import json
from datetime import datetime
import os

def deploy_promos(df):
    deployed = {
        "deployed_at": datetime.now.isoformat(),
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

    os.makedirs("data/deployed", exist_ok=True)
    with open("data/deployed/live_promos.json", "w") as f:
        json.dump(deployed, f, indent=2)