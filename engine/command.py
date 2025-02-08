import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    engine = pyttsx3.init('sapi5') #initializing pyttsx3
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female 0 for male
    engine.setProperty('rate', 174)     # setting up new voice rate
    eel.DisplayMessage(text)

    engine.say(text) #says the text
    engine.runAndWait() #waits for sometime while speaking


def takecommand():

    r = sr.Recognizer() #initialize the sr

    with sr.Microphone() as source: #taking input from microphone
        print("listening....")
        eel.DisplayMessage("listening....") #displays listening in frontend
        r.pause_threshold = 1 #pauses for 1 second
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 20, 20) # it listen for atleast 20sec if user speaks it listen for 20sec

    try: #converts speech to text
        print("recognizing")
        eel.DisplayMessage("recognizing....") #displays recognizing in frontend

        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")  #f is formatted string
        eel.DisplayMessage(query)
        time.sleep(2) #delay some time

    except Exception as e:
        return ""
    
    return query.lower() #return query in lower case

@eel.expose # now we can access from main.js
def allCommands():

    try:
        query = takecommand()
        print(query)

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            print("not run")
    except:
        print("error")
    eel.ShowHood()


