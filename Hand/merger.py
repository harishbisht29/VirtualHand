from os.path import exists
def getRecording():
    fmouse = open("mouse")
    fkeyboard = open("keyboard")

    if(exists("recording")):
        global recording
        print("Output Object Already Exists!! Overwriting It..");
        recording = open("recording", 'w+')
        recording.close()

    recording = open("recording","a+")

    lmouse = fmouse.readline()
    lkeyboard = fkeyboard.readline()

    while( lmouse != "" and lkeyboard != ""):
        if(float(lmouse.split("__")[3]) > float(lkeyboard.split("__")[3])):
            recording.write(lkeyboard)
            lkeyboard = fkeyboard.readline()
        else:
            recording.write(lmouse)
            lmouse = fmouse.readline()
    if(lmouse == ""):
        while(lkeyboard != ""):
            recording.write(lkeyboard)
            lkeyboard = fkeyboard.readline()
    recording.close()
