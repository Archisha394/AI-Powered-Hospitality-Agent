from typing import Dict, Any
from datetime import datetime
from src.data.bigquery_client import AnalyticsStore

analytics = AnalyticsStore()

class MaintenanceService:
    """
    Handles maintenance request business logic.
    """

    @staticmethod
    def create_request(issue: str, room: str) -> Dict[str, Any]:
        event = {
            "event_type": "maintenance_request_created",
            "session_id": f"room-{room}",
            "data": {"issue": issue, "room": room},
            "timestamp": datetime.utcnow().isoformat(),
        }
        analytics.log_event(event)

        return {
            "status": "success",
            "message": f"Maintenance request logged for room {room}: {issue}",
            "priority": "high",
        }
