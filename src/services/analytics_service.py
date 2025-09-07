from typing import List, Dict, Any
from src.data.bigquery_client import AnalyticsStore

analytics = AnalyticsStore()

class AnalyticsService:
    """
    Provides hotel analytics from BigQuery or local storage.
    """

    @staticmethod
    def get_events(event_type: str | None = None) -> List[Dict[str, Any]]:
        return analytics.query_events(event_type=event_type)

    @staticmethod
    def get_summary() -> Dict[str, Any]:
        events = analytics.query_events()
        total_orders = len([e for e in events if e["event_type"] == "food_order_created"])
        total_requests = len([e for e in events if e["event_type"] == "maintenance_request_created"])

        return {
            "total_food_orders": total_orders,
            "total_maintenance_requests": total_requests,
            "total_events": len(events),
        }
