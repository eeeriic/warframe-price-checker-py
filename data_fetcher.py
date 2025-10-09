from filter import get_filtered_items
from images import download_image
from prices_df import build_price_df
from prices import get_average_price, get_average_price_arcane
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

filtered = get_filtered_items()

# Normal categories
main_categories = ["wf_sets", "wf_parts", "companion_sets", "companion_parts", "weapon_sets", "weapon_parts"]

for category in main_categories:
    df = build_price_df(filtered[category], price_func=get_average_price)
    df.to_csv(f"data/{category}.csv", index=False)

    for item in filtered[category]:
        download_image(item, category)

# Arcane categories
for arcane_cat, items in filtered["arcanes"].items():
    df = build_price_df(items, price_func=get_average_price_arcane)
    df.to_csv(f"data/{arcane_cat}.csv", index=False)

    for item in items:
        download_image(item, arcane_cat)
