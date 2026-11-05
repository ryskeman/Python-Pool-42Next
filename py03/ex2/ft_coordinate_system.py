#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    # Pide a usuario coordenadas x, y , z
    while True:
        try:
            raw_input = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            )
            parts = raw_input.split(",")
            if len(parts) != 3:
                print("Invalid syntax")
                continue

            coords: list[float] = []
            has_error = False
            for part in parts:
                cleaned = part.strip()
                try:
                    coords.append(float(cleaned))
                except ValueError as e:
                    print(f"Error on parameter '{cleaned}': {e}")
                    has_error = True
                    break

            if not has_error:
                return (coords[0], coords[1], coords[2])

        except (KeyboardInterrupt, EOFError):
            print()
            return (0.0, 0.0, 0.0)


def calculate_distance(
    p1: tuple[float, float, float],
    p2: tuple[float, float, float]
) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    dist_center = calculate_distance((0.0, 0.0, 0.0), pos1)
    print(f"Distance to center: {round(dist_center, 4)}")
    print()

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    dist_between = calculate_distance(pos1, pos2)
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{round(dist_between, 4)}"
    )
    print()


if __name__ == "__main__":
    main()
