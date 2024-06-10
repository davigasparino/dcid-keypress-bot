import customtkinter as ctk
from components.Layout import Layout as ly 
from components.Procedures.Procedure import Procedure
class App:

    def __init__(self, root):
        self.ly = ly(root)
        self.menu()

    def menu(self):
        paddingY = 4
        p = Procedure(self.ly)
        ctk.CTkButton(
            self.ly.sidebarMD,
            width=self.ly.sidebarWidth,
            text="Procedures",
            command=lambda: p.List()
        ).pack(pady=paddingY)

    
    
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()