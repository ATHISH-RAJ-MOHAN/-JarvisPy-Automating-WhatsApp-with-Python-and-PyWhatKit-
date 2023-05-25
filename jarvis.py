import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
voices=engine.setProperty('voice',voices[0].id)




def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def wishMe():
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good Morning!")
  elif  hour>=12 and hour<18:
    speak(" Good Afternoon!")
  else:
    speak("Good Evening!")

  speak("I am Jarvis sir please tell me how may i help you")
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

def sendEmail(to,content):
   server=smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.login('your@gmail.com','password')#mine...
   server.sendmail('yourmail.com',to,content)
   server.close()
if __name__=="__main__":
 wishMe()
 #while True:
 if 1:    
     query=takeCommand().lower()
    
    #logic for executing task based on query
     if 'wikipedia' in query:
        speak('Searching Wikipedia.......')
        query=query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
     
     elif 'open youtube' in query:
        webbrowser.open("youtube.com")

     elif 'open google' in query:
        webbrowser.open("google.com")

     elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
     
    # elif 'play music' in query:
    #     music_dir="D:\\Music\\Favrouite Songs"
    #     songs=os.listdir(music_dir)
    #     print(songs)
    #     os.startfile(os.path.join(music_dir,songs[0]))#to start playing 1st song
       
     elif 'the time' in query:
         stTime=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f" Sir, the time is{stTime}")
         
     elif 'open code' in query:
        codePath="C:\\Users\\yourname\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
     elif 'email to baby' in query:
        try:
           speak("what should i say?")
           content=takeCommand()
           to="your@gmail.com"
           sendEmail(to,content)
        except Exception as e:
           print(e)
           speak("not able to send e-mail")
 