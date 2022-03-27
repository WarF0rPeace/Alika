# Kullanıcı hesabına giriş yapıp profil resmini güncelleyelim

from Alika import Alika
from Alika import WarForPeace

alika = Alika()
wfp = WarForPeace.WarForPeace()
wfp.clear()


numara = "+905555555555"

login = alika.login(numara)

if login[0]:

    OtpCode = input("Telefonunuza gelen onay kodunu giriniz\n>> ")
    flogin = alika.login(numara, OtpCode)
    
    if flogin[0]:

        user = alika.getUser()

        image = open("pp.png", "rb").read()
        image = wfp.ImageBase64(image).decode('utf-8')
        
        print(alika.changePP(image))
        print(user)

    else:

        print(flogin)

else:
    
    print(login)