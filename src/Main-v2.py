import customtkinter as ctk
from classes.Templates import Templates as tp
from classes.DataJson import DataJson as dj

class App:
    primaryBGColor = "#0055aa"

    def __init__(self, root):
        self.tp = tp(root)
        self.menu()
        #self.tp.Message("Mensagem que va iaparecer na tela")
    
    def menu(self):
        paddingY = 4
        ctk.CTkButton(
            self.tp.sidebarMD,
            width=self.tp.sidebarWidht,
            text="Principal",
            command=lambda: self.Principal()
        ).pack(pady=paddingY)
        ctk.CTkButton(
            self.tp.sidebarMD,
            width=self.tp.sidebarWidht,
            text="Procedures",
            command=lambda: self.Procedures()
        ).pack(pady=paddingY)
        ctk.CTkButton(
            self.tp.sidebarMD,
            width=self.tp.sidebarWidht,
            text="Settings",
            command=lambda: self.Settings()
        ).pack(pady=paddingY)

    def Principal(self):
        self.tp.clearContainers()
        self.tp.setTitle("Principal")

    def Procedures(self):
        self.tp.clearContainers()
        self.tp.setTitle("Procedures")

        btn = ctk.CTkButton(self.tp.rightMD, text=" + Add New Procedure", font=("arial", 14), width=self.tp.rightWidht)
        btn.pack(side="right")

        getJson = dj()
        
        for n, d in enumerate(getJson.ReadItems()):
            row = ctk.CTkFrame(self.tp.containerMD)
            row.pack(fill="x", pady=5)

            title = ctk.CTkLabel(row, text=f"{chr(0x235F)}   {d['data']['title']} ", font=("Arial", 14))
            title.pack(side=ctk.LEFT, padx=15)

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

    def ViewItem(self, obj): 
        self.tp.clearContainers()
        print(obj)

    def Settings(self):
        self.tp.clearContainers()
        self.tp.setTitle("Settings")        
        
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
