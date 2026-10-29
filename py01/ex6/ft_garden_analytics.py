#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def log_grow(self) -> None:
            self._grow_count += 1

        def log_age(self) -> None:
            self._age_count += 1

        def log_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.8
    ) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._growth_rate: float = growth_rate
        self._stats: Plant._Stats = self._Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)

    def get_name(self) -> str:
        return self._name

    def show(self) -> None:
        self._stats.log_show()
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._stats.log_grow()
        self._height = round(self._height + self._growth_rate, 1)

    def age(self, age: int = 1) -> None:
        self._stats.log_age()
        self._age += age

    def display_stats(self) -> None:
        self._stats.display()


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        growth_rate: float = 0.8
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def log_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
        growth_rate: float = 0.8
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter: float = trunk_diameter
        self._stats: Tree._TreeStats = self._TreeStats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self._stats.log_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide."
        )


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seed_count: int,
        growth_rate: float = 0.8
    ) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self._seed_count: int = seed_count

    def show(self) -> None:
        super().show()
        count = self._seed_count if self._bloomed else 0
        print(f"Seeds: {count}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_stats()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower("rose".capitalize(), 15.0, 10, "red", 8.0)
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("oak".capitalize(), 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("sunflower".capitalize(), 80.0, 45, "yellow", 42, 30.0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)
    print()

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_plant_stats(anon)
    print()


if __name__ == "__main__":
    main()
