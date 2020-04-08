import playsound
import os
import random
from gtts import gTTS


def say(response):
    tts=gTTS(str(response),lang='en')
    r=random.randint(1,1000000)
    audio_file='audio-'+str(r) + '.mp3';
    tts.save(audio_file)
    print('Jarvis >> '+response)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def heard(response):
    print("You    >> "+response)