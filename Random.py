import random
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()

#! ------------------Toss a coin---------------------#
def TossCoin(query):
    CoinToss = ['Head','Tail']
    Coin = random.choice(CoinToss)
    Speak("Its "+ Coin + " sir!")


#! ------------------Throw a dice---------------------#
def ThrowDice(query):
    DiceSide = ['1','2','3','4','5','6']
    Dice = random.choice(DiceSide)
    Speak("Its number " +Dice+ " sir!")

#! ------------------Random number---------------------#
def RandomNumber(query):
        Number = str(random.randint(1, 100))
        Speak("its number "+Number+ " sir")