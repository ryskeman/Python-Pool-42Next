#!/usr/bin/env python3
from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    lower_ingredients = ingredients.lower()
    if any(
        item in lower_ingredients for item in dark_spell_allowed_ingredients()
    ):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
