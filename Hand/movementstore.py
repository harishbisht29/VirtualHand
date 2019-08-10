from os.path import exists

class MovementStore:

    dlm = "__"
    handle = None
    output = "None"

    def __init__(self,output):

        self.output = output
        if(exists(output)):
            print("Output Object Already Exists!! Overwriting It..");
            self.handle = open(self.output, 'w+')
            self.handle.close()


    def store(self, atype, action, details, time):
        time = str(time)
        print(self.dlm)
        self.handle = open(self.output,"a+")
        towrite = atype + self.dlm + action + self.dlm + details + self.dlm + time + "\n";
        self.handle.write(towrite)

    def close(self):
        self.handle.close()

    def __del__(self):
        print ("destructor....called")
        self.handle.close()
