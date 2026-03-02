import json

def filter_items():
    with open("../2filterData/all_items.json", "r") as file:
        data = json.load(file)

        primes = [i for i in data if "prime" in i["tags"] and "mod" not in i["tags"]] # warfarmes, weapons and companions
        arcanes = [i for i in data if "arcane_enhancement" in i["tags"] and "mod" not in i["tags"]] # arcanes
        mods = [i for i in data if "mod" in i["tags"]] # mods

        #---

        wf = [i for i in primes if "warframe" in i["tags"]]
        weapons = [i for i in primes if "weapon" in i["tags"]]
        companions = [i for i in primes if "sentinel" in i["tags"]]

        #---

        wf_sets = [i["slug"] for i in wf if "set" in i["tags"]]
        wf_parts = [i["slug"] for i in wf if "blueprint" in i["tags"]]

        weapon_sets = [i["slug"] for i in weapons if "set" in i["tags"]]
        weapon_parts = [i["slug"] for i in weapons if "blueprint" in i["tags"]]

        companion_sets = [i["slug"] for i in companions if "set" in i["tags"]]
        companion_parts = [i["slug"] for i in companions if "blueprint" in i["tags"]]

        filtered_data = {
            "wf_sets": wf_sets,
            "wf_parts": wf_parts,
            "weapon_sets": weapon_sets,
            "weapon_parts": weapon_parts,
            "companion_sets": companion_sets,
            "companion_parts": companion_parts
        }

        with open("filtered_data.json", "w") as file:
            json.dump(filtered_data, file, indent=4)

filter_items()