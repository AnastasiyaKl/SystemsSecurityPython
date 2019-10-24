from Crypto.PublicKey import RSA
from hashlib import sha512
import os.path
import os
import tkinter as tk
import psutil
from ctypes import *
user32 = windll.user32

def start_permission():
    if (os.path.exists("C:/Users/Public/BIS_KEYS/rsa") == False and os.path.exists("C:/Users/Public/BIS_KEYS/rsa_pub") == False and os.path.exists("C:/Users/Public/BIS_KEYS/signature") == False):
        keyPair = RSA.generate(bits=1024)

        f = open("C:/Users/Public/BIS_KEYS/rsa_pub","w+")
        f.write(str(keyPair.n) + " " + str(keyPair.e))
        f.close()

        f = open("C:/Users/Public/BIS_KEYS/rsa","w+")
        f.write(str(keyPair.n) + " " + str(keyPair.d))
        f.close()

        f = open("C:/Users/Public/BIS_KEYS/signature","w+")
        msg = str(sys_inf()).encode('utf-8')
        hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
        signature = pow(hash, keyPair.d, keyPair.n)
        f.write(str(signature))
        f.close()
        return True
    elif(os.path.exists("C:/Users/Public/BIS_KEYS/rsa") == False or os.path.exists("C:/Users/Public/BIS_KEYS/rsa_pub") == False or os.path.exists("C:/Users/Public/BIS_KEYS/signature") == False):
        return False
    else:
        f = open("C:/Users/Public/BIS_KEYS/rsa_pub","r")
        contentsPub = f.read()
        arContentsPub = contentsPub.split(" ")
        try:
            arContentsPub_1 = int(arContentsPub[1])
            arContentsPub_0 = int(arContentsPub[0])
        except:
            return False
        f.close()

        f = open("C:/Users/Public/BIS_KEYS/signature","r")
        contentsSign = f.read()
        try:
            contentsSign = int(contentsSign)
        except:
            return False
        f.close()

        msg = str(sys_inf()).encode('utf-8')
        hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
        hashFromSignature = pow(contentsSign, arContentsPub_1, arContentsPub_0)
        if (hash == hashFromSignature):
            return True
        else:
            return False

def sys_inf():
    inf = ''

    # Определяем язык ввода
    hwnd = user32.GetForegroundWindow()
    threadID = user32.GetWindowThreadProcessId(hwnd, None)
    StartLang = user32.GetKeyboardLayout(threadID)
    if ( StartLang == 67699721):
        lang = " ENG "
    elif ( StartLang == 67568647):
        lang = " DEU "
    elif (StartLang == -257424350):
        lang = " UKR "
    elif (StartLang == 68748313):
        lang = " RUS "
    else :
        lang = " " + StartLang + " "
    # RAM
    memory = psutil.virtual_memory().total / (1024.0 ** 3)
    inf += " " + str(memory) + " "
    # Screen size
    root_main = tk.Tk()
    inf += " " + str(root_main.winfo_screenheight()) + "px "
    inf += " " + str(root_main.winfo_screenheight()) + "px "
    root_main.destroy()
    # Username
    inf += " " + os.environ.get( "USERNAME" ) + " "
    # Path to Windows
    inf += " " + os.environ.get('SYSTEMROOT') + " "
    # Computername
    inf += " " + os.environ['COMPUTERNAME'] + " "
    # Current disk
    inf += " " + str(os.getcwd())[:2] + " "
    # Memory on current disk
    inf += " " + str(psutil.disk_usage('/').total / (1024.0 ** 3)) + " "

    return inf

