# nlp/goal_classifier.py

def classify_goal(raw_goal: str) -> list:
    goal = raw_goal.lower()

    mappings = {
        "increase body": ["more body", "syrupy", "thicker", "stronger"],
        "reduce body": ["less body", "lighter", "watery"],
        "increase florality": ["more florality", "more floral", "jasmine", "flower", "lavender"],
        "reduce florality": ["less floral", "reduce florality"],
        "increase sweetness": ["sweeter", "more sweetness", "more sugar"],
        "reduce sweetness": ["less sweet", "less sugar"],
        "increase acidity": ["more acidity", "brighter", "more sour"],
        "reduce acidity": ["less acidity", "mellow", "less sour"],
        "increase clarity": ["clearer", "more clarity"],
        "reduce bitterness": ["less bitter", "reduce bitterness", "smoother"],
        "increase bitterness": ["more bitter", "darker", "bolder"]
    }

    classified = []

    for key, keywords in mappings.items():
        for word in keywords:
            if word in goal:
                classified.append(key)
                break  # Avoid duplicates for one match

    if not classified:
        classified.append("general balance")

    return classified
