import copy
import json
from pathlib import Path

GALLERY_FILE = Path(__file__).with_name("galaxy_chart.json")
BACKUP_FILE = Path(__file__).with_name("galaxy_chart.json.bak")
SCENARIO_FILE = Path(__file__).with_name(".unique_scenario")
BACKUP_SCENARIO_FILE = SCENARIO_FILE.with_suffix(".unique_scenario.bak")

FIELDS_TO_SET = {
    "filling_name": "magnetic_planet_lilly",
    "chance_of_first_planet_bonus": 1.0,
    "chance_of_second_planet_bonus": 1.0,
    "chance_of_loot": 1.0,
    "has_artifact": True,
    "loot_level": 2,
}

EXCLUDED_CHILD_IDS = {2, 11, 12, 17, 18, 25, 26}

# 50 안먹힘
STARTING_TRACK_LEVELS = {
    "surveying": 5,
    "logistics": 5,
    "defense": 5,
    "commerce": 5,
    "mining": 5,
    "research": 5,
}
starting_units_to_any_player_and_gravity_well_EXCLUDED=[2]

starting_units_to_any_player_and_gravity_well=        {
            "faction_allowed": "dlc_trader_loyalist",
            "faction_spawn_units": [
                {
                    "player_index": 0,
                    "gravity_well_id": 2,
                    "spawn_units": {
                        "required_units": [
                            # {
                            #     "unit": "trader_frigate_factory_structure",
                            #     "count": [
                            #         1,
                            #         1
                            #     ]
                            # },
                            # {
                            #     "unit": "trader_capital_ship_factory_structure",
                            #     "count": [
                            #         1,
                            #         1
                            #     ]
                            # },
                            # {
                            #     "unit": "trader_loyalist_titan_factory_structure",
                            #     "count": [
                            #         1,
                            #         1
                            #     ]
                            # },
                            {
                                "unit": "trader_civilian_research_lab_structure",
                                "count": [
                                    10,
                                    10
                                ]
                            },
                            {
                                "unit": "trader_military_research_lab_structure",
                                "count": [
                                    10,
                                    10
                                ]
                            },
                            {
                                "unit": "trader_population_structure",
                                "count": [
                                    10,
                                    10
                                ]
                            },
                            {
                                "unit": "trader_trade_port_structure",
                                "count": [
                                    10,
                                    10
                                ]
                            },
                            {
                                "unit": "trader_culture_center_structure",# 문화
                                "count": [
                                    10,
                                    10
                                ]
                            },
                            {
                                "unit": "trader_exotic_factory_structure",
                                "count": [
                                    10,
                                    10
                                ]
                            },
                            # {
                            #     "unit": "trader_starbase",
                            #     "count": [
                            #         10,
                            #         10
                            #     ],
                            #     "options": {
                            #         "items": [
                            #     "trader_starbase_structural_integrity_0", 
                            #     "trader_starbase_flak_field", 
                            #     "trader_starbase_docking_booms", 
                            #     "trader_starbase_unlock_torpedo_weapon", 
                            #     "trader_starbase_stun_torpedo", 
                            #     "trader_starbase_unlock_beam_weapon", 
                            #     "trader_starbase_hangar_0", 
                            #     "trader_starbase_planetary_shield_array"
                            #         ]
                            #     }
                            # },
                            # {
                            #     "unit": "trader_phase_jump_inhibitor_structure", # 억제
                            #     "count": [
                            #         10,
                            #         10
                            #     ]
                            # },
                            # {
                            #     "unit": "trader_retrofit_bay_structure", # 개조
                            #     "count": [
                            #         10,
                            #         10
                            #     ]
                            # },
                            # {
                            #     "unit": "trader_gauss_defense_structure",
                            #     "count": [
                            #         10,
                            #         10
                            #     ]
                            # },
                            # {
                            #     "unit": "trader_hangar_defense_structure",
                            #     "count": [
                            #         10,
                            #         10
                            #     ]
                            # },
                            # {
                            #     "unit": "trader_autocannon_defense_structure",
                            #     "count": [
                            #         10,
                            #         10
                            #     ]
                            # },
                            {
                                "unit": "trader_metal_extractor_structure",
                                "count": [
                                    10,
                                    10
                                ]
                            },
                            {
                                "unit": "trader_crystal_extractor_structure",
                                "count": [
                                    10,
                                    10
                                ]
                            }

                        ]
                    },
                }
            ]
        }

starting_units_to_any_player_and_gravity_well_int=    [
        {
            "faction_allowed": "dlc_trader_loyalist",
            "faction_spawn_units": [
            {
                "player_index": 0,
                "gravity_well_id": 2,
                "spawn_units": {
                    "required_units":[
                    {
                        "unit": "trader_frigate_factory_structure",
                        "count": [25, 25]
                    },
                    {
                        "unit": "trader_capital_ship_factory_structure",
                        "count": [25, 25]
                    },
                    {
                        "unit": "trader_population_structure",
                        "count": [25, 25]
                    },
                    {
                        "unit": "trader_trade_port_structure",
                        "count": [25, 25]
                    },
                    {
                        "unit": "trader_loyalist_titan_factory_structure",
                        "count": [1, 1]
                    },
                    {
                        "unit": "trader_starbase",
                        "count": [9, 9],
                        "options": {
                            "items": [
                                
                                "trader_starbase_structural_integrity_0", 
                                "trader_starbase_flak_field", 
                                "trader_starbase_docking_booms", 
                                "trader_starbase_unlock_torpedo_weapon", 
                                "trader_starbase_stun_torpedo", 
                                "trader_starbase_unlock_beam_weapon", 
                                "trader_starbase_hangar_0", 
                                "trader_starbase_planetary_shield_array"
                            ]
                        }
                    },
                    {
                        "unit": "trader_starbase",
                        "count": [9, 9],
                        "options": {
                            "items": [
                                
                                "trader_starbase_structural_integrity_0", 
                                "trader_starbase_flak_field", 
                                "trader_starbase_docking_booms", 
                                "trader_starbase_unlock_torpedo_weapon", 
                                "trader_starbase_stun_torpedo", 
                                "trader_starbase_unlock_beam_weapon", 
                                "trader_starbase_hangar_0", 
                                "trader_starbase_trade_port"
                            ]
                        }
                    },
                    {
                        "unit": "trader_starbase",
                        "count": [9, 9],
                        "options": {
                            "items": [
                                
                                "trader_starbase_structural_integrity_0", 
                                "trader_starbase_flak_field", 
                                "trader_starbase_docking_booms", 
                                "trader_starbase_unlock_torpedo_weapon", 
                                "trader_starbase_stun_torpedo", 
                                "trader_starbase_unlock_beam_weapon", 
                                "trader_starbase_hangar_0", 
                                "trader_starbase_command_center"
                            ]
                        }
                    },
                    {
                        "unit": "trader_starbase",
                        "count": [9, 9],
                        "options": {
                            "items": [
                                
                                "trader_starbase_structural_integrity_0", 
                                "trader_starbase_flak_field", 
                                "trader_starbase_docking_booms", 
                                "trader_starbase_unlock_torpedo_weapon", 
                                "trader_starbase_stun_torpedo", 
                                "trader_starbase_unlock_beam_weapon", 
                                "trader_starbase_hangar_0", 
                                "trader_starbase_factory_support"
                            ]
                        }
                    },
                    {
                        "unit": "trader_phase_jump_inhibitor_structure",
                        "count": [36, 36]
                    },
                    {
                        "unit": "trader_hangar_defense_structure",
                        "count": [36, 36]
                    },
                    {
                        "unit": "trader_retrofit_bay_structure",
                        "count": [36, 36]
                    },
                    {
                        "unit": "trader_gauss_defense_structure",
                        "count": [36, 36]
                    }
                    ]
                },
                "spawn_units_in_formation": [
                {
                    "required_units": [
                    {
                        "unit": "trader_loyalist_titan",
                        "count": [1, 1],
                        "options": {
                            "items": [
                                "trader_loyalist_titan_hangar",
                                "trader_loyalist_titan_unlock_missile_weapon",
                                "trader_loyalist_titan_unlock_beam_weapon",
                                "trader_missile_guidance_computer",
                                "trader_rapid_autoloader",
                                "trader_targeting_array"
                            ]
                        }
                    },
                    {
                        "unit": "dlc2_trader_loyalist_super_capital_ship",
                        "count": [1, 1],
                        "options": {
                            "items": [
                                "dlc2_trader_loyalist_super_capital_ship_unlock_missile_weapon",
                                "trader_missile_guidance_computer",
                                "trader_rapid_autoloader",
                                "trader_reserve_squadron_hangar",
                                "trader_targeting_array"
                            ]
                        }
                    },
                    {
                        "unit": "trader_battle_capital_ship",
                        "count": [7, 7],
                        "options": {
                            "items": [
                                "trader_heavy_gauss_slugs",
                                "trader_missile_guidance_computer",
                                "trader_rapid_autoloader",
                                "trader_targeting_array"
                            ]
                        }
                    },
                    {
                        "unit": "trader_colony_capital_ship",
                        "count": [7, 7],
                        "options": {
                            "items": [
                                "trader_reserve_squadron_hangar",
                                "trader_missile_guidance_computer",
                                "trader_rapid_autoloader",
                                "trader_targeting_array"
                            ]
                        }
                    },
                    {
                        "unit": "trader_support_capital_ship",
                        "count": [7, 7],
                        "options": {
                            "items": [
                                "trader_reserve_squadron_hangar",
                                "trader_missile_guidance_computer",
                                "trader_rapid_autoloader",
                                "trader_targeting_array"
                            ]
                        }
                    },
                    {
                        "unit": "trader_carrier_capital_ship",
                        "count": [7, 7],
                        "options": {
                            "items": [
                                "trader_reserve_squadron_hangar",
                                "trader_missile_guidance_computer",
                                "trader_rapid_autoloader",
                                "trader_targeting_array"
                            ]
                        }
                    },
                    {
                        "unit": "trader_siege_capital_ship",
                        "count": [7, 7],
                        "options": {
                            "items": [
                                "trader_heavy_gauss_slugs",
                                "trader_missile_guidance_computer",
                                "trader_rapid_autoloader",
                                "trader_targeting_array"
                            ]
                        }
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                },
                {
                    "required_units": [
                    {
                        "unit": "trader_autocannon_defense_structure",
                        "count": [6, 6]
                    }]
                }]
            }]
        },
    ]
def build_starting_units_list(planet_ids):
    units = copy.deepcopy(starting_units_to_any_player_and_gravity_well_int)

    for planet_id in planet_ids:
        if planet_id in starting_units_to_any_player_and_gravity_well_EXCLUDED:
            continue
        else:
            entry = copy.deepcopy(starting_units_to_any_player_and_gravity_well)
        entry["faction_spawn_units"][0]["gravity_well_id"] = planet_id
        units.append(entry)
    return units


def extract_player_zero_ids(data):
    for root_node in data.get("root_nodes", []):
        if root_node.get("id") == 0:
            return [
                child["id"]
                for child in root_node.get("child_nodes", [])
                if child.get("ownership", {}).get("player_index") == 0
            ]
    return []


def update_scenario_data(scenario_data, planet_ids):
    scenario_data["planets"] = [
        {
            "gravity_well_id": planet_id,
            "starting_track_levels": STARTING_TRACK_LEVELS,
        }
        for planet_id in planet_ids
    ]

    scenario_data["starting_units_to_any_player_and_gravity_well"] = build_starting_units_list(planet_ids)


def main() -> None:
    if not GALLERY_FILE.exists():
        raise FileNotFoundError(f"Could not find {GALLERY_FILE}")

    with GALLERY_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # Create a backup before modifying the file.
    with BACKUP_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    root_nodes = data.get("root_nodes", [])
    updated = False

    for root_node in root_nodes:
        if root_node.get("id") == 0:
            for child in root_node.get("child_nodes", []):
                if child.get("id") in EXCLUDED_CHILD_IDS:
                    continue
                for field, value in FIELDS_TO_SET.items():
                    child[field] = value
                updated = True
            break

    if not updated:
        print("No child_nodes updated. Root node with id 0 was not found or had no child_nodes.")
        return

    with GALLERY_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Updated galaxy_chart.json and created backup at {BACKUP_FILE}")

    if not SCENARIO_FILE.exists():
        raise FileNotFoundError(f"Could not find {SCENARIO_FILE}")

    with SCENARIO_FILE.open("r", encoding="utf-8") as f:
        scenario_data = json.load(f)

    planet_ids = extract_player_zero_ids(data)
    update_scenario_data(scenario_data, planet_ids)

    SCENARIO_FILE.replace(BACKUP_SCENARIO_FILE)
    with SCENARIO_FILE.open("w", encoding="utf-8") as f:
        json.dump(scenario_data, f, indent=4, ensure_ascii=False)

    print(f"Updated {SCENARIO_FILE} and created backup at {BACKUP_SCENARIO_FILE}")


if __name__ == "__main__":
    main()
