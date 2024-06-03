import tkinter as tk
from tkinter import messagebox
from classes.DataJson import DataJson as dj
import json
import time
import threading
import sys
import keyboard
from datetime import datetime
import pyautogui
import random

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Layout Personalizado")
        self.root.geometry("800x600")

        self.cc = 0

        self.robotLoop = False
        self.robotObj = []
        self.robotCount = 0
        sys.setrecursionlimit(1500000)

        self.primaryBGColor = "#0055aa"
        self.secondaryBGColor = "#5555bb"
        self.primaryBGButtom = "#ffffff"

        self.FieldsList = []
        self.Sidebar()
        self.Navbar = tk.Frame(self.root, width=600, height=40)
        self.Navbar.pack(side=tk.TOP, fill="both", padx=5, pady=5)
        
        self.NavTitle = tk.Frame(self.Navbar, width=200, height=40)
        self.NavTitle.pack(side=tk.LEFT, fill="both", padx=0, pady=0)
        self.setTitle("Welcome")
        
        self.NavWidget = tk.Frame(self.Navbar, width=200, height=40)
        self.NavWidget.pack(side=tk.RIGHT, fill="both", padx=0, pady=0)

        self.NavMessages = tk.Frame(self.Navbar, width=200, height=40)
        self.NavMessages.pack(side=tk.RIGHT, fill="both", padx=40, pady=0)

        self.Container = tk.Frame(self.root, width=600, height=450)
        self.Container.pack(side=tk.RIGHT, fill="both", expand=True, padx=20, pady=20)

        self.canvas = tk.Canvas(self.Container, width=600, height=440)
        self.canvas.pack(side=tk.LEFT, fill="x", expand=True, padx=0, pady=0)
            
        self.CanvasContainer()

    def Sidebar(self):
        self.sidebar = tk.Frame(self.root, width=200, height=400)
        self.sidebar.pack(side=tk.LEFT, fill="both", padx=5, pady=5)
        self.Menu()

    def CanvasContainer(self):
        self.CanvasContainer = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.CanvasContainer, anchor="nw")

        self.scrollbar = tk.Scrollbar(root, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.bind("<Configure>", self.AjustarLayout)

    def setTitle(self, title = ""):      
        self.clearContent(self.NavTitle)
        m = tk.Label(self.NavTitle, text=title, font=("Arial", 16, "bold"), fg=self.primaryBGColor)
        m.pack(side=tk.LEFT, padx=0)

    def setMessage(self, message = ""):      
        self.clearContent(self.NavMessages)
        m = tk.Label(self.NavMessages, text=message, font=("Arial", 10))
        m.pack(side=tk.LEFT, padx=0)
        
    def clearContent(self, container):
        if container.winfo_children():
            for widget in container.winfo_children():
                widget.destroy() 


    def updateScrollConfigs(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def AjustarLayout(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def HabilitarRolagem(self, event):
        self.canvas.bind_all("<MouseWheel>", self.OnMouseWheel)

    def DesabilitarRolagem(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def OnMouseWheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def CreateViewItemButton(self, d):
        return lambda: self.ViewItem(d)
         
    def Menu(self):
        self.botao_home = tk.Button(self.sidebar, text=f"{chr(0x1F3E0)} Welcome", command=self.viewHome, bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 12))
        self.botao_home.pack(side=tk.TOP, fill='x', padx=10, pady=5)

        self.botao_config = tk.Button(self.sidebar, text=f"{chr(0x1F9F0)} Configs", command=self.viewConfigs, bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 12))
        self.botao_config.pack(side=tk.TOP, fill='x', padx=10, pady=5)

        self.botao_perfis = tk.Button(self.sidebar, text=f"{chr(0x27F2)} Procedures", command=self.viewProcedure, bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 12))
        self.botao_perfis.pack(side=tk.TOP, fill='x', padx=10, pady=5)

    def updateAllFrames(self):
        self.clearContent(self.CanvasContainer)
        self.clearContent(self.NavWidget)
        self.clearContent(self.NavMessages)
        self.updateScrollConfigs()
        
    def viewHome(self):
        self.Navbar = self.setTitle("Welcome")
        self.updateAllFrames()

    def viewConfigs(self):
        self.Navbar = self.setTitle("Configs")
        self.updateAllFrames()

    def viewProcedure(self):
        self.Navbar = self.setTitle("Procedures")
        self.updateAllFrames()
        
        self.botao_home = tk.Button(self.NavWidget, text=" + ", command=self.ViewAddProfile, bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 14, "bold"))
        self.botao_home.pack(side=tk.RIGHT, fill='x', pady=5, padx=20)

        getJson = dj()
        
        for n, d in enumerate(getJson.ReadItems()):
            row = tk.Frame(self.CanvasContainer, bg="#ffffff")
            row.pack(fill="x", pady=5)

            title = tk.Label(row, text=f"{chr(0x1F80A)}   {d['data']['title']}    ", font=("Arial", 12), bg="#ffffff", width=50)
            title.pack(side=tk.LEFT, padx=15)

            unicSymbol = chr(0x1F50D)
            btnView = tk.Button(row, text=f"{unicSymbol}", command=self.CreateViewItemButton(d), bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 14, "bold"))
            btnView.pack(side=tk.RIGHT, pady=5, padx=20)   

    def ViewItem(self, obj): 
        self.robotLoop = False
        self.robotObj = obj
        self.updateAllFrames()
        self.Navbar = self.setTitle(obj['data']['title'])

        row = tk.Frame(self.CanvasContainer)
        row.pack(fill="x", pady=5)

        self.btnSave = tk.Button(row, text=f"{chr(0x23F5)} Play", 
        command=lambda: threading.Thread(
            target=self.Robot
        ).start(), bg="green", fg=self.primaryBGButtom, font=("arial", 12))
        self.btnSave.pack(side=tk.LEFT, pady=5, padx=5)

        self.btnSave = tk.Button(row, text=f"{chr(0x23F9)} Stop", 
        command=self.StopTheRobot, bg="black", fg=self.primaryBGButtom, font=("arial", 12))
        self.btnSave.pack(side=tk.LEFT, pady=5, padx=5)

        self.LiveTime = tk.Label(row, font=("Helvetica", 24))
        self.LiveTime.pack()

        row = tk.Frame(self.CanvasContainer)
        row.pack(fill="x", pady=5)

        title = tk.Label(row, text="Title", font=("arial", 15))
        title.pack(side=tk.LEFT, padx=5)
        titleValue = tk.Entry(row, width=15, font=("arial", 15))
        titleValue.insert(0, obj['data']['title'])
        titleValue.pack(side=tk.LEFT, padx=5, pady=5)

        pressDefaultTime = tk.Label(row, text=f"     {chr(0x1F552)}", font=("Arial", 15), width=4)
        pressDefaultTime.pack(side="left", padx=0)
        pressDefaultTime = tk.Label(row, text=f" Timer \n Default ", font=("Arial", 10), width=7)
        pressDefaultTime.pack(side="left", padx=0)
        pressDefaultTimeValue = tk.Entry(row, font=("Arial", 15), width=3)
        pressDefaultTimeValue.insert(0, obj['data']['timer_default'])
        pressDefaultTimeValue.pack(side="left", padx=0)

        self.btnNew = tk.Button(row, text=" + ", command=self.NewRow, bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 12, "bold"))
        self.btnNew.pack(side=tk.RIGHT, pady=5, padx=20)

        row = tk.Frame(self.CanvasContainer)
        row.pack(fill="x", pady=5)
        obs = tk.Label(row, text="Obs", font=("arial", 12))
        obs.pack(side=tk.LEFT, padx=5)
        obsValue = tk.Entry(row, width=30, font=("arial", 12))
        if obj['data']['notes']:
            obsValue.insert(0, obj['data']['notes'])
        obsValue.pack(side=tk.LEFT, padx=5, pady=5)

        self.FieldsList.append([
            titleValue,
            pressDefaultTimeValue,
            obsValue
        ])

        self.checkboxValues = [tk.BooleanVar() for _ in range(len(obj['data']['keys']))]
        self.oneTapValues = [tk.BooleanVar() for _ in range(len(obj['data']['keys']))]
        
        for n, k in enumerate(obj['data']['keys']):
            row = tk.Frame(self.CanvasContainer)
            row.pack(fill="x", pady=20)

            key = tk.Label(row, text=f"{chr(0x1F80A)} Key", font=("Arial", 12))
            key.pack(side="left", padx=5)
            
            keyValue = tk.Entry(row, font=("Arial", 12), width=10)
            keyValue.insert(0, k['key'])
            keyValue.pack(side="left", padx=5)

            pressTime = tk.Label(row, text=f"     {chr(0x1F552)}", font=("Arial", 12), width=4)
            pressTime.pack(side="left", padx=0)

            pressTimeValue = tk.Entry(row, font=("Arial", 12), width=3)
            pressTimeValue.insert(0, k['pressed'])
            pressTimeValue.pack(side="left", padx=0)

            self.oneTapValues[n] = tk.BooleanVar()
            if(k['onetap']):
                self.oneTapValues[n].set(True)
            else:
                self.oneTapValues[n].set(False)
                
            oneTapcheckbox = tk.Checkbutton(row, text=f"One Tap ", variable=self.oneTapValues[n])
            oneTapcheckbox.pack(side="left", padx=5)      

            self.checkboxValues[n] = tk.BooleanVar()
            if(k['random']):
                self.checkboxValues[n].set(True)
            else:
                self.checkboxValues[n].set(False)

            separator = tk.Label(row, text=f"    {chr(0x27F2)}", font=("Arial", 12), width=4)
            separator.pack(side="left", padx=0)
            
            checkbox = tk.Checkbutton(row, text=f"Random ", variable=self.checkboxValues[n])
            checkbox.pack(side="left", padx=5)            
                  
            
            random1 = tk.Entry(row, font=("Arial", 12), width=3)
            random1.insert(0, k['min'])
            random1.pack(side="left", padx=0)
            randomLabel = tk.Label(row, text=f" x ", font=("Arial", 12), width=2)
            randomLabel.pack(side="left", padx=0)
            random2 = tk.Entry(row, font=("Arial", 12), width=3)
            random2.insert(0, k['max'])
            random2.pack(side="left", padx=0)

            self.FieldsList.append([
                keyValue,
                pressTimeValue,
                self.oneTapValues[n],
                self.checkboxValues[n],
                random1,
                random2
            ])

        self.btnSave = tk.Button(self.NavWidget, text=f"{chr(0x274C)} Delete", command=lambda: self.deleteItems(obj['id']), bg="red", fg=self.primaryBGButtom, font=("arial", 12))
        self.btnSave.pack(side=tk.LEFT, pady=5, padx=2)

        self.btnSave = tk.Button(self.NavWidget, text=f"{chr(0x1F4BE)} Update", command=lambda: self.UpdateItems(obj['id']), bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 12))
        self.btnSave.pack(side=tk.LEFT, pady=5, padx=20)

        #chr(0x26A0)

    def ViewAddProfile(self):
        self.Navbar = self.setTitle("Add Procedure")
        self.clearContent(self.NavWidget)
        self.clearContent(self.CanvasContainer)

        row = tk.Frame(self.CanvasContainer)
        row.pack(fill="x", pady=5)

        title = tk.Label(row, text="Title", font=("arial", 15))
        title.pack(side=tk.LEFT, padx=5)
        titleValue = tk.Entry(row, width=20, font=("arial", 15))
        titleValue.pack(side=tk.LEFT, padx=5, pady=5)

        pressDefaultTime = tk.Label(row, text=f"     {chr(0x1F552)}", font=("Arial", 15), width=4)
        pressDefaultTime.pack(side="left", padx=0)
        pressDefaultTime = tk.Label(row, text=f" Timer \n Default ", font=("Arial", 10), width=7)
        pressDefaultTime.pack(side="left", padx=0)
        pressDefaultTimeValue = tk.Entry(row, font=("Arial", 15), width=3)
        pressDefaultTimeValue.pack(side="left", padx=0)

        self.btnNew = tk.Button(row, text=" + ", command=self.NewRow, bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 12, "bold"))
        self.btnNew.pack(side=tk.RIGHT, pady=5, padx=20)

        row = tk.Frame(self.CanvasContainer)
        row.pack(fill="x", pady=5)
        obs = tk.Label(row, text="Obs", font=("arial", 12))
        obs.pack(side=tk.LEFT, padx=5)
        obsValue = tk.Entry(row, width=30, font=("arial", 12))
        obsValue.pack(side=tk.LEFT, padx=5, pady=5)

        self.FieldsList.append([
            titleValue,
            pressDefaultTimeValue,
            obsValue
        ])        

        self.btnSave = tk.Button(self.NavWidget, text=f"{chr(0x1F4BE)} Save", command=self.saveItems, bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 12))
        self.btnSave.pack(side=tk.RIGHT, pady=5, padx=20)

        self.updateScrollConfigs()

    def NewRow(self):
        row = tk.Frame(self.CanvasContainer)
        row.pack(fill="x", pady=20)

        key = tk.Label(row, text=f"{chr(0x1F80A)} Key", font=("Arial", 12))
        key.pack(side="left", padx=5)
        
        keyValue = tk.Entry(row, font=("Arial", 12), width=10)
        keyValue.pack(side="left", padx=5)

        pressTime = tk.Label(row, text=f"     {chr(0x1F552)}", font=("Arial", 12), width=4)
        pressTime.pack(side="left", padx=0)

        pressTimeValue = tk.Entry(row, font=("Arial", 12), width=3)
        pressTimeValue.pack(side="left", padx=0)

        onetap_var = tk.BooleanVar()
        onetap = tk.Checkbutton(row, text="one tap", variable=onetap_var)
        onetap.pack(side="left", padx=5)

        separator = tk.Label(row, text=f"    {chr(0x27F2)}", font=("Arial", 12), width=4)
        separator.pack(side="left", padx=0)

        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(row, text="Random", variable=checkbox_var)
        checkbox.pack(side="left", padx=5)

        random1 = tk.Entry(row, font=("Arial", 12), width=3)
        random1.pack(side="left", padx=0)
        randomLabel = tk.Label(row, text=f" x ", font=("Arial", 12), width=2)
        randomLabel.pack(side="left", padx=0)
        random2 = tk.Entry(row, font=("Arial", 12), width=3)
        random2.pack(side="left", padx=0)

        self.FieldsList.append([
            keyValue,
            pressTimeValue,
            onetap_var,
            checkbox_var,
            random1,
            random2
        ])
        self.updateScrollConfigs()

    def saveItems(self): 
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
                "notes": self.FieldsList[0][2].get(),
                "keys": items
            }
        
            saveJson = dj()
            saveJson.insertItem(sendJson)

            self.FieldsList = []
            self.viewProcedure()
            self.setMessage("New procedure included successfuly!")
        except Exception as e:
            raise e
    
    def UpdateItems(self, primaryKey):  
        try:      
            items = []
            for n, field in enumerate(self.FieldsList):
                print(field)
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
                "notes": self.FieldsList[0][2].get(),
                "keys": items
            }           
            
            saveJson = dj()
            saveJson.updateItem(primaryKey, sendJson)
        
            self.FieldsList = []
            self.viewProcedure()
            self.setMessage("Procedure Update successfuly!")
        except Exception as e:
            raise e
    
    def deleteItems(self, id):

        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal

        user_confirmation = messagebox.askyesno("Confirmação", "Você tem certeza de que deseja deletar este item?")
        if user_confirmation:

            saveJson = dj()
            try:      
                saveJson.deleteItem(id)
                self.FieldsList = []
                self.viewProcedure()
                self.setMessage("Procedure deleted successfuly!")
            except Exception as e:
                raise e
        

        
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

        
        # if self.cc == 0:
        #     print('-> vai iniciar em 10 segundos')
        #     time.sleep(10)

        for k in self.robotObj['data']['keys']:
            # self.cc = self.cc + 1
            #pyautogui.click(50, 100)

            timer_default = 10

            if self.robotObj['data']['timer_default']:
                timer_default = self.robotObj['data']['timer_default']

            if k['pressed']:
                timer_default = k['pressed']

            if k['random'] and k['min'] and k['max']:
                timer_default = self.rand(int(k['min']), int(k['max']))
                print(f"the key is {k['key']} an the random number is {int(timer_default)}")
           
            print(f"inicio em {datetime.now().minute}:{datetime.now().second}")
            
            if not k['key']:
                continue

            print(k['key'])
            if k['key'] == 'click':
                print('-----> CLICK')
                rt1 = tk.Tk()
                width = rt1.winfo_screenwidth()
                height = rt1.winfo_screenheight()
                print(f"Largura da tela: {width} pixels")
                print(f"Altura da tela: {height} pixels")

                if k['random']:
                    m1 = int(self.rand(0,width - 1))
                    m2 = int(self.rand(50,height -50))
                else:
                    m1 = 50
                    m2 = 50
                print(f'em 2 segundos o click random {m1} e {m2} vai acontecer')
                pyautogui.click(m1, m2, duration=2)
            else:
                if k['onetap']:
                    print('-----> ONE TAP')
                    time.sleep(2)
                    keyboard.press(k['key'])
                    time.sleep(interval)
                    keyboard.release(k['key'])
                    time.sleep(int(timer_default))
                
                else:
                    startTime = time.time()
                    while time.time() - startTime < int(timer_default):
                        if not self.robotLoop:
                            break

                        keyboard.press(k['key'])
                        time.sleep(interval)
                        keyboard.release(k['key'])

                    print(f"Fim em {datetime.now().minute}:{datetime.now().second}")

            
            #print(f"pressionando a tecla {k['key']} po {timer_default} segundos")

        print(' * - * - * - * - * - * - * - * - * - * - * - * ')
    
    def rand(self, minimo, maximo):
        return random.uniform(minimo, maximo)
            


        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
