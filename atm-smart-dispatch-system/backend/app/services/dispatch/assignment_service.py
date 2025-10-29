"""
Service for assigning engineers to dispatches.

This module contains the logic for matching engineers to ATMs based on
skills, location, and availability.
"""
from app.models.schemas import Engineer
from typing import Dict, Any

# Mock data for demonstration purposes, now aligned with the Engineer schema
mock_engineers = [
    Engineer(engineer_id="eng1", name="Alice", skills=["Cash Dispenser"], location=(34.0522, -118.2437), is_available=True),
    Engineer(engineer_id="eng2", name="Bob", skills=["Card Reader", "Receipt Printer"], location=(36.1699, -115.1398), is_available=True),
    Engineer(engineer_id="eng3", name="Charlie", skills=["Cash Dispenser", "Security Camera"], location=(40.7128, -74.0060), is_available=False),
    Engineer(engineer_id="eng4", name="Diana", skills=["Cash Dispenser"], location=(41.8781, -87.6298), is_available=True), # Chicago
]

async def find_best_engineer(atm_location: tuple, required_skill: str) -> Dict[str, Any]:
    """
    Find the best engineer for a given ATM and required skill.

    This mock implementation iterates through available engineers and finds the
    first one who has the required skill. A real implementation would be more
    complex, involving geo-distance calculations and workload balancing.
    """

    # Find all available engineers with the required skill
    suitable_engineers = [
        eng for eng in mock_engineers
        if eng.is_available and required_skill in eng.skills
    ]

    # In a real system, you would calculate the distance from the ATM to each engineer
    # and pick the closest one. For now, we return the first one found.
    if suitable_engineers:
        # Return the engineer's data as a dictionary
        return suitable_engineers[0].model_dump()

    return None
