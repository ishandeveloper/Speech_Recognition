import speech_recognition as sr
from time import ctime
r=sr.Recognizer()

def listen_audio():
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            print("I didn't get that")
        except sr.RequestError:
            print('Sorry, Speech Service Is Down')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print("Hey, I'm Jarvis.")
    if 'time' in voice_data:
        print(ctime())

print("Jarvis >> How Can I Help You ?")
voice_data=listen_audio()
print("You    >> "+voice_data)
respond(voice_data)

        

        