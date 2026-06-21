import json
from pathlib import Path

GALLERY_FILE = Path(__file__).with_name("galaxy_chart.json")
BACKUP_FILE = Path(__file__).with_name("galaxy_chart.json.bak")
SCENARIO_FILE = Path(__file__).with_name(".unique_scenario")
BACKUP_SCENARIO_FILE = SCENARIO_FILE.with_suffix(".unique_scenario.bak")

FIELDS_TO_SET = {
    "filling_name": "random_super_rich_planet",
    "chance_of_first_planet_bonus": 1.0,
    "chance_of_second_planet_bonus": 1.0,
    "chance_of_loot": 1.0,
    "has_artifact": True,
    "loot_level": 2,
}

EXCLUDED_CHILD_IDS = {2, 11, 12, 17, 18, 25, 26}

STARTING_TRACK_LEVELS = {
    "logistics": 5,
    "defense": 5,
    "commerce": 5,
    # "mining": 5,
    "research": 5,
}


def extract_player_zero_ids(data):
    for root_node in data.get("root_nodes", []):
        if root_node.get("id") == 0:
            return [
                child["id"]
                for child in root_node.get("child_nodes", [])
                if child.get("ownership", {}).get("player_index") == 0
            ]
    return []


def update_scenario_planets(planet_ids):
    if not SCENARIO_FILE.exists():
        raise FileNotFoundError(f"Could not find {SCENARIO_FILE}")

    with SCENARIO_FILE.open("r", encoding="utf-8") as f:
        scenario_data = json.load(f)

    scenario_data["planets"] = [
        {
            "gravity_well_id": planet_id,
            "starting_track_levels": STARTING_TRACK_LEVELS,
        }
        for planet_id in planet_ids
    ]

    SCENARIO_FILE.replace(BACKUP_SCENARIO_FILE)
    with SCENARIO_FILE.open("w", encoding="utf-8") as f:
        json.dump(scenario_data, f, indent=4, ensure_ascii=False)

    print(f"Updated {SCENARIO_FILE} with {len(planet_ids)} planets. Backup created at {BACKUP_SCENARIO_FILE}")


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

    planet_ids = extract_player_zero_ids(data)
    if planet_ids:
        update_scenario_planets(planet_ids)
    else:
        print("No player_index 0 child node IDs found in galaxy_chart.json; .unique_scenario was not updated.")


if __name__ == "__main__":
    main()
