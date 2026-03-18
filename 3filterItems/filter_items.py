import json

def filter_items():
    with open("./2filterData/all_items.json", "r") as file:
        data = json.load(file)

        primes = [i for i in data if "prime" in i["tags"] and "mod" not in i["tags"]] # warfarmes, weapons and companions
        arcanes = [i for i in data if "arcane_enhancement" in i["tags"] and "mod" not in i["tags"]] # arcanes
        mods = [i for i in data if "mod" in i["tags"] and any(r in i["tags"] for r in ["legendary"])] # mods

        #---

        wf = [i for i in primes if "warframe" in i["tags"]]
        weapons = [i for i in primes if "weapon" in i["tags"] and "sentinel" not in i["tags"]]
        # companions = [i for i in primes if "sentinel" in i["tags"]]

        #---

        wf_sets = [i["slug"] for i in wf if "set" in i["tags"]]
        wf_parts = [i["slug"] for i in wf if "blueprint" in i["tags"]]

        weapon_sets = [i["slug"] for i in weapons if "set" in i["tags"]]
        weapon_parts = [i["slug"] for i in weapons if any(tag in ["component", "blueprint"] for tag in i["tags"])]

        companion_sets = [i["slug"] for i in primes if "sentinel" in i["tags"] and i["slug"].endswith("_set")]
        companion_parts = [i["slug"] for i in primes if i["slug"].endswith(("systems", "carapace", "blueprint", "cerebrum"))]
        
        #---

        def extract_base_name(slug):
            """Extract base name from set slug (e.g., 'frost_prime_set' -> 'frost')"""
            return slug.replace("_prime_set", "")

        def get_parts_for_item(name, parts_list):
            """Get all blueprint parts for a given base name"""
            return [p for p in parts_list if p.startswith(name + "_prime_")]

        wf_dict = {}
        for slug in wf_sets:
            name = extract_base_name(slug)
            parts = get_parts_for_item(name, wf_parts)
            wf_dict[name] = {
                "set": slug,
                "parts": parts
            }

        weapons_dict = {}
        for slug in weapon_sets:
            name = extract_base_name(slug)
            parts = get_parts_for_item(name, weapon_parts)
            weapons_dict[name] = {
                "set": slug,
                "parts": parts
            }

        companions_dict = {}
        for slug in companion_sets:
            name = extract_base_name(slug)
            parts = get_parts_for_item(name, companion_parts)
            companions_dict[name] = {
                "set": slug,
                "parts": parts
            }

        #---

        arcanes_dict = {}
        for i in arcanes:
            slug = i['slug']
            rank = i['maxRank']
            arcanes_dict[slug] = {
                "arcane": slug,
                "rank": rank
            }

        #---

        mods_dict = {}
        for i in mods:
            slug = i['slug']
            if 'maxRank' not in i:
                print(f"Mod '{slug}' is missing 'maxRank'")
                continue
            rank = i['maxRank']
            mods_dict[slug] = {
                "mod": slug,
                "rank": rank
            }


        #---

        filtered_data = {
            "warframe": wf_dict,
            "weapons": weapons_dict,
            "companions": companions_dict,
            "arcanes": arcanes_dict,
            "mods": mods_dict
        }

        with open("3filterItems/filtered_data.json", "w") as file:
            json.dump(filtered_data, file, indent=4)

        

filter_items()