from loguru import logger
from typing import Dict, Any

async def place_food_order(params: Dict[str, Any]) -> Dict[str, Any]:
    item = params.get("item")
    room = params.get("room")
    logger.info(f"Placing food order: {item} for room {room}")
    return {
        "status": "success",
        "message": f"Your {item} will be delivered shortly to room {room}."
    }
