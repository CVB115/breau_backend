# protocol_generator/goal_matcher.py

import json
import os
from collections import defaultdict

# Load default recipes
with open(os.path.join("data", "default_recipes.json"), "r", encoding="utf-8") as f:
    DEFAULT_RECIPES = json.load(f)

# Each recipe is tagged with goal-related attributes manually
# Define a mapping of flavour goals → weight tags
GOAL_TAG_WEIGHTS = {
    "increase body": {"body", "syrupy", "heavy"},
    "syrupy body": {"syrupy", "thick", "heavy"},
    "increase florality": {"floral", "delicate", "aromatic"},
    "reduce bitterness": {"bitterness", "astringent", "dry"},
    "increase sweetness": {"sweet", "fruit-forward", "candied"},
    "winey profile": {"grape", "winey", "ferment", "boozy"},
    "caramelized": {"caramel", "jammy", "sweet", "cooked fruit"},
    "balance cup": {"balanced", "round", "approachable"}
}

def score_recipe_against_goals(goals: list[str]) -> dict:
    """
    Score each recipe based on overlap between goal tags and recipe tags.
    Returns a dictionary mapping recipe name → score.
    """
    goal_tags = set()
    for goal in goals:
        for tag_set in GOAL_TAG_WEIGHTS.values():
            for tag in tag_set:
                if tag in goal.lower():
                    goal_tags.add(tag)

    scores = defaultdict(int)

    for recipe_name, tags in GOAL_TAG_WEIGHTS.items():
        match_score = len(goal_tags.intersection(tags))
        if match_score > 0:
            scores[recipe_name] = match_score

    return dict(scores)

def get_best_matching_recipe(goals: list[str]) -> dict:
    """
    Returns the most appropriate brewing recipe based on composite goals.
    Falls back to 'balance cup' if no match.
    """
    scores = score_recipe_against_goals(goals)

    if not scores:
        return DEFAULT_RECIPES.get("balance cup", {})

    # Choose the recipe with the highest score
    best_recipe = max(scores, key=scores.get)
    return DEFAULT_RECIPES.get(best_recipe, {})
