import json
import requests as req
import math

def getAllWarframeSetPrices():
    with open("./3filterItems/filtered_data.json", "r", encoding="utf-8") as file:
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

        with open("5Prices/warframes/warframe_sets_prices.json", "w", encoding="utf-8") as file:
            json.dump(prices, file, indent=4)
            print("all items saved")

getAllWarframeSetPrices()