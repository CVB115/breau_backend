# protocol_generator/parser.py

from nlp.semantic_matcher import match_flavour_goal
from protocol_generator.note_loader import load_note_profiles

# Load note profiles once on import
NOTE_PROFILES = load_note_profiles()


def build_description(goals: list, temp: int, ratio: str, agitation: str) -> str:
    """
    Builds a readable description string for the user based on the goal and brew parameters.
    """
    goal_phrases = {
        "increase body": "a syrupy mouthfeel and stronger presence",
        "reduce body": "a lighter and more tea-like cup",
        "increase florality": "elevated floral notes like jasmine or lavender",
        "reduce florality": "muted flower-like characteristics",
        "increase sweetness": "a sweeter and more rounded cup",
        "reduce sweetness": "less sugar-like perception",
        "increase acidity": "bright and vibrant acidity",
        "reduce acidity": "a more mellow and soft acidity",
        "reduce bitterness": "less bitterness for a smoother taste",
        "increase bitterness": "a punchy, bold bitter finish",
        "increase clarity": "a cleaner, more transparent cup",
        "general balance": "a well-rounded flavor balance"
    }

    flavor_line = [
        phrase for goal in goals if (phrase := goal_phrases.get(goal))
    ]

    flavor_sentence = "This brew targets " + ", ".join(flavor_line) + "." if flavor_line else ""
    method_sentence = f"Use {temp}°C water, a brew ratio of {ratio}, and {agitation} agitation."

    return f"{flavor_sentence} {method_sentence}".strip()


def parse_user_input(raw_input: str, bean_notes: list = []) -> dict:
    """
    Uses NLP to extract interpreted flavour goals from user text input,
    and validates the bean notes against the known note profiles.

    Args:
        raw_input (str): The user input describing their desired outcome.
        bean_notes (list): List of notes from the coffee bag (e.g., ["red_grape", "cranberry"]).

    Returns:
        dict: {
            "goals": list of parsed goal strings,
            "matched_notes": list of validated notes found in note_profiles
        }
    """
    # Step 1: Interpret goals from user's natural language
    interpreted_goals = match_flavour_goal(raw_input)

    # Ensure always returns a list even if NLP fails
    if isinstance(interpreted_goals, str):
        interpreted_goals = [interpreted_goals]

    # Step 2: Validate user-provided bean notes
    matched_notes = [note for note in bean_notes if note in NOTE_PROFILES]

    return {
        "goals": interpreted_goals,
        "matched_notes": matched_notes
    }
