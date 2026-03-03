import json

def getWeaponPrices():
    with open("../../3filterItems/filtered_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)["weapon"]
        