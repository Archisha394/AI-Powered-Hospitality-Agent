from typing import Dict, Any
from datetime import datetime
from src.data.bigquery_client import AnalyticsStore

analytics = AnalyticsStore()

class FoodService:
    """
    Handles food ordering business logic.
    """

    @staticmethod
    def place_order(item: str, room: str) -> Dict[str, Any]:
        event = {
            "event_type": "food_order_created",
            "session_id": f"room-{room}",
            "data": {"item": item, "room": room},
            "timestamp": datetime.utcnow().isoformat(),
        }
        analytics.log_event(event)

        return {
            "status": "success",
            "message": f"Order placed: {item} for room {room}",
            "eta_minutes": 30,
        }
