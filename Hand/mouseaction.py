import pyautogui
from timetrack import *

pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = False

class mouseaction:
    last_time = None;

    def __init__(self, t):
        self.last_time = t;
    def moveTo(self,x, y, time):
        pyautogui.moveTo( x, y, duration = time - self.last_time.getTime())
    def act(self, action, payload, time):

        x = int(payload.replace("(","").replace(")","").split(",")[0])
        y = int(payload.replace("(","").replace(")","").split(",")[1])
        if( self.last_time.getTime() == -1):
            self.last_time.setTime(float(time))

        self.moveTo(x, y, float(time))

        if(action == "LP"):
            pyautogui.mouseDown(button = 'left')
        elif(action == "LR"):
            pyautogui.mouseUp(button = 'left')
        elif(action == "RP"):
            pyautogui.mouseDown(button = 'right')
        elif(action == "RR"):
            pyautogui.mouseUp(button = 'right')
        self.last_time.setTime(float(time))


if __name__ == '__main__':
    timetrack = timetrack(-1)
    ma = mouseaction(timetrack)
    ma.act("MM","(500,500)",1566);
    ma.act("RP","(600,600)",1570);
