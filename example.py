from alika import App

app = App()
phone_number = input(f"Numara: ")
verification_response = app.auth.send_verification_code(phone_number)
if verification_response.get('status'):
    print(verification_response.get('message'))
    
    verification_code = input("Onay kodu: ")
    verification_data = app.auth.verify_code(phone_number, verification_code)
    
    if verification_data.get('status'):
        print(verification_data)
