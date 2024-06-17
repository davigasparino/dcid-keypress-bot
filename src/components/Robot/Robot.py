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
        self.widthScreen = obj.widthScreen
        self.heightScreen = obj.heightScreen       
        
        self.setWidth = int(self.ly.rightWidth/2)
        
        self.SleepContainer = None
        self.botAction = None
        self.botStart = None
            
    def Robot(self):
        self.robotLoop = True
        self.RobotStart()

    def printStatus(self, textContent):
        try:
            if self.SleepContainer is None:
                self.SleepContainer = ctk.CTkFrame(
                    self.ly.rightMD2,
                    width=self.ly.rightWidth
                )
                self.SleepContainer.pack(
                    fill="x", pady=20
                )

                self.addLabel(
                    self.SleepContainer,
                    text="Key: "
                )

                self.botAction = ctk.CTkLabel(
                    self.SleepContainer,
                    width=self.setWidth,
                    wraplength=self.setWidth,
                    text=str(textContent),
                    font=("Tahoma", 22),
                    text_color="Green",
                    fg_color="black",
                )
                self.botAction.pack(side=ctk.LEFT, padx=5)
            else:
                self.botAction.configure(text=str(textContent)) 
        except Exception as e:
            self.SleepContainer = None
            self.botAction = None
            print("erro => ", e)
    
    def addLabel(self, container, text):
        self.Label = ctk.CTkLabel(
            container,
            width=self.setWidth,
            wraplength=self.setWidth,
            text=text
        )
        self.Label.pack(side=ctk.LEFT)

    def RobotStart(self):
        
        self.AutomateActions()

        while self.robotLoop == True:
            if self.robotCount > sys.getrecursionlimit() - 100:
                self.StopTheRobot()

            self.printStatus(self.robotCount)
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
                    self.printStatus(key['key'])
            
                #self.printStatus(f"init {datetime.now().minute}:{datetime.now().second}")

                if not key['key']:
                    continue

                self.printStatus(key['key'])

                if key['key'] == 'click':
                    
                    

                    if key['random']:
                        m1 = int(self.rand(0,self.widthScreen - 1))
                        m2 = int(self.rand(50,self.heightScreen -50))
                    else:
                        m1 = 50
                        m2 = 50
                        
                    # self.printStatus(f'tela: {self.widthScreen}x{self.heightScreen} type: Click -> 2 seconds for the random click -> {m1} x {m2} ')
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

                        # self.printStatus(f"The end : {datetime.now().minute}:{datetime.now().second}")
    
    def rand(self, minimo, maximo):
        return random.uniform(minimo, maximo)