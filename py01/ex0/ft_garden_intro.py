#!/usr/bin/env python3

def garden_intro(name: str, height: str, age: str) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name.capitalize()}")
    print(f"Height: {height}")
    print(f"Age: {age}")
    print("=== End of Program ===")


def main() -> None:
    name: str = "rose"
    height: str = "25cm"
    age: str = "30 days"
    garden_intro(name, height, age)


if __name__ == "__main__":
    main()
