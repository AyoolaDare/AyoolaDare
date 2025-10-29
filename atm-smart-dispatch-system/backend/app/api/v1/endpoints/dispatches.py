"""
API endpoints for managing dispatches.
"""
from fastapi import APIRouter

router = APIRouter()

@router.post("/dispatches/")
async def create_dispatch():
    """
    Create a new dispatch.
    """
    # In a real application, this would trigger the assignment_service
    # to find the best engineer.
    return {"status": "Dispatch created"}

@router.get("/dispatches/{dispatch_id}")
async def get_dispatch(dispatch_id: str):
    """
    Get the status of a specific dispatch.
    """
    return {"id": dispatch_id, "status": "In progress"}
