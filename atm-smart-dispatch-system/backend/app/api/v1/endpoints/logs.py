"""
API endpoints for ingesting and querying ATM logs.
"""
from fastapi import APIRouter, Depends, Body
from elasticsearch import AsyncElasticsearch
from typing import List
from app.services.elasticsearch.es_client import get_es_client
from app.models.schemas import Log

router = APIRouter()

@router.post("/logs/", response_model=Log)
async def create_log(
    log: Log,
    es_client: AsyncElasticsearch = Depends(get_es_client)
):
    """
    Ingest a new ATM log.
    The log data is validated against the Log schema.
    """
    # Convert Pydantic model to dict for Elasticsearch
    log_dict = log.model_dump()
    # Elasticsearch expects a string for datetime
    log_dict["timestamp"] = log.timestamp.isoformat()

    response = await es_client.index(index="atm_logs", document=log_dict)

    # Return the original log object, as it's already validated
    return log

@router.get("/logs/{atm_id}", response_model=List[Log])
async def get_logs(
    atm_id: str,
    es_client: AsyncElasticsearch = Depends(get_es_client)
) -> List[Log]:
    """
    Get logs for a specific ATM.
    """
    # A more robust query for a real application
    search_body = {
        "query": {
            "match": {
                "atm_id.keyword": atm_id  # Assuming atm_id is mapped as a keyword
            }
        },
        "sort": [
            {"timestamp": "desc"}
        ],
        "size": 100 # Add pagination
    }

    response = await es_client.search(
        index="atm_logs",
        body=search_body
    )

    # Parse the results into Log models
    logs = [Log(**hit["_source"]) for hit in response["hits"]["hits"]]
    return logs
