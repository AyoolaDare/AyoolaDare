"""
APScheduler setup for running background jobs.
"""
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.jobs.offline_detection_job import detect_offline_atms

scheduler = AsyncIOScheduler()

# Schedule the offline detection job to run every 5 minutes
scheduler.add_job(detect_offline_atms, "interval", minutes=5)
