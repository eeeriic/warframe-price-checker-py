import json
import requests as req
import math

def getAllModPrices():
    with open("./3filterItems/filtered_data.json", "r", encoding="utf-8") as file:
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
                print(f"${item['mod']} done")


            except req.Timeout:
                print(f"${item['mod']} skipped - timeout")
            except ValueError:
                print(f"${item['mod']} skipped - response was not valid json")
            except req.RequestException as error:
                print(f"${item['mod']} skipped - req failed {error}")
            except Exception as error:
                print(f"${item['mod']} skipped - unexpected error: {error}")

        with open("5Prices/mods/mod_prices.json", "w", encoding="utf-8") as file:
            json.dump(prices, file, indent=4)
            print("all items saved")

getAllModPrices()