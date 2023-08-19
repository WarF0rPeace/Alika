import requests
from typing import Optional, Dict
from .api_responses import APIResponses

class APIService:
    def __init__(self, base_url: str):
        self.base_url = base_url
        
        self.headers = {"Accept": "application/json, text/plain, */*",
                        "Content-Type": "application/json",
                        "Accept-Encoding": "gzip, deflate",
                        "User-Agent": "okhttp/4.9.1"}
        
        self.app_key = "830DA10A-FA97-4244-8B40-E97EC8F085D9"
    
    def _set_authorization(self, token: Optional[str] = None) -> dict: 
        headers = self.headers.copy()
        if token: headers["Authorization"] = f"Bearer {token}"
        return headers
    
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        url = self.base_url + endpoint
        response = requests.request(method, url, json=data, headers=headers)
        return response
    
    def send_verification_code(self, phone_number: str) -> Dict:
        headers = self._set_authorization()
        headers["Captchatoken"] = "token"
        endpoint = "/promo/customerLogin"
        data = {"appKey": self.app_key, "msisdn": phone_number}
        response = self._make_request("POST", endpoint, data=data, headers=headers)

        return APIResponses.process_verification(response)
    
    def verify_code(self, phone_number: str, verification_code: str) -> Dict:
        headers = self._set_authorization()
        headers["Captchatoken"] = "token"
        endpoint = "/promo/checkPincode"
        data = {"appKey": self.app_key, "msisdn": phone_number, "pincode": verification_code}
        response = self._make_request("POST", endpoint, data=data, headers=headers)
    
        return APIResponses.process_code_verification(response)
    
    def login(self, phone_number: str, token: Optional[str] = None) -> Dict:
        pass
    
    def get_user_data(self, token: str) -> Dict:
        pass
    
    def update_user_settings(self, token: str, new_settings: Dict) -> Dict:
        pass
    
    def perform_app_action(self, token: str, action_data: Dict) -> Dict:
        pass
