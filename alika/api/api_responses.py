from typing import Optional, Union, List, Dict

class APIResponses:
    RESPONSE_MESSAGES = {
        
        "Lütfen cep telefonunuza gönderilen kodu giriniz": 1,
        "Girmiş olduğunuz cep telefonu numarası sistemde kayıtlı değildir, lütfen kontrol edip tekrar deneyiniz": 0,
        
        "Algida dünyasına yönlendiriliyorsun.": 1,
        "Girdiğiniz kod doğrulanamamıştır, lütfen tekrar deneyiniz.": 0,
        
        "Kısa bir süre içerisinde çok fazla istekte bulundunuz, lütfen daha sonra tekrar deneyiniz": 0,
    }

    @staticmethod
    def process_response(response: Optional[Union[List[Dict], Dict]]) -> Dict:
        if not isinstance(response, list):
            if not isinstance(response, dict):
                return {"status": False}
        else:
            if not isinstance(response[0], dict):
                return {"status": False}
            else: response = response[0]
        
        response = response.get('Message')
        
        if response in APIResponses.RESPONSE_MESSAGES:
            return {"status": APIResponses.RESPONSE_MESSAGES[response], "message": response}
        else:
            return {"status": False, "message": response}

    @staticmethod
    def process_verification(response) -> Dict:
        return APIResponses.process_response(response.json())

    @staticmethod
    def process_code_verification(response):
        keys_to_check = ['UCID', 'RefreshToken', 'Token', 'CustomerID']
        data = response.json()
        if not isinstance(data, list):
            if not isinstance(data, dict):
                return {"status": False}
        else:
            if not isinstance(data[0], dict):
                return {"status": False}
            else: data = data[0]
            
        api_response = APIResponses.process_response(data)
        if all(key in data for key in keys_to_check):
            api_response.update(data)
        return api_response

    @staticmethod
    def process_login(response):
        # Login API yanıtını işle
        pass

    @staticmethod
    def process_user_data(response):
        # User data API yanıtını işle
        pass

    @staticmethod
    def process_update_settings(response):
        # Update settings API yanıtını işle
        pass

    @staticmethod
    def process_app_action(response):
        # App action API yanıtını işle
        pass
