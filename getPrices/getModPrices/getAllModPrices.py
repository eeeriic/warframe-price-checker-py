import json
import requests as req
import math
from pathlib import Path

def getAllModPrices():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    input_file = project_root / "filterItems" / "filtered_data.json"
    output_file = project_root / "prices" / "mods" / "mod_prices.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)["mods"]
        url = "https://api.warframe.market/v2/orders/item/"
        
        prices = {}

        for item in data.values():
            try:
                temp = []
                res = req.get(f"{url}{item['mod']}/top?rank={item['rank']}") # calling the api
                res.raise_for_status() # raise error
                data = res.json()["data"]["sell"]
                for obj in data:
                    temp.append(obj["platinum"])
                if len(temp) == 0:
                    print(f"${item['mod']} skipped - no price data")
                    continue
                prices[item['mod']] = math.ceil(sum(temp) / len(temp))


            except req.Timeout:
                print(f"${item['mod']} skipped - timeout")
            except ValueError:
                print(f"${item['mod']} skipped - response was not valid json")
            except req.RequestException as error:
                print(f"${item['mod']} skipped - req failed {error}")
            except Exception as error:
                print(f"${item['mod']} skipped - unexpected error: {error}")

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(prices, file, indent=4)
            print("all mod prices saved")

if __name__ == "__main__":
    getAllModPrices()