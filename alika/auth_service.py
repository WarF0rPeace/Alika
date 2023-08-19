from .api.api_service import APIService
from typing import Dict

class AuthService:
    def __init__(self, base_url: str):
        self.api_service = APIService(base_url)
    
    def send_verification_code(self, phone_number: str) -> Dict:
        return self.api_service.send_verification_code(phone_number)
    
    def verify_code(self, phone_number: str, verification_code: str) -> Dict:
        return self.api_service.verify_code(phone_number, verification_code)
    
    def login(self, phone_number: str, token: str) -> Dict:
        return self.api_service.login(phone_number, token)
