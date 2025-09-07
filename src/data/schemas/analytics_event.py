from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class AnalyticsEvent(BaseModel):
    event_type: str
    session_id: str
    data: Dict[str, Any]
    timestamp: Optional[str] = datetime.utcnow().isoformat()
