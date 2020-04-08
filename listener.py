import speech_recognition as sr
from outputs import *
import time
from responses import *

r=sr.Recognizer()



def listen_audio():
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            say("I didn't get that")
        except sr.RequestError:
            say('Sorry, Speech Service Is Down')
        
        heard(voice_data)
        return voice_data
