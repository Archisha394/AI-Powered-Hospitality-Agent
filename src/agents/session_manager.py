from typing import Dict, Any
from loguru import logger

class SessionManager:
    """
    In-memory session manager for hotel guests.
    Keeps track of conversation state per session_id.
    """

    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}

    def get_session(self, session_id: str) -> Dict[str, Any]:
        if session_id not in self.sessions:
            logger.info(f"Creating new session {session_id}")
            self.sessions[session_id] = {"history": []}
        return self.sessions[session_id]

    def add_message(self, session_id: str, role: str, content: str):
        session = self.get_session(session_id)
        session["history"].append({"role": role, "content": content})

    def get_history(self, session_id: str) -> list[Dict[str, str]]:
        return self.get_session(session_id)["history"]
