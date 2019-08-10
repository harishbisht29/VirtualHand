import os
from multiprocessing import Process
from mouselistener import *
from keyboardlistener import *
def recordMouse():
    ml = MouseListener("mouse")
    with mouse.Listener( on_click=ml.on_click, on_move=ml.on_move) as listener:
        try:
            listener.join()
        except MyException as e:
            print('{0} was clicked'.format(e.args[0]))

def recordKeyboard():
    kl = KeyListener("keyboard")
    with keyboard.Listener( on_press=kl.on_press, on_release=kl.on_release) as listener:
        try:
            listener.join()
        except MyException as e:
            print('{0} was pressed'.format(e.args[0]))

p1 = Process(target= recordMouse)
p2 = Process(target = recordKeyboard)

p1.start()
p2.start()

p1.join()
p2.join()
