API_URL = "https://keel.algida.me/electra/api/promo"

AppKey = "4125C97A-D92E-4F60-82C2-CC6CA5A3E683"

LoginResponse = {

    "key": "Message",

    "wrong": {

        "values": ["Girmiş olduğunuz cep telefonu numarası sistemde kayıtlı değildir, lütfen kontrol edip tekrar deneyiniz"],
        "code": 1

    },
    
    "correct": {
        
        "values": ["Lütfen giriş yapmak için cep telefonunuza gönderilen kodu giriniz"],
        "code": 0
    
    },

    "error": {

        "values": ["Kısa bir süre içerisinde çok fazla istekte bulundunuz, lütfen daha sonra tekrar deneyiniz"],
        "code": 2

    }
}

OtpResponse   = {
 
    "key": "Message",

    "wrong": {
    
        "values": ["Girdiğiniz kod doğrulanamamıştır, lütfen tekrar deneyiniz."],
        "code": 1

    },

    "correct": {

        "values": ["Algida dünyasına yönlendiriliyorsun."],
        "code": 0,
        
        "auth": [

            "CustomerID",
            "Token",
            "RefreshToken",
            "UCID"

        ]

    },

    "error": {

        "values": ["Kısa bir süre içerisinde çok fazla istekte bulundunuz, lütfen daha sonra tekrar deneyiniz"],
        "code": 2

    }


}


LogFile = "logs.txt"
ErrorFile = "errors.txt"