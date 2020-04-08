from responses import respond
from listener import listen_audio
from outputs import say

say("How Can I Help You ?")
voice_data=listen_audio()
respond(voice_data)

        

        