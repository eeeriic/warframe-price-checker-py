import json
import requests as req

url = "https://api.warframe.market/v2/"

def get_items(): # get all items
    try:
        res = req.get(f"{url}items") # calling the api
        res.raise_for_status() # raise error
        data = res.json()

        with open("1getData/raw_all_items.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            print("all items saved")

    except req.Timeout:
        print("timeout")
    except ValueError:
        print("response was not valid json")
    except req.RequestException as error:
        print(f"req failed {error}")

get_items()
    