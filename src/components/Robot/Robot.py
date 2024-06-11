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

    def __init__(sel):
        return       
            
    def Robot(self):
        self.robotLoop = True
        self.RobotStart()
    
    def RobotStart(self):
        self.AutomateActions()

        while self.robotLoop == True:
            if self.robotCount > sys.getrecursionlimit() - 100:
                self.StopTheRobot()

            print(f'em execução {self.robotCount}')
            self.robotCount += 1
            self.RobotStart()
    
    def StopTheRobot(self):
        self.robotCount = 0
        self.robotLoop = False
        print("Loop interrompido!")
        
    def AutomateActions(self):
        print(' * - * - * - * - * - * - * - * - * - * - * - * ')
        print(self.robotObj)
        interval = 0.1
        if 'data' in self.robotObj and 'keys' in self.robotObj['data']:

            for key in self.robotObj['data']['keys']:

                timer_default = 10

                if self.robotObj['data']['timer_default']:
                    timer_default = self.robotObj['data']['timer_default']

                if key['pressed']:
                    timer_default = key['pressed']

                if key['random'] and key['min'] and key['max']:
                    timer_default = self.rand(int(key['min']), int(key['max']))
                    print(f"the key is {key['key']} an the random number is {int(timer_default)}")
            
                print(f"inicio em {datetime.now().minute}:{datetime.now().second}")
                
                if not key['key']:
                    continue

                print(key['key'])
                if key['key'] == 'click':
                    print('-----> CLICK')
                    rt1 = ctk.CTk()
                    width = rt1.winfo_screenwidth()
                    height = rt1.winfo_screenheight()
                    print(f"Largura da tela: {width} pixels")
                    print(f"Altura da tela: {height} pixels")

                    if key['random']:
                        m1 = int(self.rand(0,width - 1))
                        m2 = int(self.rand(50,height -50))
                    else:
                        m1 = 50
                        m2 = 50
                    print(f'em 2 segundos o click random {m1} e {m2} vai acontecer')
                    pyautogui.click(m1, m2, duration=2)
                else:
                    if key['onetap']:
                        print('-----> ONE TAP')
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

                        print(f"Fim em {datetime.now().minute}:{datetime.now().second}")

        print(' * - * - * - * - * - * - * - * - * - * - * - * ')
    
    def rand(self, minimo, maximo):
        return random.uniform(minimo, maximo)