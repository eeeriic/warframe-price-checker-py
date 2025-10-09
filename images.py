import requests
import os
from lists import wf_arcanes, amp_arcanes, kit_arcanes, mel_arcanes, ope_arcanes, pri_arcanes, sec_arcanes, zaw_arcanes

arcanes = (wf_arcanes + amp_arcanes + kit_arcanes + mel_arcanes +
          ope_arcanes + pri_arcanes + sec_arcanes + zaw_arcanes)


def download_image(item, category, base_folder="img"):
    folder = os.path.join(base_folder, category)
    os.makedirs(folder, exist_ok=True)

    thumb_url = "https://warframe.market/static/assets/" + item["thumb"]
    filename = os.path.basename(item["thumb"])
    save_path = os.path.join(folder, filename)

    if os.path.exists(save_path):
        print(f"Already exists: {category}/{filename}")
        return

    response = requests.get(thumb_url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"Saved: {category}/{filename}")
    else:
        print(f"Failed to download {category}/{filename}: status {response.status_code}")
