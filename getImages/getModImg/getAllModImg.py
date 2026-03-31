import json
import requests as req
from pathlib import Path

def getAllModsImg():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    filtered_file = project_root / "filterItems" / "filtered_data.json"
    output_dir = project_root / "assets" / "mods"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(filtered_file, "r", encoding="utf-8") as file:
        data = json.load(file)["mods"]
        url = "https://warframe.market/static/assets/"

        for key, item in data.items():
            try:
                res = req.get(f"{url}{item['img']}") # calling the api
                res.raise_for_status() # raise error

            except req.Timeout:
                print("timeout")
            except ValueError:
                print("response was not valid json")
            except req.RequestException as error:
                print(f"req failed {error}")

            slug = item.get("set", key)
            img_path = output_dir / f"{slug}.png"
            with open(img_path, "wb") as img:
                img.write(res.content)
                print(f"{slug} saved")

if __name__ == "__main__":
    getAllModsImg()