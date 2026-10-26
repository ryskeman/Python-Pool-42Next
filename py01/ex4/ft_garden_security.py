#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float
    ) -> None:
        self._name: str = name
        self._growth_rate: float = growth_rate
        self._height: float = 0.0
        self._age: int = 0
        self.set_height(height, is_init=True)
        self.set_age(age, is_init=True)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float, is_init: bool = False) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            if not is_init:
                print("Height update rejected")
        else:
            self._height = height
            if not is_init:
                print(f"Height updated: {int(height)}cm")

    def set_age(self, age: int, is_init: bool = False) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            if not is_init:
                print("Age update rejected")
        else:
            self._age = age
            if not is_init:
                print(f"Age updated: {age} days")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("rose".capitalize(), 15.0, 10, 0.8)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-25.0)
    rose.set_age(-30)
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
