from sys import exec_prefix
import sys
import pyttsx3
import time
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
from requests import get
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import pywhatkit
from Features import WishMe

#!      Setting up voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)

#!      Speak Function
def Speak(audio):
    # print(" ")
    print(f"FRIDAY : {audio}")
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("FRIDAY : Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("FRIDAY : Recognizing....")

        query = r.recognize_google(audio,language='en-in')
        print(f"Your Command : {query}\n")

    except Exception as e:
        return "none"
    query = query.lower()
    return query

#!-------------Def---------------#

def TaskExe():
    query = TakeCommand().lower()

#!------------Query--------------#

if __name__ == '__main__':
    WishMe()      #!  Don't Forget to comment out it...
    while True:
        query = TakeCommand().lower()

        #   Time
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p").replace(':',' ')
            Speak(f"The time is {strTime}")

        #   Costum Command
        elif 'good morning' in query or 'start my day' in query:
            from Features import GoodMorning
            GoodMorning(query)

        #   Time Table
        elif 'time table' in query or 'class' in query:
            Speak("Checking.....")
            Speak("According to Schedule")
            from Timetable import TimeTable
            TimeTable(query)

        #   Calender
        elif 'calendar' in query:
            from Features import Calender
            Calender(query)

        #   For google search
        elif 'google search' in query:
                query = query.replace("friday","")
                query = query.replace("google search","")
                query = query.replace("google","")
                from Features import GoogleSearch
                GoogleSearch(query)

        #   For YouTube search 
        elif 'youtube search' in query:
                Query = query.replace("friday","")
                query = Query.replace("youtube search","")
                from Features import YouTubeSearch
                YouTubeSearch(query)

        #   Writing notes
        elif 'write a note' in query or 'take note' in query:
                from Features import Notepad
                Notepad(query)

        #   Set Remember
        elif 'remember that' in query or 'remember me' in query:
                from Features import RememberThat
                rememberMsg = query.replace("remember that","")
                RememberThat(query)

        #   Reminding Remember
        elif 'what do you remember' in query or 'what i told you to remember' in query:
                from Features import Remember
                Remember(query)

        #   Ip adaress
        elif 'IP address' in query:
            from Features import IPAddress
            IPAddress(query)

        #   Location    #!Not working
        elif 'location' in query:
            from Features import Location
            Location(query) 

        #   Screenshot
        elif 'screenshot' in query:
            from Features import Screenshot
            Screenshot(query)

        elif 'phone number' in query:
            from Features import PhoneNo
            PhoneNo(query)
            

        #   How To Do Mode
        elif 'how to do' in query:
                from Features import HowToDo
                HowToDo(query)

        #   Calculation using API
        elif 'calculate' in query:
                from Features import Calculator
                Calculator(query)

        #   Temperature using API
        elif 'temperature' in query:
            from Features import Temperature
            Temperature(query)

        #   Chrome Automation
        elif 'chrome' in query:
            from Automations import ChromeAuto
            ChromeAuto(query)

        #   Youtube Automation
        elif 'YouTube' in query:
            from Automations import YouTubeAuto
            YouTubeAuto(query)

        #   Open Applications
        elif 'open' in query:
            from Applications import OpenApps
            OpenApps(query)

        #   Close program
        elif 'close' in query:
            from Applications import CloseApps
            CloseApps(query)

        #   For Playing random music
        elif 'play music' in query:
            from Automations import Music
            Music(query)

        #   For Create, Add, And show Tasks
        elif 'task' in query:
            from Features import Tasks
            Tasks(query)

        #   Idea
        elif 'idea' in query:
            from Features import Idea
            Idea(query)

        elif 'news' in query:
            from Features import News
            News(query)

        #   How to do   
        elif 'how to do' in query:
            from Features import HowToDo
            HowToDo(query)

        #   New work
        elif 'new work' in query:
            from Features import Work
            Work(query)

        #   Show Task
        elif 'show work' in query:
            from Features import WorkingOn
            WorkingOn(query)

        #   Toss a coin
        elif 'coin' in query:
            from Random import TossCoin
            TossCoin(query)

        #   Throw Dice
        elif 'dice' in query:
            from Random import ThrowDice
            ThrowDice(query)

        #   Choose Number
        elif 'choose number' in query:
            from Random import RandomNumber
            RandomNumber(query)

        #!   Exit program
        elif 'exit program' in query or 'quit' in query:
            Speak("Terminating program...Please wait")
            sys.exit()

        #  Sleep program
        elif 'sleep' in query or 'you can sleep' in query:
            Speak(" Ok sir,I am going to sleep now you can call me anytime")
            break

        #   Read PDF
        elif 'read PDF' in query:
            from Features import AudioBook
            AudioBook(query)

        #   For commands that are not in query
        else:
            from ChatBot import ChatterBot
            replay = ChatterBot(query)
            Speak(replay)

            # Speak('Command Not recognized')

        Speak("Sir, do you have any other work")
TaskExe()
#todo Loop and sleep function
if __name__ == '__main__':
    while True:
        Permission = TakeCommand()
        if 'wake up' in Permission or 'are you there' in Permission:
            Speak("I am always here to help you sir please tell me what I can do for you")
            TaskExe()

        elif 'exit program' in Permission or 'quit' in Permission:
            Speak("Terminating program...Please wait")
            sys.exit()