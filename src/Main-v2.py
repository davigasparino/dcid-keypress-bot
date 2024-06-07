import customtkinter as ctk
from classes.Templates import Templates as tp
from classes.DataJson import DataJson as dj
from tkinter import messagebox
import threading
import sys
import time
import random
import keyboard
import pyautogui
from datetime import datetime

class App:
    primaryBGColor = "#0055aa"
    FieldsList = []

    def __init__(self, root):
        self.tp = tp(root)
        self.menu()
        self.robotLoop = False
        self.robotObj = []
        self.robotCount = 0
        sys.setrecursionlimit(1500000)
        #self.tp.Message("Mensagem que va iaparecer na tela")
    
    def menu(self):
        paddingY = 4
        ctk.CTkButton(
            self.tp.sidebarMD,
            width=self.tp.sidebarWidth,
            text="Principal",
            command=lambda: self.Principal()
        ).pack(pady=paddingY)
        ctk.CTkButton(
            self.tp.sidebarMD,
            width=self.tp.sidebarWidth,
            text="Procedures",
            command=lambda: self.Procedures()
        ).pack(pady=paddingY)
        ctk.CTkButton(
            self.tp.sidebarMD,
            width=self.tp.sidebarWidth,
            text="Settings",
            command=lambda: self.Settings()
        ).pack(pady=paddingY)

    def Principal(self):
        self.tp.clearContainers()
        self.tp.setTitle("Principal")

    def Procedures(self):
        self.tp.clearContainers()
        self.tp.setTitle("Procedures")

        btn = ctk.CTkButton(
            self.tp.rightMD, 
            text=" + Add New Procedure", 
            font=("arial", 14), 
            width=self.tp.rightWidth,
            command=self.ViewItem
        )
        btn.pack(side="right")

        getJson = dj()
        
        for n, d in enumerate(getJson.ReadItems()):
            row = ctk.CTkFrame(self.tp.containerMD)
            row.pack(fill="x", pady=5)

            title = ctk.CTkLabel(row, text=f"{chr(0x235F)}   {d['data']['title']} ", font=("Arial", 14))
            title.pack(side=ctk.LEFT, padx=12)

            unicSymbol = chr(0x1F80A)
            btnView = ctk.CTkButton(
                row, 
                text=f"{unicSymbol}", 
                font=("arial", 14, "bold"), 
                width=20,
                command=self.CreateViewItemButton(d)
            )
            btnView.pack(side=ctk.RIGHT) 

    def CreateViewItemButton(self, d):
        return lambda: self.ViewItem(d)

    def ViewItem(self, obj = []): 
        self.robotLoop = False
        self.robotObj = obj
        
        self.tp.clearContainers()

        if obj:
            ID = obj['id']
            self.tp.setTitle(obj['data']['title'])
        else:
            ID = 0
            self.tp.setTitle("Add New Procedure")
            
        row = ctk.CTkFrame(self.tp.containerMD)
        row.pack(fill="x", pady=5)

        title = ctk.CTkLabel(row, text="Title", font=("arial", 12))
        title.pack(side=ctk.LEFT, padx=5)
        titleValue = ctk.CTkEntry(row, width=200, font=("arial", 12))
        
        if obj:
            titleValue.insert(0, obj['data']['title'])

        titleValue.pack(side=ctk.LEFT, padx=5, pady=5)

        pressDefaultTimeValue = ctk.CTkEntry(row, font=("Arial", 12), width=30)
        
        if obj:
            pressDefaultTimeValue.insert(0, obj['data']['timer_default'])
        
        pressDefaultTimeValue.pack(side=ctk.RIGHT, padx=5, pady=5)
        pressDefaultTime = ctk.CTkLabel(row, text=f" Timer Default ", font=("Arial", 12))
        pressDefaultTime.pack(side=ctk.RIGHT, padx=0)
        pressDefaultTime = ctk.CTkLabel(row, text=f"{chr(0x1F552)}", font=("Arial", 15), width=10)
        pressDefaultTime.pack(side=ctk.RIGHT, padx=0)        

        row = ctk.CTkFrame(self.tp.containerMD)
        row.pack(fill="x", pady=5)
        obs = ctk.CTkLabel(row, text="Obs", font=("arial", 12))
        obs.pack(side=ctk.LEFT, padx=0)
        obsValue = ctk.CTkTextbox(row, width=self.tp.centerWidth, height=60)
        
        if obj:
            obsValue.insert("0.0", obj['data']['notes'])
        
        obsValue.pack(side=ctk.LEFT, padx=5, pady=5)

        self.FieldsList.append([
            titleValue,
            pressDefaultTimeValue,
            obsValue
        ])

        if obj:
            self.checkboxValues = [ctk.BooleanVar() for _ in range(len(obj['data']['keys']))]
            self.oneTapValues = [ctk.BooleanVar() for _ in range(len(obj['data']['keys']))]
        
            for n, k in enumerate(obj['data']['keys']):
                row = ctk.CTkFrame(self.tp.containerMD)
                row.pack(fill="x", pady=20)

                key = ctk.CTkLabel(row, text=f"Key", font=("Arial", 12))
                key.pack(side=ctk.LEFT, padx=5)
                
                keyValue = ctk.CTkEntry(row, font=("Arial", 12), width=60)
                keyValue.insert(0, k['key'])
                keyValue.pack(side=ctk.LEFT, padx=5)

                pressTime = ctk.CTkLabel(
                    row, text=f"{chr(0x1F552)}", 
                    font=("Arial", 12)
                )
                pressTime.pack(side=ctk.LEFT, padx=0)
                pressTimeValue = ctk.CTkEntry(row, font=("Arial", 12), width=30)
                pressTimeValue.insert(0, k['pressed'])
                pressTimeValue.pack(side=ctk.LEFT, padx=5)

                self.oneTapValues[n] = ctk.BooleanVar()
                if(k['onetap']):
                    self.oneTapValues[n].set(True)
                else:
                    self.oneTapValues[n].set(False)
                    
                oneTapcheckbox = ctk.CTkSwitch(
                    row, 
                    text=f"One Tap ", 
                    variable=self.oneTapValues[n]
                )
                oneTapcheckbox.pack(side=ctk.LEFT, padx=5)      

                random2 = ctk.CTkEntry(row, font=("Arial", 12), width=30)
                random2.insert(0, k['max'])
                random2.pack(side=ctk.RIGHT, padx=0)
                randomLabel = ctk.CTkLabel(row, text=f" x ", font=("Arial", 12), width=2)
                randomLabel.pack(side=ctk.RIGHT, padx=0)
                random1 = ctk.CTkEntry(row, font=("Arial", 12), width=30)
                random1.insert(0, k['min'])
                random1.pack(side=ctk.RIGHT, padx=0)

                self.checkboxValues[n] = ctk.BooleanVar()
                if(k['random']):
                    self.checkboxValues[n].set(True)
                else:
                    self.checkboxValues[n].set(False)
                
                checkbox = ctk.CTkSwitch(row, text=f"Random", variable=self.checkboxValues[n])
                checkbox.pack(side=ctk.RIGHT, padx=5) 

                self.FieldsList.append([
                    keyValue,
                    pressTimeValue,
                    self.oneTapValues[n],
                    self.checkboxValues[n],
                    random1,
                    random2
                ])

        self.btnSave = ctk.CTkButton(
            self.tp.rightFT, 
            text=f"{chr(0x1F4BE)} Save", 
            font=("arial", 12, "bold"),
            width=self.tp.rightWidth/2-4,
            command=lambda: self.saveItems(ID)
        )
        self.btnSave.pack(side=ctk.RIGHT, pady=0, padx=3)

        if obj:
            self.btnSave = ctk.CTkButton(
                self.tp.rightFT, 
                text=f"{chr(0x274C)} Del",
                font=("arial", 12, "bold"),
                width=(self.tp.rightWidth/2)-8,
                command=lambda: self.deleteItems(obj['id']),
                fg_color="#aa0000"
            )
            self.btnSave.pack(side=ctk.RIGHT, pady=0, padx=4)

            self.btnSave = ctk.CTkButton(
                self.tp.rightMD, 
                text=f"{chr(0x23F9)} Stop",
                width=(self.tp.rightWidth/2)-8,
                command=self.StopTheRobot
            )
            self.btnSave.pack(side=ctk.RIGHT, pady=0, padx=4)
            
            self.btnSave = ctk.CTkButton(
                self.tp.rightMD, 
                text=f"{chr(0x23F5)} Play",
                width=(self.tp.rightWidth/2)-8,
                command=lambda: threading.Thread(
                    target=self.Robot
                ).start(),
            )
            self.btnSave.pack(side=ctk.RIGHT, pady=0, padx=4)

        self.btnNew = ctk.CTkButton(
            self.tp.containerFT, 
            text="+ Add new row", 
            command=self.NewRow,
            font=("arial", 12, "bold")
        )
        self.btnNew.pack(side=ctk.RIGHT, pady=0, padx=0)

        

        #chr(0x26A0)
    
    def NewRow(self):
        row = ctk.CTkFrame(self.tp.containerMD)
        row.pack(fill="x", pady=20)

        key = ctk.CTkLabel(row, text=f"Key", font=("Arial", 12))
        key.pack(side=ctk.LEFT, padx=5)
        
        keyValue = ctk.CTkEntry(row, font=("Arial", 12), width=60)
        keyValue.pack(side=ctk.LEFT, padx=5)

        pressTime = ctk.CTkLabel(
            row, text=f"{chr(0x1F552)}", 
            font=("Arial", 12)
        )
        pressTime.pack(side=ctk.LEFT, padx=0)
        pressTimeValue = ctk.CTkEntry(row, font=("Arial", 12), width=30)
        pressTimeValue.pack(side=ctk.LEFT, padx=5)

        onetap_var = ctk.BooleanVar()   
        oneTapcheckbox = ctk.CTkSwitch(
            row, 
            text=f"One Tap ", 
            variable=onetap_var
        )
        oneTapcheckbox.pack(side=ctk.LEFT, padx=5)      

        random2 = ctk.CTkEntry(row, font=("Arial", 12), width=30)
        random2.pack(side=ctk.RIGHT, padx=0)
        randomLabel = ctk.CTkLabel(row, text=f" x ", font=("Arial", 12), width=2)
        randomLabel.pack(side=ctk.RIGHT, padx=0)
        random1 = ctk.CTkEntry(row, font=("Arial", 12), width=30)
        random1.pack(side=ctk.RIGHT, padx=0)
        
        checkbox_var = ctk.BooleanVar()  
        checkbox = ctk.CTkSwitch(
            row, 
            text=f"Random", 
            variable=checkbox_var
        )
        checkbox.pack(side=ctk.RIGHT, padx=5) 

        self.FieldsList.append([
            keyValue,
            pressTimeValue,
            onetap_var,
            checkbox_var,
            random1,
            random2
        ])

    def saveItems(self, id = 0): 
        try:      
            items = []
            for n, field in enumerate(self.FieldsList):
                if n > 0 and all(field):
                    items.append({
                        "key": field[0].get(),
                        "pressed": field[1].get(),
                        "onetap": field[2].get(),
                        "random": field[3].get(),
                        "min": field[4].get(),
                        "max": field[5].get()
                    })

            sendJson = {
                "title": self.FieldsList[0][0].get(),
                "timer_default": self.FieldsList[0][1].get(),
                "notes": self.FieldsList[0][2].get("1.0", "end"),
                "keys": items
            }
        
            saveJson = dj()
            saveJson.Save(sendJson, int(id))

            self.FieldsList = []
            self.Procedures()
            self.tp.Message("New procedure included successfuly!")
        except Exception as e:
            raise e
    
    def deleteItems(self, id):
        root = ctk.CTk()
        root.withdraw()  # Esconde a janela principal
        user_confirmation = messagebox.askyesno("Confirmação", "Você tem certeza de que deseja deletar este item?")
        if user_confirmation:

            saveJson = dj()
            try:      
                saveJson.deleteItem(id)
                self.FieldsList = []
                self.Procedures()
                self.tp.Message("New procedure included successfuly!")
            except Exception as e:
                raise e

    def Settings(self):
        self.tp.clearContainers()
        self.tp.setTitle("Settings") 

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
        
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
