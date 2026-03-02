import json

def filter_all_items():
    with open("../1getData/raw_all_items.json", "r", encoding="utf-8") as file:
        data = json.load(file)["data"]
        all_items = [item for item in data if any(tag in ["prime", "arcane_enhancement", "mod"] for tag in item['tags'])]

        with open("all_items.json", "w", encoding="utf-8") as file:
            json.dump(all_items, file, indent=4)
            print("all items saved")


filter_all_items()