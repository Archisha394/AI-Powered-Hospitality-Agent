# agents/core.py
from adk import LlmAgent
from adk.llms import GeminiModel
from adk.tools import Tool

# Configure Gemini Flash
gemini_flash = GeminiModel(
    name="gemini-2.5-flash",
    project="your-gcp-project-id",   # set via env too
    location="us-central1",          # choose region supported
)

FoodOrderingAgent = LlmAgent(
    name="FoodOrderingAgent",
    llm=gemini_flash,
    system_prompt="""You are the hotel's food ordering agent. Validate room number,
    check menu items, confirm quantities, and call the API tool to place orders.
    Always return JSON with 'items', 'subtotal', 'status'.""",
    tools=[api_call]
)

ServiceRequestAgent = LlmAgent(
    name="ServiceRequestAgent",
    llm=gemini_flash,
    system_prompt="""You triage service requests (maintenance, amenities, etc.).
    Classify into type, assign priority, then call the API to log the request.""",
    tools=[api_call]
)

AnalyticsAgent = LlmAgent(
    name="AnalyticsAgent",
    llm=gemini_flash,
    system_prompt="""You generate structured KPIs for managers. Query BigQuery using
    bq_query. Respond ONLY in JSON with fields revenue, occupancy, guest_feedback.""",
    tools=[bq_query]
)
