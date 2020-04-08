from responses import respond
from listener import listen_audio
from outputs import say
import time

def listeningloop():
    time.sleep(1)
    say("How Can I Help You ?")
    while 1:
        voice_data=listen_audio()
        respond(voice_data)
        

listeningloop()

        