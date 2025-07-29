# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from nlp.goal_classifier import classify_goal
from protocol_generator.ruleset import generate_protocol

app = FastAPI()

class BrewRequest(BaseModel):
    bean_notes: str
    roast_level: str
    goal: str

class BrewResponse(BaseModel):
    flavour_goal: str
    protocol: dict
    description: str

@app.post("/brew", response_model=BrewResponse)
def get_brew_protocol(request: BrewRequest):
    # Classify the user input into structured goals
    classified_goal = classify_goal(request.goal)

    # Generate a brewing protocol from default recipes
    protocol = generate_protocol(
        bean_notes=request.bean_notes,
        roast_level=request.roast_level,
        goals=classified_goal
    )

    return BrewResponse(
        flavour_goal=classified_goal[0],
        protocol=protocol,
        description=protocol["description"]
    )

