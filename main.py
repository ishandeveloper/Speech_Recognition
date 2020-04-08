import speech_recognition as sr

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

print('How Can I Help You ?')
voice_data=listen_audio()
print(voice_data)
        

        