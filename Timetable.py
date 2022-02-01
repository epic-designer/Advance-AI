import pyttsx3
from datetime import date
import calendar
import  datetime

#!      Setting up voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

#! --------------Speak Function--------------#
def Speak(audio):
    print(" ")
    print(f"FRIDAY : {audio}")
    engine.say(audio)
    engine.runAndWait()


def TimeTable(query):
    
    Date = datetime.datetime.now()
    Day = str(calendar.day_name[Date.weekday()])
    Time = datetime.datetime.now().strftime("%H:%M").replace(':','')
    Time = int(Time)

    #!  Monday
    if Day == 'Monday':
        if Time>=1145 and Time<=1230:
            Speak('Its time of C-English Class...')

        elif Time>=1230 and Time<=1315:
            Speak('Sir Its time of OS Class...')

        elif Time>=1315 and Time<=1345:
            Speak('Its time to take break Class...')
            # print('Its time to take break Class...')
            print('Abhi lunchtime hai badme aana\U0001F923')

        elif Time>=1345 and Time<=1430:
            # print('Boring...Stats Class')
            Speak('Boring...Stats Class')

        elif Time>=1430 and Time<=1515:
            # print('DM Class...')
            Speak('Sir Its time of DM Class...')

        elif Time>=1515 and Time<=1600:
            # print('Your favorite Class\n C Programming...')
            Speak('Its time of your favorite Class')
            Speak('C Programming')

        elif Time>=1600 and Time<=1745:
            Speak('Its time of CF Class...')
            # print('CF Class...')

        else:
            # print('There is no class at that schedule')
            Speak("Sir There is no class at that schedule")

    #!  Tuesday
    elif Day == 'Tuesday':
        if Time>=1145 and Time<=1230:
            Speak('Sir Its time for English Class...')

        elif Time>=1230 and Time<=1315:
            Speak('Sir Its time for OS Class...')

        elif Time>=1315 and Time<=1345:
            Speak('Its time to take break Class...')
            Speak('Abhi lunchtime hai badme aana\U0001F923')

        elif Time>=1345 and Time<=1430:
            Speak('Boring...Stats Class')

        elif Time>=1430 and Time<=1515:
            Speak('Sir Its time for DM Class...')

        elif Time>=1515 and Time<=1600:
            Speak('Sir Its time for Your favorite Class')
            Speak('C Programming...')

        elif Time>=1600 and Time<=1745:
            Speak('Sir Its time for CF Class...')

        else:
            Speak('There is no class at that schedule')

    #!  Wednesday
    elif Day == 'Wednesday':
        if Time>=1145 and Time<=1230:
            Speak('Sir Its time for English Class...')

        elif Time>=1230 and Time<=1315:
            Speak('OA Class...')

        elif Time>=1315 and Time<=1345:
            Speak('Its time to take break Class...')
            Speak('Abhi lunch time hai badme aana\U0001F923')

        elif Time>=1345 and Time<=1430:
            Speak('Boring...Stats Class')

        elif Time>=1430 and Time<=1515:
            Speak('Sir Its time for DM Class...')

        elif Time>=1515 and Time<=1600:
            Speak('Sir Its time for Your favorite Class')
            Speak('C Programming...')

        elif Time>=1600 and Time<=1745:
            Speak('Sir Its time for CF Class...')

        else:
            Speak('There is no class at that schedule')

    #!  Thursday
    elif Day == 'Thursday':
        if Time>=1145 and Time<=1230:
            Speak('Sir Its time for S-English Class...')

        elif Time>=1230 and Time<=1315:
            Speak('Sir Its time for OA Class...')

        elif Time>=1315 and Time<=1345:
            Speak('Its time to take break Class...')
            Speak('Abhi lunchtime hai badme aana\U0001F923')

        elif Time>=1345 and Time<=1430:
            Speak('Boring...Stats Class')

        elif Time>=1430 and Time<=1515:
            Speak('Sir Its time for DM Class...')

        elif Time>=1515 and Time<=1600:
            Speak('Sir Its time for Your favorite Class')
            Speak('C Programming...')

        elif Time>=1600 and Time<=1745:
            Speak('Sir Its time for CF Class...')

        else:
            Speak('There is no class at that schedule')

    #!  Friday
    elif Day == 'Friday':
        if Time>=1145 and Time<=1230:
            Speak('Sir Its time for S-English Class...')

        elif Time>=1230 and Time<=1315:
            Speak('Sir Its time for OA Class...')

        elif Time>=1315 and Time<=1345:
            Speak('Its time to take break Class...')
            Speak('Abhi lunchtime hai badme aana\U0001F923')

        elif Time>=1345 and Time<=1430:
            Speak('Boring...Stats Class')

        elif Time>=1430 and Time<=1515:
            Speak('Sir Its time for DM Class...')

        elif Time>=1515 and Time<=1600:
            Speak('Sir Its time for Your favorite Class')
            print('C Programming...')

        elif Time>=1600 and Time<=1745:
            Speak('Sir Its time for OS Class...')

        else:
            Speak('Sir Its time for There is no class at that schedule')

    #!  Saturday
    elif Day == 'Saturday':
        if Time>=1145 and Time<=1230:
            Speak('Sir Its time for S-English Class...')

        elif Time>=1230 and Time<=1315:
            Speak('Sir Its time for OA Class...')

        elif Time>=1315 and Time<=1345:
            Speak('Its time to take break Class...')
            Speak('Abhi lunchtime hai badme aana\U0001F923')

        elif Time>=1345 and Time<=1430:
            Speak('Boring...Stats Class')

        elif Time>=1430 and Time<=1515:
            Speak('Sir Its time for DM Class...')

        elif Time>=1515 and Time<=1600:
            Speak('Sir Its time for Your favorite Class')
            Speak('C Programming...')

        elif Time>=1600 and Time<=1745:
            Speak('Sir Its time for OS Class...')

        else:
            print('Sir! There is no class at that schedule')

    #!  Sunday  
    else:
        Speak('Today is Sunday sir!')
        Speak('There is No class Today')