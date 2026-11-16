#!/usr/bin/env python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(
        mages: list[dict[str, Any]], min_power: int
        ) -> list[dict[str, Any]]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_p = max(mages, key=lambda m: m["power"])["power"]
    min_p = min(mages, key=lambda m: m["power"])["power"]
    avg_p = round(sum(map(lambda m: m["power"], mages)) / len(mages), 2)
    return {"max_power": max_p, "min_power": min_p, "avg_power": avg_p}


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "Orb"},
        {"name": "Fire Staff", "power": 92, "type": "Staff"}
    ]

    print()
    print("Testing artifact sorter...")
    sorted_arts = artifact_sorter(artifacts)
    print(
        f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']}"
        " power) comes before "
        f"{sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)"
    )

    print("\nTesting spell transformer...")
    transformed = spell_transformer(["fireball", "heal", "shield"])
    print(" ".join(transformed))

    mages = [
        {"name": "Gandalf", "power": 95, "element": "light"},
        {"name": "Merlin", "power": 80, "element": "arcane"},
        {"name": "Morgana", "power": 60, "element": "shadow"},
    ]

    print("\nTesting power filter...")
    print(power_filter(mages, 80))
    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
