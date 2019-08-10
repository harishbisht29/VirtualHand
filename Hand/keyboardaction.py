import pyautogui
from key_mappings import *
from pynput.keyboard import Key, Controller
import time as timer
from timetrack import *


class keyboardaction:
    last_time = None
    keyboard = None
    def __init__(self, t):
        self.last_time = t
        self.keyboard = Controller();
    def act(self, action, payload, time):
        if( payload.isalpha() ):
            payload = payload.lower()
        if( self.last_time.getTime() == -1):
            self.last_time.setTime(float(time))

        actionKey = key_mapping[payload]

        timer.sleep(float(time) - self.last_time.getTime())
        if(action == "KP"):
            self.keyboard.press(actionKey)
        elif(action == "KR"):
            self.keyboard.release(actionKey)
        self.last_time.setTime(float(time));


if __name__ == '__main__':
    timetrack = timetrack(-1)
    ka = keyboardaction(timetrack)
    ka.act("KP","h",1566);
    ka.act("KR","h",1570);
    ka.act("KP","a",1566);
    ka.act("KR","a",1570);
    ka.act("KP","Key.space",1566);
    ka.act("KR","Key.space",1570);
    ka.act("KP","r",1566);
    ka.act("KR","r",1570);
