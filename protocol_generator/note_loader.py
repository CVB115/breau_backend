# protocol_generator/note_loader.py

import json
import os

def load_note_profiles():
    with open(os.path.join("data", "note_profiles.json"), "r", encoding="utf-8") as f:
        return json.load(f)

NOTE_PROFILE_PATH = os.path.join("data", "note_profiles.json")

with open(NOTE_PROFILE_PATH, "r", encoding="utf-8") as f:
    NOTE_PROFILES = json.load(f)

def get_note_profile(note_name: str) -> dict:
    key = note_name.strip().lower().replace(" ", "_")
    return NOTE_PROFILES.get(key, {})

def get_all_profiles(note_list: list) -> list:
    """Returns all profiles from the list of note names."""
    return [get_note_profile(n) for n in note_list if get_note_profile(n)]

def summarize_profiles(note_list: list) -> dict:
    """Summarizes the tags, volatility, and note types for goal matching."""
    tags = set()
    volatilities = []
    note_types = set()
    mouthfeel = set()
    overtraits = set()
    undertraits = set()

    for note in note_list:
        profile = get_note_profile(note)
        tags.update(profile.get("tags", []))
        note_types.add(profile.get("note_type", ""))
        mouthfeel.add(profile.get("mouthfeel_influence", ""))
        overtraits.update(profile.get("over_extracted_traits", []))
        undertraits.update(profile.get("under_extracted_traits", []))

        # Normalize volatility: can be string or float
        v = profile.get("volatility", "medium")
        if isinstance(v, str):
            v_map = {"low": 0.3, "medium": 0.6, "high": 0.9}
            v = v_map.get(v.lower(), 0.5)
        volatilities.append(v)

    return {
        "tags": list(tags),
        "note_types": list(note_types),
        "volatility_avg": round(sum(volatilities) / len(volatilities), 2) if volatilities else None,
        "mouthfeel_influences": list(mouthfeel),
        "over_extracted_traits": list(overtraits),
        "under_extracted_traits": list(undertraits)
    }

def match_goal_traits(goal: str, traits_summary: dict) -> dict:
    """Returns contextual flags to adjust brew based on user's goal and bean traits."""
    flags = {}

    if "body" in goal.lower():
        flags["emphasize_body"] = any(
            kw in traits_summary["mouthfeel_influences"][0].lower()
            for kw in ["thickness", "density", "coating", "rounded"]
        ) or "body" in traits_summary["tags"]

    if "floral" in goal.lower():
        flags["emphasize_aroma"] = "floral" in traits_summary["tags"] or traits_summary["volatility_avg"] >= 0.8

    if "clarity" in goal.lower():
        flags["avoid_astringent"] = "chalky" in traits_summary["over_extracted_traits"]
        flags["emphasize_top_note"] = "top-note" in traits_summary["tags"]

    if "reduce bitterness" in goal.lower():
        flags["avoid_bitter"] = any(x in traits_summary["over_extracted_traits"] for x in ["bitter", "chalky", "burnt"])

    if "syrupy" in goal.lower():
        flags["increase_contact_time"] = "jammy" in traits_summary["tags"] or "coating" in traits_summary["mouthfeel_influences"]

    return flags
