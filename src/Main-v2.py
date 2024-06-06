import customtkinter as ctk
from classes.Templates import Templates as tp

class App:
    def __init__(self, root):
        self.tp = tp(root)
        
        
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
