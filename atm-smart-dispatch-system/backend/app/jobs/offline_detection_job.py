"""
Scheduled job for detecting offline ATMs.

This job runs periodically to check for ATMs that have not sent a
heartbeat recently.
"""
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def detect_offline_atms():
    """
    Check for offline ATMs and create alerts.
    """
    logger.info("Running offline ATM detection job...")
    # In a real application, this would:
    # 1. Query Elasticsearch for the last heartbeat of each ATM.
    # 2. Compare the timestamp with the current time.
    # 3. If an ATM is offline, create an alert.
    # For now, we'll just log a message.
    logger.info("Offline ATM detection job complete.")
