import time
from responses import *
from listener import *

def start():
    time.sleep(1)
    say("How Can I Help You ?")
    while 1:
        voice_data=listen_audio()
        respond(voice_data)

start()