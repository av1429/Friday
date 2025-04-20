import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import randfacts
import random
from datetime import date
from datetime import time
import requests
from bs4 import BeautifulSoup
import os
from pywikihow import search_wikihow
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            a=["i'm listening","i'm all ears","i'm hearing","what do you want"]
            print("i'm listening.... ")
            b=random.choice(a)
            talk(b)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '')
                talk(command)
    except:
        pass
    return command

def runfriday():
        command = take_command()
        print(f'did you ask about \'{command}\'?')

        if 'play' in command:
            song = command.replace('play', '')
            talk('playing..' + song)
            pywhatkit.playonyt(song)

        elif 'open youtube' in command:
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            webbrowser.open("google.com")

        elif 'open mail' in command:
            webbrowser.open("gmail.com")

        elif 'open spotify' in command:
            webbrowser.open("spotify.com")

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time)
            talk('current time is' + time)
        
        elif 'date' in command:
            today=date.today()
            print(today.strftime("%d/%B/%Y"))
            talk(today)

        elif 'what do you got about' in command:
            person = command.replace('tell me about', '')
            info = wikipedia.summary(person)
            print(info)
            talk(info)

        elif 'what do you know about' in command:
            person = command.replace('tell me about', '')
            info = wikipedia.summary(person)
            print(info)
            talk(info)

        elif 'what do you have about' in command:
            person = command.replace('tell me about', '')
            info = wikipedia.summary(person)
            print(info)
            talk(info)

        elif "activate how to mod" in command:
            talk("how to mode is activated")
            while True:
                talk(" please tell me what do you want to know")
                how=take_command()
                try :
                    if 'exit' in how or 'close' in how:
                        talk("how to do mode is closed")
                        break
                    else:
                        max_results=1
                        how_to=search_wikihow(how, max_results)
                        assert len(how_to)==1
                        how_to[0].print()
                        talk(how_to[0].summary)
                except Exception as e:
                    talk(" sorry, i am not able to find this")

        elif 'joke' in command:
            talk(pyjokes.get_joke())

        elif "i didn't get your joke" in command:
            talk("i am improvising day by day, please bare with me")

        elif 'fact' in command:
            talk(randfacts.get_fact())

        elif 'remind' in command:
            talk("when do you want me to remind")
            remindertime=take_command()
            talk("I will remind you at")
            talk(remindertime)
            while True:
                timeat= datetime.datetime.now()
                now=timeat.strftime("%H:%M")
                if now ==remindertime:
                    talk("reminderrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
                    talk(command)

                elif now>remindertime:
                    break
          
        elif 'weather' in command:
           search='temperature in karaikudi'
           url=f"https://www.google.com/search?q={search}"
           r=requests.get(url)
           data=BeautifulSoup(r.text,"html.parser")
           temp=data.find("div",class_="BNeawe").text
           talk("current weather at karaikudi is")
           talk(temp)

        elif 'remember that' in command:
            remembermsg = command.replace('remember that','')
            remembermsg = command.replace('friday','')
            talk("you told me to remember :")
            talk(remembermsg)
            remember=open('data.txt','a')
            remember.write(remembermsg+'\n')
            remember.close()

        elif 'what do you remember' in command:
            remember1=open('data.txt','r')
            talk("you told me to remember :")
            talk(remember1.read())
            remember1.close()

            
        elif "good girl" in command:
            talk("i love you 3000")

        elif "who are you" in command:
            talk("Hi I'm FRIDAY. An AI, created by Aravinth. I will be helpful for playing any songs on Youtube, giving you info about any person,place,thing,object,anything that is available in Wikipedia. I can even tell you the date, time, current weather of Karaikudi. I can even remind with alarms. I can even remember whatever you want me to remember and will tell you everything whenever you ask me. If you’re bored, feel free to ask any joke or fact. Just say “Hey Friday!”" )

        else:
            talk("i didn't get you, say hey friday")

while True :
    runfriday()

        

