"""
API endpoints for managing engineers.
"""
from fastapi import APIRouter
from typing import List
from app.models.schemas import Engineer

router = APIRouter()

# Mock database of engineers
mock_engineers_db = {
    "eng1": {"engineer_id": "eng1", "name": "Alice", "skills": ["Cash Dispenser"], "location": (34.0522, -118.2437), "is_available": True},
    "eng2": {"engineer_id": "eng2", "name": "Bob", "skills": ["Card Reader", "Receipt Printer"], "location": (36.1699, -115.1398), "is_available": True},
}

@router.post("/engineers/", response_model=Engineer)
async def create_engineer(engineer: Engineer):
    """
    Add a new engineer to the system.
    In a real system, this would be saved to a persistent database.
    """
    mock_engineers_db[engineer.engineer_id] = engineer.model_dump()
    return engineer

@router.get("/engineers/", response_model=List[Engineer])
async def get_all_engineers():
    """
    Get a list of all engineers.
    """
    return list(mock_engineers_db.values())

@router.get("/engineers/{engineer_id}", response_model=Engineer)
async def get_engineer(engineer_id: str):
    """
    Get information about a specific engineer.
    """
    engineer = mock_engineers_db.get(engineer_id)
    if not engineer:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Engineer not found")
    return engineer
