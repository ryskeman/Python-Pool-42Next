#!/usr/bin/env python3
from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    InvalidStrategyError
)


Opponent = tuple[CreatureFactory, BattleStrategy]


def run_tournament(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_1, strategy_1 = opponents[i]
            factory_2, strategy_2 = opponents[j]
            c1 = factory_1.create_base()
            c2 = factory_2.create_base()
            print()
            print("* Battle *")
            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")
            try:
                strategy_1.act(c1)
                strategy_2.act(c2)
            except InvalidStrategyError as err:
                print(f"Battle error, aborting tournament: {err}")
                return


def main() -> None:
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]")
    run_tournament([(flame_factory, normal), (transform_factory, aggressive)])

    print()
    print("Tournament 1 (error)")
    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    run_tournament(
        [(transform_factory, aggressive), (flame_factory, aggressive)]
    )


if __name__ == "__main__":
    main()
