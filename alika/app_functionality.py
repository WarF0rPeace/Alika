from .api.api_service import APIService
from typing import Dict, Optional

class AppFunctionality:
    def __init__(self, base_url: str, user_token: Optional[str] = None):
        self.api_service = APIService(base_url)
        self.user_token = user_token
    
    def perform_action(self, action_data: Dict) -> Dict:
        return self.api_service.perform_app_action(self.user_token, action_data)
