import customtkinter as ctk
from classes.Layout import Layout as ly

class App:
    def __init__(self, root):
        layout = ly(root)
        layout.setTabs([
            ['principal', 'Principal'],
            ['procedures', 'Procedures'],
            ['settings', 'Settings']
        ])

        layout.getTemplate('procedures')
      
        
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
