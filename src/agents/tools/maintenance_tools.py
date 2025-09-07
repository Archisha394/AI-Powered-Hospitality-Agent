from loguru import logger
from typing import Dict, Any

async def create_maintenance_request(params: Dict[str, Any]) -> Dict[str, Any]:
    issue = params.get("issue")
    room = params.get("room")
    logger.info(f"Creating maintenance request: {issue} in room {room}")
    return {
        "status": "success",
        "message": f"A maintenance technician has been dispatched for room {room} ({issue})."
    }
