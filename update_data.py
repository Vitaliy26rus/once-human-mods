mods_data = {
    "weapons": [
        {
            "name_en": "Assault Rifle",
            "name_ru": "Штурмовая винтовка",
            "mods": [
                {"name_en": "Extended Magazine", "name_ru": "Удлиненный магазин", "source": "Container A"},
                {"name_en": "Silencer", "name_ru": "Глушитель", "source": "Container B"}
            ]
        }
    ],
    "armor": [
        {
            "name_en": "Kevlar Vest",
            "name_ru": "Кевларовый жилет",
            "mods": [
                {"name_en": "Reinforced Plates", "name_ru": "Усиленные пластины", "source": "Container C"}
            ]
        }
    ],
    "containers": [
        {"id": "weapon_crate", "name": {"en": "Weapon Crate","ru": "Ящик с оружейными модами"}, "description": {"en": "Weapon mods container","ru": "Ящик с оружейными модами"}, "source": "..."},
        {"id": "gear_crate", "name": {"en": "Gear Crate","ru": "Ящик с модами брони"}, "description": {"en": "Armor mods container","ru": "Ящик с модами брони"}, "source": "..."}
    ],
    "sources": [
        {"mod_name_en": "Extended Magazine", "mod_name_ru": "Удлиненный магазин", "container": "Weapon Crate"},
        {"mod_name_en": "Silencer", "mod_name_ru": "Глушитель", "container": "Weapon Crate"}
    ]
}