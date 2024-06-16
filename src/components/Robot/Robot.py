import sys
import time
import random
import keyboard
import pyautogui
import customtkinter as ctk
from datetime import datetime

class Robot:
    robotCount = 0
    robotObj = []
    robotLoop = False

    def __init__(self, obj = []):
        self.ly= obj.ly  
        self.SleepContainer = None
        self.text = None
            
    def Robot(self):
        self.robotLoop = True
        self.RobotStart()

    def printStatus(self, textContent):

        if self.SleepContainer is None:
            self.SleepContainer = ctk.CTkFrame(
                self.ly.rightMD,
                width=self.ly.rightWidth,
                height=100,
                fg_color="transparent",
            )
            self.SleepContainer.pack(
                fill="x", pady=20
            )

            self.text = ctk.CTkLabel(
                self.SleepContainer,
                width=self.ly.rightWidth,
                wraplength=self.ly.rightWidth,
                text=str(textContent)
            )
            self.text.pack()
        else:
            self.text.configure(text=str(textContent)) 
       
    def RobotStart(self):
        
        self.AutomateActions()

        while self.robotLoop == True:
            if self.robotCount > sys.getrecursionlimit() - 100:
                self.StopTheRobot()

            self.printStatus(f'em execução {self.robotCount}')
            self.robotCount += 1
            self.RobotStart()
    
    def StopTheRobot(self):
        self.robotCount = 0
        self.robotLoop = False
        self.printStatus("Loop ended!")
        
    def AutomateActions(self):       
        interval = 0.1
        if 'data' in self.robotObj and 'keys' in self.robotObj['data']:

            for key in self.robotObj['data']['keys']:

                if not self.robotLoop:
                    break

                timer_default = 10

                if self.robotObj['data']['timer_default']:
                    timer_default = self.robotObj['data']['timer_default']

                if key['pressed']:
                    timer_default = key['pressed']

                if key['random'] and key['min'] and key['max']:
                    timer_default = self.rand(int(key['min']), int(key['max']))
                    self.printStatus(f"the key is {key['key']} an the random number is {int(timer_default)}")
            
                self.printStatus(f"init {datetime.now().minute}:{datetime.now().second}")

                if not key['key']:
                    continue

                self.printStatus(f"key: {key['key']}")

                if key['key'] == 'click':
                    rt1 = ctk.CTk()
                    width = rt1.winfo_screenwidth()
                    height = rt1.winfo_screenheight()

                    if key['random']:
                        m1 = int(self.rand(0,width - 1))
                        m2 = int(self.rand(50,height -50))
                    else:
                        m1 = 50
                        m2 = 50
                    self.printStatus(f'tela: {width}x{height} type: Click -> 2 seconds for the random click -> {m1} x {m2} ')
                    pyautogui.click(m1, m2, duration=2)
                else:
                    if key['onetap']:
                        time.sleep(2)
                        keyboard.press(key['key'])
                        time.sleep(interval)
                        keyboard.release(key['key'])
                        time.sleep(int(timer_default))
                    
                    else:
                        startTime = time.time()
                        while time.time() - startTime < int(timer_default):
                            if not self.robotLoop:
                                break

                            keyboard.press(key['key'])
                            time.sleep(interval)
                            keyboard.release(key['key'])

                        self.printStatus(f"The end : {datetime.now().minute}:{datetime.now().second}")
    
    def rand(self, minimo, maximo):
        return random.uniform(minimo, maximo)