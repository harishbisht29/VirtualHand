from movementstore import *
from keyboardaction import *
from mouseaction import *
from timetrack import *
from merger import *

getRecording()
t = timetrack(-1)
ka = keyboardaction(t)
ma = mouseaction(t)
for line in open("recording"):
    if(line.split("__")[0] == "K"):
        ka.act(line.split("__")[1],line.split("__")[2],line.split("__")[3])
    else:
        ma.act(line.split("__")[1],line.split("__")[2],line.split("__")[3])

