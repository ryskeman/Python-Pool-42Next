#!/usr/bin/env python3
from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lower_ingredients = ingredients.lower()
    if any(
        item in lower_ingredients for item in light_spell_allowed_ingredients()
    ):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
