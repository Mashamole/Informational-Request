
from newsapi import NewsApiClient
import calendar
from time import gmtime, strftime, localtime
import time
import wikipedia
import wolframalpha
import pyttsx3
import speech_recognition as sr
import pprintpp


client = wolframalpha.Client('TQEPQQ-G68H4RU9U3 ')


"""
engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
# VOICE
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# changing index, changes voices. 1 for female
engine.setProperty('voice', voices[1].id)

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()


engine.say("Welcome to BetaBot 1")
engine.runAndWait()





while True:
    query = str(input('Enter query: '))
    res = client.query(query)
    output = next(res.results).text
    speakText = str(output)
    engine.say(speakText)
    engine.runAndWait()



engine.stop()

"""


class BetaBot1():

    def __init__(self, arg_name):
        self.name = arg_name

    def getName(self):
        return self.name

    def Welcome(self):
        engine = pyttsx3.init()
        # getting details of current voice
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say("Welcome {0}".format(self.getName()))
        engine.say("it is")
        timet = strftime("%A, %B %d %Y %I:%M:%S", localtime())
        toText = str(timet)
        engine.say(toText)
        engine.runAndWait()

    def action(self):
        engine = pyttsx3.init()
        # getting details of current voice
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say("Choose one of the options listed below")
        engine.say(
            "The options are finance, knowledge of the world and people, or mathmatical calculations")
        engine.runAndWait()
        while True:
            print()
            print()

    def wikipedia(self):
        while(True):
             user_input = input("Question: ")
             if user_input == 'quit' or user_input == 'q':
                break
             print(wikipedia.summary(user_input, sentences=5))

    def options(self):
        print("1: search'\n'")
        print()


try:
    BetaRun = BetaBot1("Marcus")
    BetaRun.Welcome()
    BetaRun.action()
    while(True):
        #query = ""
        query = str(input("Enter: "))
        if query == "":
            continue
        if query == "wiki":
            BetaRun.wikipedia()
except:
    print("Error starting Bot")
# while(True):


#
# BetaRun.action()


#print(strftime("%A, %B %d %Y %I:%M:%S",localtime()))


# Init
newsapi = NewsApiClient(api_key='7c57b65cc4e34349a2244c8d39d3289b')


sources = newsapi.get_sources(category='Trump', language='en', country='us')
# print(all_articles)
pprintpp.pprint(sources)

# MongoDB call to Database for user profiles
#
"""
import pymongo

client = pymongo.MongoClient("mongodb+srv://Kelchi:<Lechi110!>@betacluster-2ddcy.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

print(db)

"""

"""
while True:

    user_input = input("Question: ")
    if user_input == 'quit' or user_input == 'q':
        break
    print(wikipedia.summary(user_input, sentences=5))


r = sr.Recognizer()

with sr.Microphone() as source:

    print("Say something!")

    audio = r.listen(source)
"""

"""
# recognize speech using Sphinx

try:

    print("Sphinx thinks you said " + r.recognize_sphinx(audio))

except sr.UnknownValueError:

    print("Sphinx could not understand audio")

except sr.RequestError as e:

    print("Sphinx error; {0}".format(e))

"""
# Speech to Text Functionality
""" 
r = sr.Recognizer()

with sr.Microphone() as source: 
    print('Speak: ')
    audio = r.listen(source)

    try: 
        text = r.recognize_google(audio)
        print('you said: {}'.format(text))
    except:
        print("did not recognize:")

"""
