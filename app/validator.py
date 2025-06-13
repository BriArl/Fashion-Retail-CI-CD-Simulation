from datetime import datetime
from dateutil.parser import parse

VALID_CATEGORIES = ["Dresses", "Shoes", "Tops"]
VALID_STORES = ["Barcelona", "Madrid", "Online"]

def validate_promos(df):
    errors = []
    seen_ids = set()

    for idx, row in df.iterrows():
        pid, cat, store, start, end = row["promo_id"], row["category"], row["store"], row["start_date"], row["end_date"]

        if pid in seen_ids:
            errors.append(f"Duplicate promo_id at row {idx}: {pid}")
        seen_ids.add(pid)

        if cat not in VALID_CATEGORIES:
            errors.append(f"Invalid category at row {idx}: {cat}")
        if store not in VALID_STORES:
            errors.append(f"Invalid store at row {idx}: {store}")
        
        try:
            start_date = parse(start)
            end_date = parse(end)
            if start_date > end_date:
                errors.append(f"Start date after end date at row {idx}")
        except Exception:
            errors.append(f"Invalid date format at row {idx}")

    return (len(errors) == 0, errors)