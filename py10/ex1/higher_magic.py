#!/usr/bin/env python3
from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str],
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def power_bolt(target: str, power: int) -> str:
        return f"{power}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon", 10)
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    mega_bolt = power_amplifier(power_bolt, 3)
    orig = power_bolt("Dragon", 10)
    amp = mega_bolt("Dragon", 10)
    print(f"Original: {orig}, Amplified: {amp}")

    print("\nTesting conditional caster...")
    strong_fireball = conditional_caster(
        lambda _, power: power >= 15, fireball
    )

    print(f"Low power: {strong_fireball('Dragon', 10)}")
    print(f"High power: {strong_fireball('Dragon', 20)}")

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal])
    print(f"Sequence result: {combo('Dragon', 10)}")


if __name__ == "__main__":
    main()
