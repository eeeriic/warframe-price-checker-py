import json
from pathlib import Path

def filter_all_items():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    input_file = project_root / "getData" / "raw_all_items.json"
    output_file = project_root / "filterData" / "all_items.json"
    
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)["data"]
        all_items = [item for item in data if any(tag in ["prime", "arcane_enhancement", "mod"] for tag in item['tags'])]

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(all_items, file, indent=4)
            print("all items saved")


if __name__ == "__main__":
    filter_all_items()