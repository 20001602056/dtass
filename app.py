import pyttsx3
from pywhatkit.mail import send_hmail 
import speech_recognition as sr  
import datetime      
import os     
import cv2
import random
import wikipedia    
from requests import get
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wish():
        hour =int(datetime.datetime.now().hour)
        if hour>=8 and hour<=12:
            speak("good morning")
        elif hour>12 and hour<18:
            speak("good afternoon")
        else:
            speak("good evening")
        speak("Hello, How can i help you")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('hs9450331@gmail.com','mailpassword')
    server.sendmail("hs9450331@gmail.com",to,content)
    server.close

 
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source,timeout=30000,phrase_time_limit=30000)

    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said {query}")
    except Exception as e:
        return "none"
    query = query.lower()
    return query

def TaskExecution():
    wish()
    while True:
        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        elif "close notepad" in query:
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe") 

        elif "hide files" in query or "hide folder" in query or "visiable for everyone"in query:
            speak("tell me what you want to hide or make it visible")
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("The files or folder are hidden")
            elif "visible" in condition:
                os.system("All files or folder are visible")

            elif "leave it" in condition or "leave for now" in condition:
                speak("ok")

        elif " shutdown"in query:
            os.system("shutdown /s /t 5")

        elif "restart"in query:
            os.system("shutdown /r /t 5")

        elif "sleep" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        
        elif "open cmd"in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k= cv2.waitKey(50)
                if k==27:
                    break
                cap.realease()
                cv2.destroyAllWindows()
        elif "play music"in query:
            music_dir = "E:\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "joke" in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            speak(My_joke)

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "open linkedin" in query:
            webbrowser.open("www.linkedin.com")
        elif "open google" in query:
            webbrowser.open("www.google.com")
        elif "open twitter" in query:
            webbrowser.open("www.twitter.com")
        elif "open amazon" in query:
            webbrowser.open("www.amazon.in")
        elif "open flipkart" in query:
            webbrowser.open("www.flipkart.com")
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com")
        elif "open netfilx" in query:
            webbrowser.open("www.netflix.com")
        elif "open zoom" in query:
            webbrowser.open("www.zoom.us")
        elif "open meet" in query or "open google meet" in query:
            webbrowser.open("https://meet.google.com")
        elif "open office" in query:
            webbrowser.open("www.office.com")
        elif "open outlook" in query:
            webbrowser.open("www.outlook.com")
        elif "open quora" in query:
            webbrowser.open("www.quora.com")

        elif "search google" in query:
            speak("what should i search on google ")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+918398945887","this is for testing",8,35)

        elif "email" in query:
            try:
                speak("what should i send?")
                content = takecommand().lower()
                to="himanshu.sharmav45@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("mail not send")
        elif "news"in query:
            speak("News Feteching")

        elif "no thanks"in query:
            speak("Thanks for using")
            os.system("taskkill/f /im figma.exe")
            sys.exit()

        elif "hello" in query or "hey" in query:
            speak("Hello,may i help you")

        elif "how are you" in query:
            speak("I am fine what about you")
        


        speak("Any other thing you want to search")

if __name__=="__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission:
            TaskExecution()
        elif "goodbye" in permission:
            sys.exit()
