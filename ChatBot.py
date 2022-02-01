import random

Hello = ['hey','hello','hi']

Replay_Hello = ['Hello sir ! I am Friday.How are You ?','Hello sir, Good to see you again,How are You ?','Whats up sir,How are You ?','How are you Sir,How can I help You ?']

Fine = ['i am fine','good','better','nice','working','great']

Replay_Fine = ['Thats good to hear you sir!','Sir ! Thats really nice.','Good to hear that Sir!','Sir, Thats great','Its good to know Sir .']

How_Are_You = ['whats up','how are you doing','are you fine','ok','are you ok']

Replay_HowAreYou = ['I am good sir','Just great Sir','I am Fine Sir,Thanks for Asking','All systems are running perfect']

Features = ['features','capabilities','abilities']

Replay_Features = ['Sir I can perform many works for you','I can do all thanks that you implemented inside me','I can do google for you,open apps,play music,etc','I Can Message Your Mom That You Are Not Studing.','Let Me Ask You First , How Can I Help You ?',
'If You Want Me To Tell My Features , Call : Print Features !']

Sorry = ['Command not recognized','I am unable to do that Sir','I am unable to get that sir','Sorry sir I cannot get that','Task not defined','Say that again please']

Print_feature = 'Can tell time,date,location.\nCan tell temperature of area as well as any location.\nCan Write a note for you.\nIt has a costum command which tell us about day.\nIt can tell which class is going on according to time and day.\nIt can also perform methamatical calculations of 2 variables.\nIt has ability to make google search and speak.\nIt can search a query on youtube and can play first video.\nIt can remember a query and tell us when asked.\nIt can tell us our IP Address\nIt can take a screenshot and save it at specific folder.\nIt can play music.\nI addede a special how to do mode which can tell us result in stepwise manner.\nIt has chrome automation can automate features like google search, switch tab, bookmarks ,open downloads , open & close new tab,open new window,show history.\nCan open websites like Youtube,Instagram,FaceBook,Discord.\nIt has some randomization features like \n>coin toss\n>throw dice\n>select random numbers.\nIt has a special feature It can read pdf for us.\nSome extra features like password generator,QR Code generator.'

def ChatterBot(Text):

        if 'hey' in Text or 'hello' in Text or 'hii' in Text:
            return random.choice(Replay_Hello)

        elif 'i am fine' in Text or 'i am good' in Text or 'better' in Text or 'nice' in Text or 'working' in Text or 'great' in Text:
            return random.choice(Replay_Fine)

        elif 'whats up' in Text or 'how are you doing' in Text or 'are you fine' in Text or 'ok' in Text or 'are you ok' in Text:
            return random.choice(Replay_HowAreYou)

        elif 'features' in Text or 'capabilities' in Text or 'capabilities' in Text:
            return random.choice(Replay_Features)

        elif 'print features' in Text:
            return Print_feature

        else:
            return random.choice(Sorry)