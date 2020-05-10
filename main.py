#we are creating a desktop assistant and I have named it Tubai 2.0
import os
import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import keyboard
import sys

print("Welcome User! I am developed by Tubai! I am his assistant Tubai2.0")

engine=pyttsx3.init('sapi5')#object creation
engine.say("Welcome User! I am developed by Tubai! I am his assistant Tubai2.0")
engine.runAndWait()
volume=engine.getProperty('volume')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#this function allows to speak the given text when text is passed
def speak(text):
    engine.say(text)
    engine.runAndWait()

#this function will wish you ('user')
def wishuser():
    currenttime=datetime.datetime.now()
    hour=int(currenttime.strftime("%H"))
    if hour>0 and hour<12:
        speak("Good Morning User")
    elif hour>12 and hour<15:
        speak("Good Afternoon user")
    elif hour>15 and hour<19:
        speak("Good Evening user")
    else:
        speak("Great!Hope you had a good day!")


#let's begin with all the other stuffs!

def usercommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.phrase_threshold=0.5
        audio = r.listen(source)
        try:
             print("Recognising...")
             query = r.recognize_google(audio,language="en-US")
             print(f"{query}\n")
        except Exception as e:
             print("Sorry,Could not get you..Please Say again ")
             speak("Sorry,Could not get you..Please Say again ")
             query = None
        return query

speak('Hey pal,whatsapp!')
speak("What can I do for you??")
if __name__ == "__main__":
    wishuser()
    query = usercommand().lower()
    while(1):
      try:
        if 'open vlc' in query:
            speak("opening vlc for you..")
            print("opening vlc for you..")
            vlcpath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlcpath)
            break

        elif 'google' in query:
            speak("opening google for you")
            print("opening google for you")
            webbrowser.open_new("www.google.com")
            break
        elif 'vs code' in query:
            speak("opening vs code for you")
            print("opening vs code for you")
            vscodepath="C:\\Users\\Tubai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodepath)
            break
        elif 'wikipedia' in query:
            speak("Searching in wikipedia...")
            print("searching in wikipedia")
            search=wikipedia.summary(query,sentences=3)
            speak("As per wikipedia...")
            print(search)
            speak(search)
            break
        elif 'youtube' in query:
            speak("opening youtube")
            print("opening youtube")
            webbrowser.open_new("www.youtube.com")
            break
        else:
            print("Sorry , I cant do this....my master hasnt taught me this ")
            break
      except:
          if keyboard.is_pressed():
              sys.exit()
