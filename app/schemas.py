from datetime import datetime
from pydantic import BaseModel, field_validator


# Expected format when user add new event
class EventCreate(BaseModel):
    title: str
    event_date: str
    event_time: str
    description: str
    league_id: int
    home_team_id: int
    away_team_id: int
    venue_id: int

    # Make sure title is not empty
    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        return value

    # Make sure date format is YYYY-MM-DD
    @field_validator("event_date")
    @classmethod
    def validate_event_date(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("event_date must be in YYYY-MM-DD format")
        return value

    # Make sure time format is HH:MM
    @field_validator("event_time")
    @classmethod
    def validate_event_time(cls, value):
        try:
            datetime.strptime(value, "%H:%M")
        except ValueError:
            raise ValueError("event_time must be in HH:MM format")
        return value

    # Make sure IDs are positive
    @field_validator("league_id", "home_team_id", "away_team_id", "venue_id")
    @classmethod
    def validate_positive_ids(cls, value):
        if value <= 0:
            raise ValueError("IDs must be greater than 0")
        return value