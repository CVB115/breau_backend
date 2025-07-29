from fastapi import FastAPI
from pydantic import BaseModel
from nlp.semantic_matcher import match_flavour_goal  # ✅ USE MODEL NOW
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
    flavour_goal = match_flavour_goal(request.goal)  # previously used classify_goal

    protocol = generate_protocol(
        request.bean_notes,
        request.roast_level,
        [flavour_goal]  # protocol expects a list
    )

    return BrewResponse(
        flavour_goal=flavour_goal,
        protocol=protocol,
        description=protocol["description"]
    )

    print(f"User goal: {request.goal} → Matched: {flavour_goal}")

