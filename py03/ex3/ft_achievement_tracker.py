#!/usr/bin/env python3
import random


ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind"
]


def gen_player_achievements() -> set[str]:
    count = random.randint(5, 9)
    selected = random.sample(ACHIEVEMENTS, k=count)
    return set(selected)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    total_pool = set(ACHIEVEMENTS)

    all_distinct = alice.union(bob, charlie, dylan)

    common = alice.intersection(bob, charlie, dylan)

    only_alice = alice.difference(bob, charlie, dylan)
    only_bob = bob.difference(alice, charlie, dylan)
    only_charlie = charlie.difference(alice, bob, dylan)
    only_dylan = dylan.difference(alice, bob, charlie)

    alice_missing = total_pool.difference(alice)
    bob_missing = total_pool.difference(bob)
    charlie_missing = total_pool.difference(charlie)
    dylan_missing = total_pool.difference(dylan)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distinct achievements: {all_distinct}")
    print()
    print(f"Common achievements: {common}")
    print()
    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")
    print()
    print(f"Alice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}")
    print()


if __name__ == "__main__":
    main()
