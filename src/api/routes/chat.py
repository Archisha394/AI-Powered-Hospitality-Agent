from fastapi import APIRouter, Depends
from src.api.models.chat_models import ChatRequest, ChatResponse
from src.agent.adk_client import ADKClient
from src.agent.session_manager import SessionManager
from src.agent.prompts.base_prompt import BASE_SYSTEM_PROMPT
from src.agent.tools.food_tools import place_food_order
from src.agent.tools.maintenance_tools import create_maintenance_request
from src.services.food_service import FoodService
from src.services.maintenance_service import MaintenanceService

router = APIRouter()
adk = ADKClient()
sessions = SessionManager()

# Wrap services with tools
async def place_food_order_tool(params):
    result = FoodService.place_order(params.get("item"), params.get("room"))
    return {"reply": result["message"], "data": result}

async def maintenance_tool(params):
    result = MaintenanceService.create_request(params.get("issue"), params.get("room"))
    return {"reply": result["message"], "data": result}


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    sessions.add_message(request.session_id, "user", request.message)

    tools = [place_food_order_tool, maintenance_tool]
    response = await adk.generate_response(
        request.session_id,
        request.message,
        tools,
        system_prompt=BASE_SYSTEM_PROMPT,
    )

    reply = response.get("reply", "")
    data = response if "reply" in response else None
    sessions.add_message(request.session_id, "assistant", reply)

    return ChatResponse(reply=reply, data=data)
