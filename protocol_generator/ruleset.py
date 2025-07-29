# protocol_generator/ruleset.py
from .parser import build_description

def generate_protocol(bean_notes: str, roast_level: str, goals: list) -> dict:
    # Defaults
    temp = 92
    ratio = "1:16"
    agitation = "medium"
    description = []

    for goal in goals:
        if goal == "increase body":
            temp += 2
            ratio = "1:15"
            agitation = "high"
            description.append("Increase temperature, reduce ratio, and increase agitation to build body.")
        
        elif goal == "reduce body":
            temp -= 1
            ratio = "1:17"
            agitation = "low"
            description.append("Reduce strength by using a higher ratio and lower agitation.")

        elif goal == "increase florality":
            temp = min(temp, 91)
            ratio = "1:17"
            agitation = "low"
            description.append("Use lower temperature and gentle flow to enhance florals.")

        elif goal == "reduce bitterness":
            temp -= 1
            agitation = "gentle"
            description.append("Lower temperature and reduce agitation to reduce bitterness.")

        elif goal == "increase sweetness":
            temp = 92
            agitation = "medium"
            ratio = "1:16"
            description.append("Balance extraction to emphasize sweetness.")

        elif goal == "increase acidity":
            temp -= 1
            ratio = "1:17"
            agitation = "low"
            description.append("Slightly lower temperature and higher ratio increase acidity.")

        elif goal == "reduce acidity":
            temp += 1
            ratio = "1:15"
            agitation = "medium"
            description.append("Raise temperature and lower ratio to mute acidity.")

        elif goal == "increase clarity":
            ratio = "1:17"
            agitation = "light"
            description.append("Clarity improves with higher ratio and minimal agitation.")

    return {
        "temp": temp,
        "ratio": ratio,
        "agitation": agitation,
        "description": build_description(goals, temp, ratio, agitation)
    }

