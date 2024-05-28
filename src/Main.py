import tkinter as tk
from classes.DataJson import DataJson as dj
import json
import time

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Layout Personalizado")
        self.root.geometry("800x600")

        self.primaryBGColor = "#0055aa"
        self.secondaryBGColor = "#5555bb"
        self.primaryBGButtom = "#ffffff"

        self.FieldsList = []
        self.UpFieldsList = []
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

            title = tk.Label(row, text=f"{chr(0x1F80A)}   {d['title']}    ", font=("Arial", 12), bg="#ffffff", width=50)
            title.pack(side=tk.LEFT, padx=15)

            unicSymbol = chr(0x1F50D)
            btnView = tk.Button(row, text=f"{unicSymbol}", command=self.CreateViewItemButton(d), bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 14, "bold"))
            btnView.pack(side=tk.RIGHT, pady=5, padx=20)   

    def ViewItem(self, obj): 
        self.updateAllFrames()
        self.Navbar = self.setTitle(obj['title'])

        row = tk.Frame(self.CanvasContainer)
        row.pack(fill="x", pady=5)

        self.btnSave = tk.Button(row, text=f"{chr(0x23F5)} Play", command=lambda: self.UpdateItems(obj['title']), bg="green", fg=self.primaryBGButtom, font=("arial", 12))
        self.btnSave.pack(side=tk.LEFT, pady=5, padx=5)

        self.btnSave = tk.Button(row, text=f"{chr(0x23F9)} Stop", command=lambda: self.UpdateItems(obj['title']), bg="black", fg=self.primaryBGButtom, font=("arial", 12))
        self.btnSave.pack(side=tk.LEFT, pady=5, padx=5)

        row = tk.Frame(self.CanvasContainer)
        row.pack(fill="x", pady=5)

        title = tk.Label(row, text="Title", font=("arial", 15))
        title.pack(side=tk.LEFT, padx=5)
        titleValue = tk.Entry(row, width=20, font=("arial", 15))
        titleValue.insert(0, obj['title'])
        titleValue.pack(side=tk.LEFT, padx=5, pady=5)

        pressDefaultTime = tk.Label(row, text=f"     {chr(0x1F552)}", font=("Arial", 15), width=4)
        pressDefaultTime.pack(side="left", padx=0)
        pressDefaultTime = tk.Label(row, text=f" Timer \n Default ", font=("Arial", 10), width=7)
        pressDefaultTime.pack(side="left", padx=0)
        pressDefaultTimeValue = tk.Entry(row, font=("Arial", 15), width=3)
        pressDefaultTimeValue.insert(0, obj['timer_default'])
        pressDefaultTimeValue.pack(side="left", padx=0)

        self.UpFieldsList.append([
            titleValue,
            pressDefaultTimeValue
        ])

        self.btnNew = tk.Button(row, text=" + ", command=self.NewRow, bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 12, "bold"))
        self.btnNew.pack(side=tk.RIGHT, pady=5, padx=20)

        self.btnSave = tk.Button(self.NavWidget, text=f"{chr(0x274C)} Delete", command=lambda: self.UpdateItems(obj['title']), bg="red", fg=self.primaryBGButtom, font=("arial", 12))
        self.btnSave.pack(side=tk.LEFT, pady=5, padx=2)

        self.btnSave = tk.Button(self.NavWidget, text=f"{chr(0x1F4BE)} Update", command=lambda: self.UpdateItems(obj['title']), bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 12))
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

        self.FieldsList.append([
            titleValue,
            pressDefaultTimeValue
        ])
        
        self.btnNew = tk.Button(row, text=" + ", command=self.NewRow, bg=self.primaryBGColor, fg=self.primaryBGButtom, font=("arial", 12, "bold"))
        self.btnNew.pack(side=tk.RIGHT, pady=5, padx=20)

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
            checkbox_var,
            random1,
            random2
        ])
        self.updateScrollConfigs()

    def saveItems(self):        
        items = []
        for n, field in enumerate(self.FieldsList):
            if n > 0:
                items.append({
                    "key": field[0].get(),
                    "pressed": field[1].get(),
                    "random": field[2].get(),
                    "min": field[3].get(),
                    "max": field[4].get()
                })

        sendJson = {
            "title": self.FieldsList[0][0].get(),
            "timer_default": self.FieldsList[0][1].get(),
            "keys": items
        }

        try:
            saveJson = dj()
            saveJson.insertItem(sendJson)

            self.viewProcedure()
            self.setMessage("New procedure included successfuly!")
        except Exception as e:
            raise e
    
    def UpdateItems(self, obj):
        print('------------ UPDATE ------------')
        print(obj)
        print('------------ ------ ------------')
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
