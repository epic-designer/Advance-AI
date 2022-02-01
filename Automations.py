from os import startfile
import keyboard
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import pyttsx3
import speech_recognition as sr
import webbrowser as web
import os
import random
from Features import Speak, TakeCommand

#! Chrome Automation
def ChromeAuto(command):
        query = str(command)
        if 'new tab' in query:
            press_and_release('ctrl + t')

        elif 'close tab' in query:
            press_and_release('ctrl + w')

        elif 'new window' in query:
            press_and_release('ctrl + n')

        elif 'history' in query:
            press_and_release('ctrl + h')

        elif 'downloads' in query:
            press_and_release('ctrl + j')

        elif 'bookmark' in query:
            press_and_release('ctrl + d')
            press('enter')

        elif 'history' in query:
            press_and_release('ctrl + h')

        elif 'incognito mode' in query:
            press_and_release('ctrl + Shift + n')

        elif 'switch tab' in query:
            tab = query.replace("switch tab", "")
            Tab = tab.replace("to","")
            num = Tab

            Tabbs = f'ctrl + {num}'
            press_and_release(Tabbs)

        elif 'open' in query:
            name = query.replace("open","")
            NAmeA = str(name)


            if 'youtube' in query:
                web.open("https://www.youtube.com/")
                # print("Opening youtube as web")
                Speak("Opening youtube as web")


            elif 'whatsapp' in query:
                web.open("https://web.whatsapp.com/")
                # print("Openin whatsapp as web")
                Speak("Opening whatsapp as web")


            elif 'instagram' in query:
                web.open("https://www.instagram.com/")
                # print("Opening instagram as web")
                Speak("Opening instagram as web")


            elif 'discord' in query:
                web.open("https://discord.com/channels/917978594842665010/917991684728578068")
                # print("Opening discord as web")
                Speak("Opening discord as web")
            

            elif 'my official website' in query:
                web.open("epicdesigns.rf.gd")
                # print("Opening your website as web")
                Speak("Opening your website as web")

            elif 'my portfolio website' in query:
                web.open("https://epicdesign.rf.gd/")
                # print("Opening your portfolio website")
                Speak("Opening your portfolio website")

            elif 'City Premier College' in query and 'CPC' in query:
                web.open("https://www.cpcnagpur.com/")
                Speak("Opening Website")

#!  Music
def Music(music):

            music_dir = 'D:\\my music'
            songs = os.listdir(music_dir)
            print(songs)
            rdm = random.choice(songs)
            os.startfile(os.path.join(music_dir, rdm))
            Speak("Playing Music")

#! Youtube Automation
def YouTubeAuto(command):
    query = TakeCommand().lower()

    if 'pause' in query:
        press_and_release('space bar')

    elif 'resume' in query:
        press('space bar')
    
    elif 'full screen' in query:
        press('f')

    elif 'film screen' in query:
        press('t')
        
    elif 'skip' in query:
        press('l')

    elif 'back' in query:
        press('j')

    elif 'increse' in query:
        press_and_release('shift + >')

    elif 'decrease' in query:
        press_and_release('shift + <')

def CPC(query):
    Speak("Opening...")
    web.open("https://www.cpcnagpur.com/")
    Speak("Opening City Premire College website")