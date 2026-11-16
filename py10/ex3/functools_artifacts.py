#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    ops: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
        }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    enchanters: dict[str, Callable[[str], str]] = {
        "fire_enchant": functools.partial(base_enchantment, 50, "fire"),
        "ice_enchant": functools.partial(base_enchantment, 50, "ice"),
        "lightning_enchant": functools.partial(
            base_enchantment, 50, "lightning"
        ),
    }
    return enchanters


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def main() -> None:

    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    for n in (0, 1, 10, 15):
        print(f"Fib({n}): {memoized_fibonacci(n)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))

    print("\nTesting partial enchanter...")

    def base_enchant(power: int, element: str, target: str) -> str:
        return f"{element.capitalize()}, enchantment ({power}) on {target}"

    enchants = partial_enchanter(base_enchant)
    print(enchants["fire_enchant"]('Sword'))


if __name__ == "__main__":
    main()
