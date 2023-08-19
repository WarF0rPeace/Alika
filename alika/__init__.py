from .auth_service import AuthService
from .user_service import UserService
from .app_functionality import AppFunctionality

class App:
    
    def __init__(self) -> None:
        
        self.base_url = "https://keel.algida.me/electra/api"
        
        self.auth = AuthService(base_url=self.base_url)
        self.user = UserService(base_url=self.base_url)
        self.app = AppFunctionality(base_url=self.base_url, user_token=None)
    
    def set_user_token(self, user_token):
        
        self.user.user_token = user_token
        self.app.user_token = user_token