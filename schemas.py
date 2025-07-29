# schemas.py

from pydantic import BaseModel
from typing import Optional

class BrewProtocol(BaseModel):
    temp: int
    bloom_temp: Optional[int]
    ratio: str
    bloom_ratio: Optional[str]
    agitation: str
    pour_style: Optional[str]
    filter_flow: Optional[str]
    grind_size: Optional[str]
    contact_time: Optional[str]
    total_pours: Optional[int]
    description: str

class BrewRequest(BaseModel):
    bean_notes: str
    roast_level: str
    goal: str

class BrewResponse(BaseModel):
    flavour_goal: str
    protocol: BrewProtocol
    description: str
