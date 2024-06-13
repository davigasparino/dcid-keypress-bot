import os

class Logs:
    def __init__(self):
        self.logsFile = os.path.join(os.getcwd()+'/data','logs.txt')

    def addLog(self, logItem):
        print(" --------------------------------------------- ")
        print('logItem => ', logItem)
        print('logsFile => ', self.logsFile)
        print(" --------------------------------------------- ")
        with open(self.logsFile, 'a') as row:
            row.write( logItem +'\n')