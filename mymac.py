import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

f=open("pass.txt")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)

password = f.read()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=6 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am MAC, how may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say it again please...")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("neelaksh10singh@gmail.com", password)
    server.sendmail("neelaksh10singh@gmail.com", to, content)
    server.close()

def findfile(filename, path):
    for root, dir, files in os.walk(path):
        if filename in files:
            return os.path.join(root, filename)


if __name__ == '__main__':
    chromepath= "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    Wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            try:
                speak("Searching wikipedia...")
                query=query.replace("wikipedia", "")
                results= wikipedia.summary(query, sentences= 2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except:
                print("Can't find your requested result. Search again with a different keyword.")
                speak("Can't find your requested result. Search again with a different keyword.")


        elif 'open youtube' in query:
            webbrowser.get(chromepath).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chromepath).open("google.com")

        elif 'open instagram' in query:
            webbrowser.get(chromepath).open("instagram.com")

        elif 'open codechef' in query:
            webbrowser.get(chromepath).open("codechef.com")

        elif 'open geeks for geeks' in query:
            webbrowser.get(chromepath).open("geeksforgeeks.org")

        elif 'open stack overflow' in query:
            webbrowser.get(chromepath).open("stackoverflow.com")

        elif 'open quora' in query:
            webbrowser.get(chromepath).open("quora.com")

        elif 'open chrome' in query:
            os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")

        elif 'open notepad' in query:
            os.startfile("C:/Windows/notepad.exe")

        elif 'open python editor' in query:
            os.startfile("C:/Windows/py.exe")

        elif 'open telegram' in query:
            os.startfile("C:/Users/91910/AppData/Roaming/Telegram Desktop/Telegram.exe")

        elif 'play music' in query:
            music_dir='C:/Files/songs'
            songs= os.listdir(music_dir)
            num= random.randint(0, (len(songs)-1))
            os.startfile(os.path.join(music_dir, songs[num]))

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

        elif 'the date'in query:
            strdate=datetime.date.today().strftime("%B %d, %y")
            speak(f"Today's date is {strdate}")

        elif 'send email' in query or 'send an email' in query:
            try:
                speak("Whom should I send email to?")
                address=takeCommand().lower()
                speak("What should I say?")
                content = takeCommand()
                sendEmail(address, content)
                speak("Email has been sent!")
            except:
                speak("Sorry sir! I am not able to send email.")

        elif 'shutdown computer' in query or 'shutdown system' in query:
            speak("Do you really want to shutdown your pc?")
            content= takeCommand().lower()
            if 'yes' in content:
                os.system("shutdown /s /t 1")
            else:
                speak("Can't shutdown your pc.")

        elif 'see a movie' in query or 'watch a movie' in query:
            try:
                speak("Which movie would you like to watch?")
                moviename=takeCommand().lower()
                addressmovie = findfile(f"{moviename}.mkv", "C:/Files/movies")
                os.startfile(addressmovie)
            except:
                speak("Can't find your requested movie.")

