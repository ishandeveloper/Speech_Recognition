from time import ctime
from listener import listen_audio
import webbrowser
from outputs import say


def respond(voice_data):
    if 'what is your name' in voice_data:
        say("Hey, I'm Jarvis.")
    if 'time' in voice_data:
        say(ctime())
    if 'search' in voice_data:
        say('What do you want to search for?')
        search=listen_audio()
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        say("Here's what I found for "+search)
    if ('find location' or 'search for location' or 'the location' or 'find place') in voice_data:
        say('What Is The Location?')
        location=listen_audio()
        url='https://google.com/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        say("Here's The Location Of "+location)
    if 'exit' or 'stop listening' in voice_data:
        exit()

 
