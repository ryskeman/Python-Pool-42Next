#!/usr/bin/env python3
from ex3 import TransformCreatureFactory
from ex3.capability import TransformCapability


def main() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    base = factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())
    print()

    evolved = factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())
    print()


if __name__ == "__main__":
    main()
