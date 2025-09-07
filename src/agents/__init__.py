from fastapi import APIRouter, Query
from typing import Optional
from src.services.analytics_service import AnalyticsService

router = APIRouter()

@router.get("/analytics/events")
def get_events(event_type: Optional[str] = Query(None, description="Filter by event type")):
    return AnalyticsService.get_events(event_type=event_type)

@router.get("/analytics/summary")
def get_summary():
    return AnalyticsService.get_summary()
