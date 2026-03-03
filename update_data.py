import requests
from bs4 import BeautifulSoup
import json, re

weapon_url = "https://game8.co/games/Once-Human/archives/468371"
armor_url  = "https://game8.co/games/Once-Human/archives/468372"
suffixes_url = "https://game8.co/games/Once-Human/archives/460076"

def parse_table(table):
    rows = table.find_all("tr")
    headers = [th.get_text().strip() for th in rows[0].find_all("th")]
    data = []
    for row in rows[1:]:
        cells = row.find_all(["td","th"])
        if len(cells) != len(headers): continue
        data.append({h: c.get_text().strip() for h,c in zip(headers,cells)})
    return data

def fetch_mods(url, category):
    html = requests.get(url).text
    soup = BeautifulSoup(html,"html.parser")
    table = soup.find("table")
    if not table: return []
    rows = parse_table(table)
    mods = []
    for r in rows:
        name = r.get("Mod", r.get("Image","")).strip()
        tier = r.get("Tier","").split()
        effect = r.get("Core Effect","")
        if not name: continue
        mods.append({
            "id": re.sub(r"[^0-9a-z]","_",name.lower()),
            "name":{"en":name,"ru":name},
            "category":category,
            "tier":tier,
            "slots":["all_weapons"] if category=="weapon" else ["mask","torso","bottoms"],
            "effect":{"en":effect,"ru":effect},
            "containers":["weapon_crate"] if category=="weapon" else ["gear_crate"],
            "source":url
        })
    return mods

def fetch_suffixes(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html,"html.parser")
    table = soup.find("table")
    if not table: return []
    rows = parse_table(table)
    suffixes = []
    for r in rows:
        name = r.get("Suffix","").strip()
        type_en = r.get("Effect","").strip()
        if not name: continue
        effect_base = {
            "common": r.get("Common",""),
            "uncommon": r.get("Uncommon",""),
            "rare": r.get("Rare",""),
            "epic": r.get("Epic",""),
            "legendary": r.get("Legendary","")
        }
        suffixes.append({
            "id": re.sub(r"[^0-9a-z]","_",name.lower()),
            "name":{"en":name,"ru":name},
            "type_en":type_en,
            "type_ru":type_en,
            "effect_base":effect_base,
            "source":url
        })
    return suffixes

weapon_mods = fetch_mods(weapon_url,"weapon")
armor_mods  = fetch_mods(armor_url,"armor")
suffixes    = fetch_suffixes(suffixes_url)

data = {
    "meta":{"game":"Once Human","languages":["en","ru"],"sources":[weapon_url,armor_url,suffixes_url]},
    "containers":[
        {"id":"weapon_crate","name":{"en":"Weapon Crate","ru":"Ящик с оружейными модами"},"description":{"en":"Weapon mods container","ru":"Ящик с оружейными модами"},"source":weapon_url},
        {"id":"gear_crate","name":{"en":"Gear Crate","ru":"Ящик с модами брони"},"description":{"en":"Armor mods container","ru":"Ящик с модами брони"},"source":armor_url}
    ],
    "mods":weapon_mods+armor_mods,
    "suffixes":suffixes
}

with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)

print(f"Updated: {len(weapon_mods)} weapon mods, {len(armor_mods)} armor mods, {len(suffixes)} suffixes")