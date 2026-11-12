#!/usr/bin/env python3
from alchemy.elements import create_earth
from alchemy.elements import create_air
from elements import create_fire
from elements import create_water


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{create_earth()}'"
        f" and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{create_fire()}'"
        f" and '{create_water()}'"
    )
