from .api.api_service import APIService
from typing import Dict, Optional

class UserService:
    def __init__(self, base_url: str, user_token: Optional[str] = None):
        self.api_service = APIService(base_url)
        self.user_token = user_token
    
    def get_user_data(self) -> Dict:
        return self.api_service.get_user_data(self.user_token)
    
    def update_user_settings(self, new_settings: Dict) -> Dict:
        return self.api_service.update_user_settings(self.user_token, new_settings)
