# protocol_generator/ruleset.py

import json
import os

# Load default recipes from JSON file
with open(os.path.join("data", "default_recipes.json"), "r", encoding="utf-8") as f:
    DEFAULT_RECIPES = json.load(f)

def generate_protocol(bean_notes: str, roast_level: str, goals: list) -> dict:
    """
    Selects a brewing protocol based on the user's flavour goals.
    Falls back to the 'balance cup' recipe from the JSON if no goal matches.
    """

    # Normalize goals
    goals = [g.lower().strip() for g in goals]

    # Try to find a matching recipe
    selected_recipe = None
    for goal in goals:
        if goal in DEFAULT_RECIPES:
            selected_recipe = DEFAULT_RECIPES[goal]
            break

    # Fallback to 'balance cup' from JSON
    if not selected_recipe:
        selected_recipe = DEFAULT_RECIPES.get("balance cup")
        if not selected_recipe:
            raise ValueError("No fallback 'balance cup' recipe found in default_recipes.json")

    return selected_recipe

