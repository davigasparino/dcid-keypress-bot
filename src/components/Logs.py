import os
import datetime

class Logs:
    def __init__(self):
        self.logsFile = os.path.join(os.getcwd()+'/data','logs.txt')
        self.dateNow = datetime.datetime.now()
        # self.dateNow = self.dateNow.strftime('%Y-%m-%d %H:%M:%S')

    def addLog(self, logItem):
        with open(self.logsFile, 'a') as row:
            row.write( str(logItem) + '\n' + str(self.dateNow) +'\n')
            row.write(" --------------------------------------------- \n")