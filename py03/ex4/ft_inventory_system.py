#!/usr/bin/env python3
import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in args:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item = parts[0]
        qty_str = parts[1]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            qty = int(qty_str)
            inventory[item] = qty
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")

    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for item, qty in inventory.items():
        percent = (qty / total_qty) * 100
        print(f"Item {item} represents {percent:.1f}%")

    most_item = max(inventory, key=lambda k: inventory[k])
    least_item = min(inventory, key=lambda k: inventory[k])
    print(
        f"Item most abundant: {most_item}"
        f" with quantity {inventory[most_item]}"
    )
    print(
        f"Item least abundant: {least_item}"
        f" with quantity {inventory[least_item]}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
