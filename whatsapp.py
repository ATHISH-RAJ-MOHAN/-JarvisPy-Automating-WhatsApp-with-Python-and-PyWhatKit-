import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
voices=engine.setProperty('voice',voices[0].id)


def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def takeCommand():
  #it takes microphone input from the use and retuns string output

  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening.....")
    r.pause_threshold=1 #i need 1sec gap in b|w to speak
    audio = r.listen(source)

  try:
       print("Recognising.......")
       query=r.recognize_google(audio, language="En-In") 
       print(f"User said: {query}\n")

  except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"
  return query
strTime=int(datetime.now().strftime("%H"))
update=int((datetime.now()+timedelta(minutes=2)).strftime("%M"))

def sendMessage():
   speak("who do you want to send message")

   speak("whats the message")
   message=str(input("enter the message"))
   pywhatkit.sendwhatmsg("+91 phone-number",message,time_hour=strTime,time_min=update)
   pass
   
    
   