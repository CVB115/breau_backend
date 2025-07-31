from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from protocol_generator import parser, ruleset

app = FastAPI()


class BrewRequest(BaseModel):
    goal: str
    bean_notes: List[str]  # Corrected type
    roast_level: str


class BrewResponse(BaseModel):
    goals: List[str]
    matched_notes: List[str]
    protocol: dict
    description: str


@app.post("/brew", response_model=BrewResponse)
def get_brew_protocol(request: BrewRequest):
    # Step 1: Interpret user goal and match bean notes
    parsed = parser.parse_user_input(request.goal, request.bean_notes)

    # Step 2: Generate brewing protocol
    protocol = ruleset.generate_protocol(
        bean_notes=parsed["matched_notes"],
        roast_level=request.roast_level,
        goals=parsed["goals"]
    )

    # Step 3: Generate human-readable description
    description = parser.build_description(
        goals=parsed["goals"],
        temp=protocol["temp"],
        ratio=protocol["ratio"],
        agitation=protocol["agitation"]
    )

    return BrewResponse(
        goals=parsed["goals"],
        matched_notes=parsed["matched_notes"],
        protocol=protocol,
        description=description
    )
