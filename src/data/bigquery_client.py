import json
from pathlib import Path
from typing import Dict, Any, List
from loguru import logger
from google.cloud import bigquery
from src.config.settings import get_settings

settings = get_settings()
LOCAL_FILE = Path(__file__).parent / "analytics_local.json"


class AnalyticsStore:
    """
    Writes analytics events to BigQuery if credentials/env are set.
    Otherwise falls back to local JSON.
    """

    def __init__(self):
        self.use_bigquery = (
            settings.GCP_PROJECT_ID
            and settings.BIGQUERY_DATASET
            and settings.BIGQUERY_TABLE_ANALYTICS
        )
        if self.use_bigquery:
            self.client = bigquery.Client(project=settings.GCP_PROJECT_ID)
            self.table = f"{settings.GCP_PROJECT_ID}.{settings.BIGQUERY_DATASET}.{settings.BIGQUERY_TABLE_ANALYTICS}"
            logger.info(f"AnalyticsStore using BigQuery table {self.table}")
        else:
            logger.warning("BigQuery not configured → Using local JSON store")

    def log_event(self, event: Dict[str, Any]):
        if self.use_bigquery:
            errors = self.client.insert_rows_json(self.table, [event])
            if errors:
                logger.error(f"BigQuery insert failed: {errors}")
        else:
            self._log_local(event)

    def _log_local(self, event: Dict[str, Any]):
        events: List[Dict[str, Any]] = []
        if LOCAL_FILE.exists():
            events = json.loads(LOCAL_FILE.read_text())
        events.append(event)
        LOCAL_FILE.write_text(json.dumps(events, indent=2))
        logger.debug(f"Event logged locally: {event}")

    def query_events(self, event_type: str | None = None) -> List[Dict[str, Any]]:
        if self.use_bigquery:
            query = f"SELECT * FROM `{self.table}`"
            if event_type:
                query += f" WHERE event_type='{event_type}'"
            results = self.client.query(query).result()
            return [dict(row) for row in results]
        else:
            if LOCAL_FILE.exists():
                events = json.loads(LOCAL_FILE.read_text())
                if event_type:
                    return [e for e in events if e.get("event_type") == event_type]
                return events
            return []
