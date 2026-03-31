import json
import requests as req
import math
from pathlib import Path

def getAllWarframeSetPrices():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    input_file = project_root / "filterItems" / "filtered_data.json"
    output_file = project_root / "prices" / "warframes" / "warframe_sets_prices.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)["warframe"]
        url = "https://api.warframe.market/v2/orders/item/"
        
        prices = {}

        for item in data.values():
            try:
                temp = []
                res = req.get(f"{url}{item['set']}/top") # calling the api
                res.raise_for_status() # raise error
                data = res.json()["data"]["sell"]
                for obj in data:
                    temp.append(obj["platinum"])
                prices[item['set']] = math.ceil(sum(temp) / len(temp))


            except req.Timeout:
                print("timeout")
            except ValueError:
                print("response was not valid json")
            except req.RequestException as error:
                print(f"req failed {error}")

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(prices, file, indent=4)
            print("all warframe sets saved")

if __name__ == "__main__":
    getAllWarframeSetPrices()