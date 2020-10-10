
from time import time
import pyttsx3
# thư viện hổ trợ chuyển đổi từ text sang giọng nói qua audio
import speech_recognition
# thư viện hổ trợ nghe giọng nói mà dịch ra text.
from datetime import date, datetime

def audioToText():
    siri_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
         #print("Siri : I'm Listening")
         audio = siri_ear.listen(mic)
    try:
        you = siri_ear.recognize_google(audio)
    except: 
        you = ""
    return you
def textToAudio(siri_brain):
    siri_speak = pyttsx3.init()
    print("Processing, please wait...")
    siri_speak.say(siri_brain)
    print("Siri: " + siri_brain)
    siri_speak.runAndWait()
def getDate():
    today = date.today()
    d = today.strftime("%B %d, %Y")
    return d
def getTime():
    now = datetime.now()
    t = now.strftime("%H hours %M minutes %S seconds")
    return t
while True:    
    you = audioToText()
    siri_brain = ""
         
    if  "hello" in you:
        siri_brain = "Hello Duc"
    elif "who are you" in you:
        siri_brain = "I'm robot"
    elif "today" in you:
         siri_brain = getDate()
    elif "time" in you:
        siri_brain = getTime()
    elif "handsome" in you:
        siri_brain = "yes very handsome"
    elif "bye" in you:
        print("Good Bye")
        textToAudio("good bye see you again")
        break
    else :
        siri_brain = "I can't hear you, try again"
    print("You: " + you)
    textToAudio(siri_brain)


