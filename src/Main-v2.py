import customtkinter as ctk
from classes.Templates import Templates as tp

class App:
    def __init__(self, root):
        self.tp = tp(root)
        self.menu()
        #self.tp.Message("Mensagem que va iaparecer na tela")
    
    def menu(self):
        paddingY = 4
        ctk.CTkButton(
            self.tp.sidebarMD,
            width=self.tp.sidebarWidht,
            text="Principal"
        ).pack(pady=paddingY)
        ctk.CTkButton(
            self.tp.sidebarMD,
            width=self.tp.sidebarWidht,
            text="Procedures"
        ).pack(pady=paddingY)
        ctk.CTkButton(
            self.tp.sidebarMD,
            width=self.tp.sidebarWidht,
            text="Settings"
        ).pack(pady=paddingY)

        
        
        
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
