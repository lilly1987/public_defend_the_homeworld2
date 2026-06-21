import json
from pathlib import Path

GALLERY_FILE = Path(__file__).with_name("galaxy_chart.json")
BACKUP_FILE = Path(__file__).with_name("galaxy_chart.json.bak")

FIELDS_TO_SET = {
    "filling_name": "random_super_rich_planet",
    "chance_of_first_planet_bonus": 1.0,
    "chance_of_second_planet_bonus": 1.0,
    "chance_of_loot": 1.0,
    "has_artifact": True,
    "loot_level": 2,
}

EXCLUDED_CHILD_IDS = {2,11, 12, 17, 18, 25, 26}


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


if __name__ == "__main__":
    main()
