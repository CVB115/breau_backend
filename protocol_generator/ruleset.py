# protocol_generator/ruleset.py

import json
import os
from protocol_generator.note_loader import load_note_profiles
from protocol_generator.goal_matcher import get_best_matching_recipe

# Load note profiles
note_profiles = load_note_profiles()

def extract_relevant_notes(bean_notes: list[str]) -> list[str]:
    """
    Extracts flavour notes from the bean's tasting notes
    based on matches in the note_profiles dictionary.
    """
    matched = []
    lower_notes = [note.lower() for note in bean_notes]
    for note in note_profiles:
        if note.lower() in lower_notes:
            matched.append(note)
    return matched

def generate_protocol(bean_notes: list[str], roast_level: str, goals: list[str]) -> dict:
    """
    Generates a brewing protocol based on user's flavour goals
    and bean tasting notes. Now uses modular goal matching logic.
    """
    # Ensure everything is lowercase and clean
    cleaned_goals = [g.lower().strip() for g in goals]
    matched_notes = extract_relevant_notes(bean_notes)

    # [Optional] - Print debug info (disable in production)
    # print("Matched Notes:", matched_notes)
    # print("Goals:", cleaned_goals)

    # Call goal matcher
    protocol = get_best_matching_recipe(cleaned_goals)

    return protocol
