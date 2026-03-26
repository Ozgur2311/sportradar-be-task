from typing import Optional
from pydantic import BaseModel, field_validator


class LeagueCreate(BaseModel):
    name: str
    sport_id: int

    # Make sure league name is not empty
    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("League name cannot be empty")
        return value

    # Make sure sport_id is positive
    @field_validator("sport_id")
    @classmethod
    def validate_sport_id(cls, value):
        if value <= 0:
            raise ValueError("sport_id must be greater than 0")
        return value


class TeamCreate(BaseModel):
    name: str
    sport_id: int
    city: Optional[str] = None
    country: Optional[str] = None

    # Make sure team name is not empty
    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Team name cannot be empty")
        return value

    # Make sure sport_id is positive
    @field_validator("sport_id")
    @classmethod
    def validate_sport_id(cls, value):
        if value <= 0:
            raise ValueError("sport_id must be greater than 0")
        return value

   
class VenueCreate(BaseModel):
    name: str
    city: Optional[str] = None
    country: Optional[str] = None

    # Make sure venue name is not empty
    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Venue name cannot be empty")
        return value