import requests
import requests_cache

session = requests_cache.CachedSession('warframe_cache', backend='sqlite', expire_after=3600)

def get_average_price(item_name):
    url_name = item_name.lower().replace(" ", "_")
    url = f"https://api.warframe.market/v1/items/{url_name}/orders"
    response = session.get(url)

    if response.status_code == 200:
        data = response.json()
        sell_orders = [
            order["platinum"] for order in data["payload"]["orders"]
            if order["order_type"] == "sell"
            and order["user"]["status"] in ["online", "ingame"]
            and order["platinum"] > 2
            and order["user"]["platform"] == "pc" # only pc orders
        ]

        # sort prices and take the values in range
        sell_orders = sorted(sell_orders)[2:8]

        # return the average of these prices if available
        return round(sum(sell_orders) / len(sell_orders)) if sell_orders else None
    else:
        print(f"Failed to fetch price for {item_name}")
        return None

def get_average_price_arcane(item_name, mod_rank=5):
    url_name = item_name.lower().replace(" ", "_")
    url = f"https://api.warframe.market/v1/items/{url_name}/orders"
    response = session.get(url)

    if response.status_code == 200:
        data = response.json()
        sell_orders = [
            order["platinum"] for order in data["payload"]["orders"]
            if order["order_type"] == "sell"
            and order["user"]["status"] in ["online", "ingame"]
            and order["user"]["platform"] == "pc"
            and order.get("mod_rank") == mod_rank
            and order["platinum"] > 2
        ]

        # take middle range to avoid extreme outliers
        sell_orders = sorted(sell_orders)[2:8]

        return round(sum(sell_orders) / len(sell_orders)) if sell_orders else None
    else:
        print(f"Failed to fetch price for {item_name}")
        return None

