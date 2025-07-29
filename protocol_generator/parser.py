# protocol_generator/parser.py

def build_description(goals: list, temp: int, ratio: str, agitation: str) -> str:
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

    flavor_line = []
    for goal in goals:
        phrase = goal_phrases.get(goal, "")
        if phrase:
            flavor_line.append(phrase)

    flavor_sentence = "This brew targets " + ", ".join(flavor_line) + "."

    method_sentence = f"Use {temp}°C water, a brew ratio of {ratio}, and {agitation} agitation."

    return f"{flavor_sentence} {method_sentence}"
