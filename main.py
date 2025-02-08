import os
import eel
from engine.features import *
from engine.command import * #imports all functions of command.py



def start():
    eel.init("www")

    playAssistantSound()



    os.system('start msedge.exe --app="http://localhost:8000/index.html"') #opens in app mode

    eel.start('index.html', mode=None, host='localhost', block=True)