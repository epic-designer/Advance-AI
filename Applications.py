from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import pyttsx3
import speech_recognition as sr
import webbrowser as web
import os

from Features import Speak, TakeCommand

def OpenApps(app):
    query = str(app)

    #Discord
    if 'discord' in query:
            discordPath = "C:\\Users\\Hp\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe"
            os.startfile(discordPath)
            # print("Opening discord")
            Speak("Opening discord")

    #VS Code
    elif 'vs code' in query:
            codePath = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            Speak("Opening VS code")

    # Command prompt
    elif 'command prompt' in query:
            os.system("start cmd")
            # print("Opening command prompt")
            Speak("Opening command prompt")

    #- Whatsapp
    elif 'whatsapp' in query:
            WAPath = "C:\\Users\\Hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(WAPath)
            # print("Opening Whatsapp")
            Speak("Opening Whatsapp")

    #- spotify
    elif 'spotify' in query:
            SpotifyPath = "C:\\Users\\Hp\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(SpotifyPath)
            # print("Opening Spotify")
            Speak("Opening Spotify")

    # Canva app
    elif 'canva' in query:
            CanvaAppPath = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Canva\\Canva.exe"
            os.startfile(CanvaAppPath)
            # print("Opening CanvaApp")
            Speak("Opening CanvaApp")

        # Notepad ++
    elif 'notepad plus plus' in query:
            NotepadplusplusPath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(NotepadplusplusPath)
            # print("Opening Notepad plus plus")
            Speak("Opening Notepad plus plus")

    # Teams
    elif 'teams' in query:
            teamsPath = "C:\\Users\\Hp\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            os.startfile(teamsPath)
            # print("Opening Teams")
            Speak("Opening Teams")

    elif 'notepad' in query:
            notepadPath = "C:\\Windows\\system32\\Notepad.exe"
            os.startfile(notepadPath)
            # print("Opening Notepad")
            Speak("Opening Notepad")

    elif 'calculator' in query:
            os.system("start calc")
            # print("Opening Calculator")
            Speak("Opening Calculator")

    elif 'control panel' in query:
            os.system("start control")
            # print("Opening Control panel")
            Speak("Opening Control panel")

def CloseApps(app):
    query = str(app)

    if 'notepad' in query:
        os.system("taskkill /f /im Notepad.exe")
        # print("Closing Notepad")
        Speak("Closing Notepad")

    elif 'discord' in query:
        os.system("taskkill /f /im Discord.exe")
        # print("Closing Discord")
        Speak("Closing Discord")

    elif 'vs code' in query:
        os.system("taskkill /f /im Code.exe")
        # print("Closing VS code")
        Speak("Closing VS code")

    elif 'command prompt' in query:
        os.system("taskkill /f /im cmd")
        # print("Closing command prompt")
        Speak("Closing command prompt")

    elif 'whatsapp' in query:
        os.system("taskkill /f /im WhatsApp.exe")
        # print("Closing whatsapp")
        Speak("Closing whatsapp")

    elif 'canva' in query:
        os.system("taskkill /f /im Canva.exe")
        # print("Closing canva")
        Speak("Closing canva")

    elif 'notepad plus plus' in query:
        os.system("taskkill /f /im notepad++.exe")
        # print("Closing Notepad ++")
        Speak("Closing Notepad ++")

    elif 'teams' in query:
        os.system("taskkill /f /im Teams.exe")
        # print("Closing Teams")
        Speak("Closing Teams")

    elif 'calculator' in query:
        os.system("taskkill /f /im calc")
        # print("Closing Calculator")
        Speak("Closing Calculator")

    elif 'control panel' in query:
        os.system("taskkill /f /im control")
        # print("Closing control panel")
        Speak("Closing control panel")