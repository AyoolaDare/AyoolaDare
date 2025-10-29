"""
API endpoints for ingesting and querying ATM logs.
"""
from fastapi import APIRouter, Depends
from elasticsearch import AsyncElasticsearch
from app.services.elasticsearch.es_client import get_es_client

router = APIRouter()

@router.post("/logs/")
async def create_log(
    log: dict,
    es_client: AsyncElasticsearch = Depends(get_es_client)
):
    """
    Ingest a new ATM log.
    """
    # In a real application, you would validate the log format
    # with a Pydantic model.
    response = await es_client.index(index="atm_logs", document=log)
    return {"status": "Log received", "id": response["_id"]}

@router.get("/logs/{atm_id}")
async def get_logs(
    atm_id: str,
    es_client: AsyncElasticsearch = Depends(get_es_client)
):
    """
    Get logs for a specific ATM.
    """
    # This is a simplified query. In a real application, you would add
    # pagination, sorting, and filtering.
    response = await es_client.search(
        index="atm_logs",
        body={"query": {"match": {"atm_id": atm_id}}}
    )
    return [hit["_source"] for hit in response["hits"]["hits"]]
