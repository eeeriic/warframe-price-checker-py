import json

def get_filtered_items():
    with open("warframe market items en.txt", "r", encoding="utf-8") as f:
        data = json.load(f)

    info = data['payload']['items']

    from lists import warframes, companions, wf_arcanes, amp_arcanes, kit_arcanes, mel_arcanes, ope_arcanes, pri_arcanes, sec_arcanes, zaw_arcanes

    # --- Prime categorization ---
    prime_items = [item for item in info if "Prime" in item['item_name'] and "Primed" not in item['item_name']]
    sets = [item for item in prime_items if item['item_name'].endswith("Prime Set")]
    parts = [item for item in prime_items if not item['item_name'].endswith("Prime Set")]

    wf_parts = [item for item in parts if any(w + " Prime" in item['item_name'] for w in warframes)]
    wf_sets = [item for item in sets if any(w + " Prime Set" in item['item_name'] for w in warframes)]

    companion_parts = [item for item in parts if any(c + " Prime" in item['item_name'] for c in companions)]
    companion_sets = [item for item in sets if any(c + " Prime Set" in item['item_name'] for c in companions)]

    weapon_parts = [item for item in parts if item not in wf_parts + companion_parts]
    weapon_sets = [item for item in sets if item not in wf_sets + companion_sets]

    # --- Arcanes by category ---
    arcane_categories = {
        "wf_arcanes": wf_arcanes,
        "amp_arcanes": amp_arcanes,
        "kit_arcanes": kit_arcanes,
        "mel_arcanes": mel_arcanes,
        "ope_arcanes": ope_arcanes,
        "pri_arcanes": pri_arcanes,
        "sec_arcanes": sec_arcanes,
        "zaw_arcanes": zaw_arcanes
    }

    arcanes = {
        name: [item for item in info if item['item_name'] in arcane_list]
        for name, arcane_list in arcane_categories.items()
    }

    return {
        "wf_parts": wf_parts,
        "wf_sets": wf_sets,
        "companion_parts": companion_parts,
        "companion_sets": companion_sets,
        "weapon_parts": weapon_parts,
        "weapon_sets": weapon_sets,
        "arcanes": arcanes  # this is now a dict of categories
    }

