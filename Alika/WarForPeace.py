import os
import random
import re
import string
import base64

from datetime import datetime

from Alika import variables

from colorama import Fore, init

init(autoreset=True)


class WarForPeace():

    def getRandomString(self, length: int):
        
        letters = string.ascii_letters + string.digits
        return ''.join(
            
            random.choice(
                
                letters
            
            ) for i in range(
                
                length
                
            )
        )

    def getCurrentTime(self):
        
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def log(self, LogFile, Text):
        
        _file = open(
            
            LogFile,
            'a',
            encoding='utf-8'
        
        )

        _file.write(f"[{self.getCurrentTime()}] {str(Text)}\n")

    def writeWfp(self, text, _type, _log):
        
        msg = f'{Fore.LIGHTMAGENTA_EX}[{self.getCurrentTime()}]{Fore.YELLOW} - '
        
        if _type == 'info':
            
            msg += f'{Fore.LIGHTCYAN_EX}{text}'
        
        elif _type == 'danger':
        
            msg += f'{Fore.RED}{text}'
        
        elif _type == 'success':
        
            msg += f'{Fore.LIGHTGREEN_EX}{text}'
        
        elif _type == 'plain':
        
            msg += f'{Fore.LIGHTWHITE_EX}{text}'
        
        elif _type == 'special':
        
            msg += text
        
        print(msg)
        
        if _log:
        
            self.log(
                
                variables.LogFile,
                text
            
            )
    
    def errorLog(self, e):
        
        text = f"\n{'=' * 20}\nError: {e}\nError Line: {e.__traceback__.tb_lineno}\n{'='*20}"
        
        self.log(    
            
            variables.ErrorFile,
            text
        
        )
        
        self.writeWfp(
            
            f"{text}",
            'danger',
            False
        
        )
    
    def phoneFormat(self, number):
        
        number = number.lstrip("+")
        number = number.lstrip("90")
        number = re.sub("[ ()-]", '', number)
        
        assert(len(number) == 10)
        
        number = f"{number[:3]} {number[3:6]} {number[6:8]} {number[8:]}"
        
        return number

    def imageBase64(self, image):

        return base64.b64encode(image)

    def readFile(self, filename, method, writetable = False):

        f = open(filename, method, encoding='utf-8')
            
        if writetable:

            return f

        content = [line.strip('\n') for line in f]
        
        return content

    def clear(self):

        if os.name == 'posix':
        
            os.system('clear')
        
        elif os.name in ('ce', 'nt', 'dos'):
        
            os.system('cls')
        
        else:
        
            print("\n") * 120