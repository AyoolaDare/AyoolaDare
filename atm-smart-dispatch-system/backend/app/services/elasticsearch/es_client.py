"""
Elasticsearch client configuration and management.

This module provides an asynchronous client for interacting with Elasticsearch.
"""
from elasticsearch import AsyncElasticsearch
from app.config import settings

# Global Elasticsearch client instance
es_client = AsyncElasticsearch(
    hosts=[settings.ELASTICSEARCH_URL],
    # Add authentication if needed, e.g., http_auth=(settings.ES_USER, settings.ES_PASSWORD)
)

async def get_es_client() -> AsyncElasticsearch:
    """
    Dependency to get the Elasticsearch client.
    """
    return es_client

async def close_es_client():
    """
    Close the Elasticsearch client connection.
    """
    await es_client.close()
