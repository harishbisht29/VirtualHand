from pynput import keyboard
from time import time
from movementstore import *
# This class will store the keystrokes to output.
class KeyListener:
    output = None
    atype = None
    action = None
    details = None
    t = None
    handle = None
    def __init__(self, output):
        self.output = output
        self.atype = "K"
        self.handle = MovementStore(self.output)
    def on_press(self, key):
        self.action = "KP"
        try:
            self.details = key.char
        except:
            self.details = str(key)

        self.t = time()
        print( self.atype + " " + self.action + " " + self.details + " " +str(self.t))
        self.store_to_output();

    def on_release(self, key):
        self.action = "KR"
        try:
            self.details = key.char
        except:
            self.details = str(key)

        self.t = time()
        print( self.atype + " " + self.action + " " + self.details + " " +str(self.t))
        self.store_to_output();


    def store_to_output(self):
        self.handle.store(self.atype, self.action, self.details, self.t)

class MyException(Exception): pass



if __name__ == '__main__':
    kl = KeyListener("keyboard")
    with keyboard.Listener( on_press=kl.on_press, on_release=kl.on_release) as listener:
        try:
            listener.join()
        except MyException as e:
            print('{0} was pressed'.format(e.args[0]))
