from loguru import logger
from typing import List, Callable, Dict, Any

class ADKClient:
    """
    Stubbed Google ADK/Gemini orchestrator client.
    Replace `generate_response` with real ADK calls if needed.
    """

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key
        logger.info("ADKClient initialized (stub mode)")

    async def generate_response(
        self,
        session_id: str,
        message: str,
        tools: List[Callable],
        system_prompt: str = "You are a hotel assistant."
    ) -> Dict[str, Any]:
        """
        Simulate an LLM multi-agent response.
        For demo: route by keyword (pizza → food tool, light → maintenance).
        """

        logger.debug(f"[ADK Stub] Session={session_id}, Msg={message}")

        if "pizza" in message.lower():
            for tool in tools:
                if tool.__name__ == "place_food_order":
                    return await tool({"item": "pizza", "room": "120"})
        if "light" in message.lower():
            for tool in tools:
                if tool.__name__ == "create_maintenance_request":
                    return await tool({"issue": "Light not working", "room": "305"})

        return {"reply": f"(Stub) Received your message: {message}"}
