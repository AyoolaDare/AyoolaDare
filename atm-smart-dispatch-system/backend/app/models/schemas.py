"""
Pydantic schemas for data validation and serialization.
"""
from pydantic import BaseModel, Field
from typing import List, Tuple, Dict, Any
from datetime import datetime

class Asset(BaseModel):
    """
    Represents an ATM asset.
    """
    atm_id: str = Field(..., description="The unique identifier for the ATM.")
    location: Tuple[float, float] = Field(..., description="The latitude and longitude of the ATM.")
    status: str = Field(..., description="The current status of the ATM (e.g., Online, Offline, Error).")
    cash_level: int = Field(..., description="The current cash level percentage.")

class Log(BaseModel):
    """
    Represents a log entry from an ATM.
    """
    atm_id: str = Field(..., description="The ID of the ATM that generated the log.")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="The timestamp of the log event.")
    event_type: str = Field(..., description="The type of event (e.g., StatusUpdate, Error, Transaction).")
    details: Dict[str, Any] = Field(..., description="A dictionary containing event-specific details.")

class Engineer(BaseModel):
    """
    Represents a service engineer.
    """
    engineer_id: str = Field(..., description="The unique identifier for the engineer.")
    name: str = Field(..., description="The name of the engineer.")
    skills: List[str] = Field(..., description="A list of the engineer's skills.")
    location: Tuple[float, float] = Field(..., description="The current latitude and longitude of the engineer.")
    is_available: bool = Field(True, description="Indicates if the engineer is available for dispatch.")

class DispatchBase(BaseModel):
    """
    Base model for a dispatch.
    """
    atm_id: str = Field(..., description="The ID of the ATM requiring service.")
    description: str = Field(..., description="A description of the issue requiring dispatch.")
    required_skill: str = Field(..., description="The skill required to resolve the issue.")

class DispatchCreate(DispatchBase):
    """
    Model for creating a new dispatch.
    """
    pass

class Dispatch(DispatchBase):
    """
    Represents a dispatch assignment.
    """
    dispatch_id: str = Field(..., description="The unique identifier for the dispatch.")
    engineer: Engineer | None = Field(None, description="The engineer assigned to the dispatch.")
    status: str = Field("Created", description="The status of the dispatch (e.g., Created, InProgress, Completed).")
