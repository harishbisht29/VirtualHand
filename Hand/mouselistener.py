from pynput import mouse
from time import time
from movementstore import *

class MouseListener:
    output = None
    atype = None
    action = None
    details = None
    t = None
    handle = None

    def __init__(self, output):
        self.output = output
        self.atype = "M"
        self.handle = MovementStore(self.output)
    def on_move(self, x, y):
        self.action = "MM"
        self.details ="(" + str(x) + "," + str(y) +")"
        self.t = time()
        print(self.atype + " " + self.action + " " + self.details + " " +str(self.t))
        self.store_to_output();

    def on_click(self, x, y, button, pressed):
        self.t = time()
        if(button == mouse.Button.left):
            self.action = "L"
        else:
            self.action = "R"
        if(pressed):
            self.action = self.action + "P"
        else:
            self.action = self.action + "R"
        self.details = "(" + str(x) + "," + str(y) +")"

        print( self.atype + " " + self.action + " " + self.details + " " +str(self.t))
        self.store_to_output();

    def store_to_output(self):
        self.handle.store(self.atype, self.action, self.details, self.t)

class MyException(Exception): pass



if __name__ == '__main__':
    ml = MouseListener("mouse")
    with mouse.Listener( on_click=ml.on_click, on_move=ml.on_move) as listener:
        try:
            listener.join()
        except MyException as e:
            print('{0} was clicked'.format(e.args[0]))
