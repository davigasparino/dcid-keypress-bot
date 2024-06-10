import customtkinter as ctk
from components.View import View as vw 
#from components.Template import Template as tp 
class App:

    def __init__(self, root):
        self.vw = vw(root)
        self.menu()

    def menu(self):
        paddingY = 4
        ctk.CTkButton(
            self.vw.tp.sidebarMD,
            width=self.vw.tp.sidebarWidth,
            text="Principal",
            command=lambda: self.vw.Principal()
        ).pack(pady=paddingY)
        ctk.CTkButton(
            self.vw.tp.sidebarMD,
            width=self.vw.tp.sidebarWidth,
            text="Procedures",
            command=lambda: self.vw.Procedures()
        ).pack(pady=paddingY)
        ctk.CTkButton(
            self.vw.tp.sidebarMD,
            width=self.vw.tp.sidebarWidth,
            text="Settings",
            command=lambda: self.vw.Settings()
        ).pack(pady=paddingY)

    
    
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()