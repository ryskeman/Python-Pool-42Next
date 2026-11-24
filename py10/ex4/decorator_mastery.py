#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any
from functools import wraps
import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(
    min_power: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power: int | float
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = next(
                    (
                        a for a in args if isinstance(a, (int, float))
                        and not isinstance(a, bool)
                    ),
                    0,
                )
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(
    max_attempts: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and all(c.isalpha() or c.isspace() for c in name)
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting power validator...")

    @power_validator(min_power=20)
    def arcane_blast(target: str, power: int) -> str:
        return f"Arcane blast hits {target} with {power} power"

    print(arcane_blast("Dragon", 25))
    print(arcane_blast("Dragon", 10))

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise RuntimeError("Spell destabilized")

    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def resilient_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(resilient_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
