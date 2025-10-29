"""
Service for assigning engineers to dispatches.

This module contains the logic for matching engineers to ATMs based on
skills, location, and availability.
"""

# Mock data for demonstration purposes
mock_engineers = [
    {"id": "eng1", "name": "Alice", "skills": ["Cash Dispenser"], "location": (34.0522, -118.2437)},
    {"id": "eng2", "name": "Bob", "skills": ["Card Reader", "Receipt Printer"], "location": (36.1699, -115.1398)},
    {"id": "eng3", "name": "Charlie", "skills": ["Cash Dispenser", "Security Camera"], "location": (40.7128, -74.0060)},
]

async def find_best_engineer(atm_location: tuple, required_skill: str) -> dict:
    """
    Find the best engineer for a given ATM and required skill.

    In a real application, this would involve:
    - Querying a database of engineers.
    - Calculating travel times using a geocoding service.
    - Checking real-time availability.
    - Applying a more sophisticated matching algorithm.
    """
    # For now, we'll just find the first engineer with the required skill.
    for engineer in mock_engineers:
        if required_skill in engineer["skills"]:
            return engineer
    return None
