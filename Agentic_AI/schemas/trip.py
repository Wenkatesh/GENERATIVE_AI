from pydantic import BaseModel, Field


class TripRequest(BaseModel):
    source: str = Field(..., description="Starting location")
    destination_type: str = Field(..., description="Beach, Hill Station, Heritage, etc.")
    budget: str = Field(..., description="Low, Medium, High")
    duration: int = Field(..., description="Trip duration in days")
    interests: list[str] = Field(default_factory=list)