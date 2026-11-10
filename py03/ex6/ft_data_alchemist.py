#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()

    players = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]

    all_cap = [name.capitalize() for name in players]
    cap_only = [name for name in players if name[0].isupper()]

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_cap}")
    print(f"New list of capitalized names only: {cap_only}")
    print()

    score_dict = {name: random.randint(1, 1000) for name in all_cap}
    average = sum(score_dict.values()) / len(score_dict)

    high_scores = {
        name: score for name, score in score_dict.items() if score > average
    }

    print(f"Score dict: {score_dict}")
    print(f"Score average is {average:.2f}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
