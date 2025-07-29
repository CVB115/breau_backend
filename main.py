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
    classified_goal = classify_goal(request.goal)

    protocol = generate_protocol(
        request.bean_notes,
        request.roast_level,
        classified_goal
    )

    return BrewResponse(
        flavour_goal=classified_goal[0],
        protocol=protocol,
        description=protocol["description"]
    )
