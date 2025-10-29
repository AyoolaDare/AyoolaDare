"""
API endpoints for managing dispatches.
"""
from fastapi import APIRouter, HTTPException
from typing import Dict
import uuid
from app.models.schemas import Dispatch, DispatchCreate, Engineer
from app.services.dispatch.assignment_service import find_best_engineer

router = APIRouter()

# Mock database for dispatches
mock_dispatches_db: Dict[str, Dispatch] = {}

@router.post("/dispatches/", response_model=Dispatch)
async def create_dispatch(dispatch_create: DispatchCreate):
    """
    Create a new dispatch.
    This endpoint receives dispatch creation data, finds the best available
    engineer using the assignment service, and creates a dispatch record.
    """
    # In a real application, you'd fetch ATM details from a database
    mock_atm_location = (40.7128, -74.0060) # Mock New York City location

    # Find the best engineer for the job
    assigned_engineer_data = await find_best_engineer(
        atm_location=mock_atm_location,
        required_skill=dispatch_create.required_skill
    )

    if not assigned_engineer_data:
        raise HTTPException(status_code=404, detail="No available engineer found with the required skill.")

    # Create an Engineer model instance from the data
    assigned_engineer = Engineer(**assigned_engineer_data)

    # Generate a unique ID for the dispatch
    dispatch_id = str(uuid.uuid4())

    # Create the full Dispatch object
    new_dispatch = Dispatch(
        dispatch_id=dispatch_id,
        atm_id=dispatch_create.atm_id,
        description=dispatch_create.description,
        required_skill=dispatch_create.required_skill,
        engineer=assigned_engineer,
        status="Assigned"
    )

    # Save to our mock database
    mock_dispatches_db[dispatch_id] = new_dispatch

    return new_dispatch

@router.get("/dispatches/{dispatch_id}", response_model=Dispatch)
async def get_dispatch(dispatch_id: str):
    """
    Get the status of a specific dispatch.
    """
    dispatch = mock_dispatches_db.get(dispatch_id)
    if not dispatch:
        raise HTTPException(status_code=404, detail="Dispatch not found")
    return dispatch
