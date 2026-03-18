import json

with open('1getData/raw_all_items.json', 'r', encoding="utf-8") as f:
    data = json.load(f)['data']

# Example for the first item in your list
first_item = data[0]
# Access the nested dictionary for the English localization
i18n_en = first_item.get('i18n', {}).get('en', {})

image_url = i18n_en.get('icon') # or 'thumb'
item_name = i18n_en.get('name')

if image_url and item_name:
    # The full URL is usually prefixed with the market's domain
    full_image_url = f"https://warframe.market/static/assets/{image_url}"
    print(f"Image URL for {item_name}: {full_image_url}")
else:
    print("Image URL or item name not found for this item.")
