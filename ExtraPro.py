import pyttsx3
import speech_recognition as sr
import pyqrcode
import png
from pyqrcode import QRCode
import os
import random
import string
from pytube import YouTube

#!      Setting up voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def Speak(audio):
    print(" ")
    print(f"FRIDAY : {audio}")   #!  Replace FRIDAY
    engine.say(audio)
    engine.runAndWait()

def QRCode(query):
    Speak("Sir , Enter url for QR Code")
    link = input(str("Enter Link (url) : "))

    url = pyqrcode.create(link)

    Speak("Please, Enter name for QR Code")
    Name = input(str("Enter name for QR code : "))

    Final = url.png(f"{Name}.png", scale = 8)
    QRName = Name+".png"

    path_1 = "E:\\Projects\\Advance AI\\"+QRName
    path_2 = "E:\\Projects\\Advance AI\\DataBase\\QR Codes\\"+QRName

    os.rename(path_1,path_2)
    Speak("QR Code is saved at default folder")

def PasswordGenerator(query):
    print("Welcome to Password Generator")
    length = int(input('\nEnter length of password : '))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = upper+lower+num+symbols

    temp = random.sample(all,length)
    password = "".join(temp)
    print(password)
