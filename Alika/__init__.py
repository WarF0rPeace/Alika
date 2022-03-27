from Alika import variables
from Alika import WarForPeace

import requests

class Alika():

    def __init__(self) -> None:
        
        self.headers = {
            
            "Accept"            : "application/json, text/plain, */*",
            "Content-Type"      : "application/json",
            "Accept-Encoding"   : "gzip, deflate",
            "User-Agent"        : "okhttp/4.9.1"
        
        }

        self.wfp = WarForPeace.WarForPeace()
        
    
    def login(self, PhoneNumber, PinCode = None):

        try:

            if not PinCode:


                json_data = {
                    
                    "appKey"    : variables.AppKey,
                    "msisdn"    : PhoneNumber
                
                }
                
                r = requests.post(
                    
                    url         = f"{variables.API_URL}/customerLogin",
                    headers     = self.headers,
                    json        = json_data
                
                )

                try: json_resp = r.json()[0]
                except: json_resp = r.json()
                

                if variables.LoginResponse['key'] in json_resp.keys():

                    if json_resp[variables.LoginResponse['key']] in variables.LoginResponse['correct']['values']:

                        self.PhoneNumber = PhoneNumber 
                        
                        return True, json_resp, variables.LoginResponse['correct']['code']
                    
                    elif json_resp[variables.LoginResponse['key']] in variables.LoginResponse['wrong']['values']:

                        return False, json_resp, variables.LoginResponse['wrong']['code']

                    elif json_resp[variables.LoginResponse['key']] in variables.LoginResponse['error']['values']:

                        return False, json_resp, variables.LoginResponse['error']['code']                   
               
                self.wfp.writeWfp(

                    text    = f"Garip bir şeyler oldu, bu yanıtı tanımlayamıyorum manuel olarak variables.py dosyasına tanımlayın",
                    _type   = "info",
                    _log    = True

                )

                self.wfp.writeWfp(
                    
                    text    = r.text,
                    _type   = "danger",
                    _log    = True
                
                )
                
                return False, json_resp, 'wfp'


            else:
                
                json_data = {
                    
                    "appKey"    : variables.AppKey,
                    "msisdn"    : PhoneNumber,
                    "pincode"   : PinCode
                
                }
                
                r = requests.post(
                    
                    url         = f"{variables.API_URL}/checkPincode",
                    headers     = self.headers,
                    json        = json_data
                
                )

                try: json_resp = r.json()[0]
                except: json_resp = r.json()

                if variables.OtpResponse['key'] in json_resp.keys():

                    if json_resp[variables.OtpResponse['key']] in variables.OtpResponse['correct']['values']:

                        self.PhoneNumber    = PhoneNumber

                        self.CustomerId     = json_resp[variables.OtpResponse['correct']['auth'][0]]
                        self.Token          = json_resp[variables.OtpResponse['correct']['auth'][1]]
                        self.RefreshToken   = json_resp[variables.OtpResponse['correct']['auth'][2]]
                        self.UCID           = json_resp[variables.OtpResponse['correct']['auth'][3]]
                        
                        return True, json_resp, variables.LoginResponse['correct']['code']
                    
                    elif json_resp[variables.OtpResponse['key']] in variables.OtpResponse['wrong']['values']:

                        return False, json_resp, variables.LoginResponse['wrong']['code']
                    
                    
               
                self.wfp.writeWfp(

                    text    = f"Garip bir şeyler oldu, bu yanıtı tanımlayamıyorum manuel olarak variables.py dosyasına tanımlayın",
                    _type   = "info",
                    _log    = True

                )

                self.wfp.writeWfp(
                    
                    text    = r.text,
                    _type   = "danger",
                    _log    = True
                
                )
                
                return False, json_resp, 'wfp'

        except Exception as e:

            self.wfp.errorLog(

                e

            )

            return False, e
    
    def getUser(self, Token = None, CustomerId = None):

        try:

            Token = self.Token if not Token else Token
            CustomerId = self.CustomerId if not CustomerId else CustomerId

            headers = self.headers.copy()

            headers['Authorization'] = f"Bearer {Token}"
            
            json_data = {
                
                "appKey"        : variables.AppKey,
                "CustomerID"    : CustomerId
            
            }

            r = requests.post(
                
                url         = f"{variables.API_URL}/getCustomer",
                headers     = headers,
                json        = json_data
            
            )

            if r.status_code == 401:

                return False, r
            
            elif r.status_code == 200:

                json_resp = r.json()

                return True, json_resp


        except Exception as e:

            self.wfp.errorLog(

                e

            )

            return False, e
    
    def getGifts(self, Token = None):

        try:

            Token = self.Token if not Token else Token

            headers = self.headers.copy()

            headers['Authorization'] = f"Bearer {Token}"
            
            json_data = {
                
                "appKey"    : variables.AppKey
            
            }

            r = requests.post(
                
                url         = f"{variables.API_URL}/getGifts",
                headers     = headers,
                json        = json_data
            
            )

            if r.status_code == 401:

                return False, r
            
            elif r.status_code == 200:

                json_resp = r.json()

                return True, json_resp


        except Exception as e:

            self.wfp.errorLog(

                e

            )

            return False, e
    
    def buyGift(self, GiftId: int, Token = None, CustomerId = None):

        try:

            Token = self.Token if not Token else Token
            CustomerId = self.CustomerId if not CustomerId else CustomerId

            headers = self.headers.copy()

            headers['Authorization'] = f"Bearer {Token}"
            
            json_data = {
                
                "appKey"        : variables.AppKey,
                "CustomerID"    : CustomerId,
                "GiftID"        : GiftId
            
            }

            r = requests.post(
                
                url         = f"{variables.API_URL}/buyGift",
                headers     = headers,
                json        = json_data
            
            )

            if r.status_code == 401:

                return False, r
            
            elif r.status_code == 200:

                json_resp = r.json()
                
                return True, json_resp
             
            
            return False, json_resp


        except Exception as e:

            self.wfp.errorLog(

                e

            )

            return False, e
    
    def dataPreCheck(self, Token = None, CustomerId = None):

        try:
            
            Token = self.Token if not Token else Token
            CustomerId = self.CustomerId if not CustomerId else CustomerId

            headers = self.headers.copy()

            headers['Authorization'] = f"Bearer {Token}"
            
            json_data = {
                
                "appKey"        : variables.AppKey,
                "CustomerID"    : CustomerId

            }

            r = requests.post(
                
                url         = f"{variables.API_URL}/dataPreCheck",
                headers     = headers,
                json        = json_data
            
            )

        
            if r.status_code == 401:

                    return False, r
                
            elif r.status_code == 200:

                json_resp = r.json()
                
                return True, json_resp
                
            
            return False, json_resp
        
        except Exception as e:

            self.wfp.errorLog(

                e

            )

            return False, e
    
    def useDataGift(self, GiftCode: str, PhoneNumber = None, Token = None, CustomerId = None):

        try:
            
            Token = self.Token if not Token else Token
            CustomerId = self.CustomerId if not CustomerId else CustomerId
            PhoneNumber = self.PhoneNumber if not PhoneNumber else PhoneNumber

            PhoneNumber = self.wfp.phoneFormat(PhoneNumber)

            headers = self.headers.copy()

            headers['Authorization'] = f"Bearer {Token}"
            
            json_data = {
                
                "CustomerID"    : CustomerId,
                "GiftCode"      : GiftCode,
                "Msisdn"        : PhoneNumber,
                "appKey"        : variables.AppKey,

            }

            r = requests.post(
                
                url         = f"{variables.API_URL}/useInternetGift",
                headers     = headers,
                json        = json_data
            
            )

        
            if r.status_code == 401:

                    return False, r
                
            elif r.status_code == 200:

                json_resp = r.json()
                
                return True, json_resp
                
            
            return False, json_resp
        
        except Exception as e:

            self.wfp.errorLog(

                e

            )

            return False, e
    
    def UseStickCode(self, StickCode: str, Token = None, CustomerId = None):

        try:
            
            Token = self.Token if not Token else Token
            CustomerId = self.CustomerId if not CustomerId else CustomerId
            
            headers = self.headers.copy()

            headers['Authorization'] = f"Bearer {Token}"
            
            json_data = {
                
                "CustomerID"    : CustomerId,
                "StickCode"     : StickCode,
                "appKey"        : variables.AppKey,

            }

            r = requests.post(
                
                url         = f"{variables.API_URL}/checkStickcode",
                headers     = headers,
                json        = json_data
            
            )

        
            if r.status_code == 401:

                    return False, r
                
            elif r.status_code == 200:

                json_resp = r.json()
                
                return True, json_resp
                
            
            return False, json_resp
        
        except Exception as e:

            self.wfp.errorLog(

                e

            )

            return False, e
    
    
    def changePP(self, ImageData, Token = None, CustomerId = None):

        try:
            
            Token = self.Token if not Token else Token
            CustomerId = self.CustomerId if not CustomerId else CustomerId
            
            headers = self.headers.copy()

            headers['Authorization'] = f"Bearer {Token}"
            
            json_data = {
                
                "CustomerID"    : CustomerId,
                "Image"         : ImageData,
                "appKey"        : variables.AppKey,

            }

            r = requests.post(
                
                url         = f"{variables.API_URL}/saveProfilePicture",
                headers     = headers,
                json        = json_data
            
            )

        
            if r.status_code == 401:

                    return False, r
                
            elif r.status_code == 200:

                json_resp = r.json()
                
                return True, json_resp
                
            
            return False, r.text
        
        except Exception as e:

            self.wfp.errorLog(

                e

            )

            return False, e