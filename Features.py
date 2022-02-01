import pywhatkit
import wikipedia
from pywikihow import WikiHow , search_wikihow
import os
import webbrowser as web
from sys import exec_prefix
import pyttsx3
import datetime
from GoogleNews import GoogleNews
import PyPDF2
import pyautogui
import time
import phonenumbers
from phonenumbers import carrier,geocoder,timezone
import random
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
from requests import get
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import pywhatkit
import wolframalpha
import calendar


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def Speak(audio):
    print(" ")
    print(f"FRIDAY : {audio}")   #!  Replace FRIDAY
    engine.say(audio)
    engine.runAndWait()

# Take Command
def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(":Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print(": Recognizing....")
        
        query = r.recognize_google(audio,language='en-in')
        print(f": Your Command : {query}\n")
        
    except:
        return ""
    return query.lower()

#   todo Wish Query
def WishMe():
    strTime = datetime.datetime.now().strftime("%I:%M %p").replace(':',' ')
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        # print("Good Morning!")
        Speak("Good Morning!")

    elif hour>=12 and hour<18:
        # print("Good Afternoon!")
        Speak("Good Afternoon!")

    else:
        # print("Good Evening!")
        Speak("Good Evening!")
    Speak(f"The time is {strTime}")
    # print(f"The time is {strTime}")
    Speak("I am FRIDAY Sir. Please tell me how may I help you")
    # print("I am FRIDAY Sir. Please tell me how may I help you")

#   todo YouTube search
def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")

#   todo Google search
def GoogleSearch(term):
    import wikipedia as googleScrap
    Speak("This is what I found on Google!")
    pywhatkit.search(term)

    try:
        result = googleScrap.summary(term,5)
        Speak(result)
    except:
        Speak("No readable data found")

#   todo Notepad automation (To take note)  
def Notepad(term):
    Speak("Tell me the title.")
    Title = TakeCommand()

    Speak("Tell me the note.")
    Speak("I am ready to write.")

    writes = TakeCommand()

    time = datetime.datetime.now().strftime("%H:%M")
    filename = Title + str(time).replace(":",".") + "-note.txt"

    with open(filename,"w") as file:
        file.write(writes)

    path_1 = "E:\\Projects\\Advance AI\\" + str(filename)
    path_2 = "E:\\Projects\\Advance AI\\Notes\\" + str(filename)

    os.rename(path_1,path_2)
    os.startfile(path_2)

    Speak("Note is saved successfully!")

#   todo Costum Command
def GoodMorning(term):
            Speak("Hello sir!")
            strTime = datetime.datetime.now().strftime("%I %M %p")
            Speak(f"time is {strTime}")

            strDate = datetime.datetime.now().strftime("%b %m")
            Speak(f"todays date is {strDate}")
            search = "temperature in nagpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            date = BeautifulSoup(r.text,"html.parser")
            temp = date.find("div",class_="BNeawe").text
            Speak(f"Current {search} is {temp}")

            Speak("Showing your tasks!..")
            Taskpath = "E:\\Projects\\Advance AI\\Data\\Tasks.txt"
            os.startfile(Taskpath)

#   todo Remember That
def RememberThat(term):
    rememberMsg = TakeCommand().lower()
    Speak("Ok Sir!I will remeber that")
    print(rememberMsg)
    remember = open('Data\\Remember.txt','w')
    remember.write(rememberMsg)
    remember.close()

#   todo Remember msg
def Remember(term):
    remember = open('Data\\Remember.txt','r')
    Speak("You tell me to remember that"+ remember.read())

#   todo Create,add and open taks.
def Tasks(term):
    #Create Tasks
    if 'create' in term:

        Speak("Ok sir!What should be the task")
        task = TakeCommand().lower()
        print(task)
        Speak("Task created!")
        theTask = open('Data\\Tasks.txt','w')
        theTask.write(">\t"+task)
        theTask.close()

    #Add Tasks
    elif 'add' in term:
        Speak("Ok sir!What should I add in tasks")
        task = TakeCommand().lower()
        print(task)
        Speak("Task added Successfully!")
        theTask = open('Data\\Tasks.txt','a')
        theTask.write(">\t" + task + "\n")
        theTask.close()

    #Show Tasks
    elif 'show' in term:
        print("Showing tasks")
        Speak("Showing tasks")
        path = "E:\\Projects\\Advance AI\\Data\\Tasks.txt"
        os.startfile(path)

#   todo API
def WolfRame(query):
    api_key = "99JXT5-AH2KPA6Q22"
    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)

    Answer = next(requested.results).text

    try:
        Answer = next(requested.results).text
        return Answer
    except:
        Speak("String value is not answerable")

#   todo Calculator
def Calculator(query):

    Term = str(query)
    Term = Term.replace("friday","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("into","*")

    Final = str(Term)

    try:
        result = WolfRame(Final)
        Speak(f"{result}")
        print(result)
    except:
        Speak("Answer not found")

#   todo Temperature
def Temperature(query):
    Term = str(query)
    Term = Term.replace("Friday","")
    Term = Term.replace("friday","")
    Term = Term.replace("check","")
    Term = Term.replace("in","")
    Term = Term.replace("what is the","")
    Term = Term.replace("temperature","")

    temp_query = str(Term)

    if 'outside' in temp_query:
        var1 = "Temperature in nagpur"
        answer = WolfRame(var1)
        Speak(f"{var1} is {answer} .")
        # print(f"{var1} is {answer} .")

    else:
        var2 = "Temprature in " + temp_query
        answ = WolfRame(var2)
        Speak(f"{var2} is {answ}")
        print(f"{var2} is {answ}")

#   Dictionary
def Dictionary(query):
    Term = str(query)
    Meaning = WolfRame(Term)
    Speak(Meaning)

#   todo IP Address
def IPAddresss(term):
    ip = get('https://api.ipify.org').text
    Speak(f"Your IP Address is {ip}")

#   todo   Location
def Location(term):
    Speak("Please wait...Let me check.")
    try:
        IP = requests.get('https://api.ipify.org').text
        print(IP)
        url = 'https://get.geojs.io/v1/ip/geo/' +IP+'.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()

        city = geo_data['city']
        state = geo_data['state']
        country = geo_data['country']
        Speak(f"Sir! We are in {city} city of state {state} of {country} country")

    except Exception as e:
        Speak("Sorry sir! I am not able to find due to network issue")
        pass

#   todo   Screenshot
def Screenshot(term):
    Speak("Sir,Please tell me the name of the screenshot file.")
    Name = TakeCommand().lower()
    Speak("Please hold down a bit I am taking screenshot")
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save(f"{Name}.png")
    Path1 = "E:\\Projects\\Advance AI\\"+str(Name)+".png"
    Path2 = "E:\Projects\\Advance AI\\DataBase\\Screenshot\\"+str(Name)+".png"
    os.rename(Path1,Path2)
    Speak("I am done sir Screnshot Saved")

#   todo   How-to-do
def HowToDo(query):
    Speak("How to do mode is initiated.Please tell me what should I search")
    how = TakeCommand()
    max_results = 1
    how_to = search_wikihow(how,max_results)
    assert len(how_to) == 1
    how_to[0].print()
    Speak(how_to[0].summary)

#   todo Work
def Work(query):
        Speak("Ok sir ! Tell me what is our new work")
        Work = TakeCommand().lower()
        print(Work)
        Speak("New work added sussessfully!")
        theTask = open('Data\\Work.txt','w')
        theTask.write(Work)
        theTask.close()

#   todo Working on
def WorkingOn(query):
        # Speak("Sir we are recently working on ")
        Working = open('Data\\Work.txt','r')
        Speak("We are currently working on"+ Working.read())
        Workpath = "E:\\Projects\\Advance AI\\Data\\Work.txt"
        os.startfile(Workpath)

#   todo  Idea
def Idea(query):
    if 'new' in query:        
        Speak("Its good to here that sir You got new idea")
        Speak("Please tell me the idea")
        Idea = TakeCommand().lower()
        print(Idea)
        Speak("Added Successfully!")
        theIdea = open('Data\\Ideas.txt','a')
        theIdea.write(">\t" + Idea + "\n")
        theIdea.close()

    elif 'show' in query:
        Speak("Showing Ideas file")
        IDEA = "E:\\Projects\\Advance AI\\Data\\Ideas.txt"
        os.startfile(IDEA)

#   todo Calender
def Calender(query):
    if 'month' in query:
        year = 2022
        month = 1
        print(calendar.month(year, month))
        Speak('Showing Calendar')

    elif 'year' in query:
        year = 2022
        print(calendar.calendar(year))
        Speak('Showing Calendar')

def AudioBook(query):
    pdf = input(str("Enter PDF Path : "))
    book = open(pdf,'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    Speak(f"Tatal number of pages in this Book is {pages} .")
    Speak("Sir , Please tell me page number where I have to start.")
    pageNo = int(input("Please Enter Page Number : "))
    page = pdfReader.getPage(pageNo)
    text = page.extractText()
    Speak(text)

def News(query):
    Speak("Searching for latest news...")
    googlenews = GoogleNews()
    googlenews = GoogleNews(period='1d')
    googlenews.search('Maharastra')
    result = googlenews.result()
    Speak("Here is result Sir...")

    for x in result:
        print("-"*50)
        print("Title--",x['title'])
        print("Date/Time--",x['date'])
        print("Description--",x['desc'])
        print("Link--",x['link'])

def PhoneNo(query):
    MobNo = input("Enter mobile number with country code : ")
    MobNo = phonenumbers.parse(MobNo)
    print(timezone.time_zones_for_number(MobNo))
    print(carrier.name_for_number(MobNo,"en"))
    print(geocoder.description_for_number(MobNo,"en"))
    print("Valid Mobile Number : ",phonenumbers.is_valid_number(MobNo))
    print("Checking possibility of Number : ",phonenumbers.is_possible_number(MobNo))
