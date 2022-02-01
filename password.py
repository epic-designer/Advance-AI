import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()

def Password(pass_inp):
    Password = "epic"

    Pass = str(Password)

    if Pass == str(pass_inp):
        Speak("Access Granted . ")
        import main

    else:
        Speak("Access Not Granted . ")

if __name__ == '__main__':
    Speak("This file is Password Protected . ")
    Speak("Please enter password to Access file")

    passsss = input('Please enter password : ')
    Speak("You entered \" "+passsss + " \" as a password.")
    print("You entered \" "+passsss + " \" as a password.")