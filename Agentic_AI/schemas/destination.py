from pydantic import BaseModel


class DestinationRecommendation(BaseModel):
    city: str
    state: str
    country: str
    reason: str
    best_time: str
    estimated_budget: str
    highlights: list[str]