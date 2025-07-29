# protocol_generator/ruleset.py

import json
import os

# Load default recipes
with open(os.path.join("data", "default_recipes.json"), "r", encoding="utf-8") as f:
    DEFAULT_RECIPES = json.load(f)

def generate_protocol(bean_notes: str, roast_level: str, goals: list) -> dict:
    """
    Selects a brewing protocol based on user flavour goals.
    Falls back to a balanced default if no goal matches.
    """

    # Normalize input goals
    goals = [g.lower().strip() for g in goals]

    selected_recipe = None

    for goal in goals:
        if goal in DEFAULT_RECIPES:
            selected_recipe = DEFAULT_RECIPES[goal]
            break

    if not selected_recipe:
        # Fallback to balanced cup
        selected_recipe = DEFAULT_RECIPES.get("balance cup", {
            "temp": 92,
            "bloom_temp": 90,
            "ratio": "1:16",
            "bloom_ratio": "1:2.5",
            "agitation": "low",
            "pour_style": "pulse",
            "filter_flow": "medium",
            "grind_size": "medium",
            "contact_time": "medium",
            "total_pours": 3,
            "description": "A balanced cup across the board with no extremes. Useful as a default if no preference is set."
        })

    return selected_recipe
