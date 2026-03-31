import json
from pathlib import Path

def filter_items():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    input_file = project_root / "filterData" / "all_items.json"
    output_file = project_root / "filterItems" / "filtered_data.json"
    
    with open(input_file, "r") as file:
        data = json.load(file)

        items_by_slug = {i["slug"]: i for i in data}

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

        def get_thumb_for_slug(slug):
            """Prefer i18n.en thumbnail path for lists; fall back to icon when missing."""
            item = items_by_slug.get(slug, {})
            en = (item.get("i18n") or {}).get("en", {})
            return en.get("thumb") or en.get("icon") or item.get("thumb") or item.get("icon")

        wf_dict = {}
        for slug in wf_sets:
            name = extract_base_name(slug)
            parts = get_parts_for_item(name, wf_parts)
            wf_dict[name] = {
                "set_img": get_thumb_for_slug(slug),
                "set": slug,
                "parts": parts
            }

        weapons_dict = {}
        for slug in weapon_sets:
            name = extract_base_name(slug)
            parts = get_parts_for_item(name, weapon_parts)
            weapons_dict[name] = {
                "set_img": get_thumb_for_slug(slug),
                "set": slug,
                "parts": parts
            }

        companions_dict = {}
        for slug in companion_sets:
            name = extract_base_name(slug)
            parts = get_parts_for_item(name, companion_parts)
            companions_dict[name] = {
                "set_img": get_thumb_for_slug(slug),
                "set": slug,
                "parts": parts
            }

        #---

        arcanes_dict = {}
        for i in arcanes:
            slug = i['slug']
            rank = i['maxRank']
            arcanes_dict[slug] = {
                "img": get_thumb_for_slug(slug),
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
                "img": get_thumb_for_slug(slug),
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

        with open(output_file, "w") as file:
            json.dump(filtered_data, file, indent=4)

        

if __name__ == "__main__":
    filter_items()