"""
Main FastAPI application for the ATM Smart Dispatch System.

This module initializes the FastAPI app, includes API routers,
and sets up middleware.
"""
from fastapi import FastAPI
from app.api.v1.endpoints import logs, dispatches, engineers
from app.jobs.scheduler import scheduler

app = FastAPI(title="ATM Smart Dispatch System")

# Include API routers
app.include_router(logs.router, prefix="/api/v1", tags=["logs"])
app.include_router(dispatches.router, prefix="/api/v1", tags=["dispatches"])
app.include_router(engineers.router, prefix="/api/v1", tags=["engineers"])

@app.on_event("startup")
async def startup_event():
    """
    Actions to perform on application startup.
    - Start the scheduler.
    """
    scheduler.start()

@app.on_event("shutdown")
async def shutdown_event():
    """
    Actions to perform on application shutdown.
    - Shutdown the scheduler.
    """
    scheduler.shutdown()

@app.get("/")
async def read_root():
    """
    Root endpoint for basic health checks.
    """
    return {"message": "Welcome to the ATM Smart Dispatch System"}
