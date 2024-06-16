import customtkinter as ctk
from components.Layout import Layout as ly 
from components.Procedures.Procedure import Procedure
from components.Robot.Robot import Robot
from pynput import keyboard as pyk
class App:

    def __init__(self, root):
        self.ly = ly(root)
        self.rbt = Robot(self)
        self.menu()

    def menu(self):
        paddingY = 4
        p = Procedure(self)
        ctk.CTkButton(
            self.ly.sidebarMD,
            width=self.ly.sidebarWidth,
            text="Procedures",
            command=lambda: p.List()
        ).pack(pady=paddingY)

    def Abort(self, key):
        if key == pyk.Key.esc:
            self.rbt.StopTheRobot()

    
    
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)

    listener = pyk.Listener(on_release=app.Abort)
    listener.start()

    root.mainloop()