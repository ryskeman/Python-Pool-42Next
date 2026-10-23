#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.heigth: int = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.heigth}cm, {self.age} days old")


def main() -> None:
    plant1 = Plant("rose", 25, 30)
    plant2 = Plant("sunflower", 80, 45)
    plant3 = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()
