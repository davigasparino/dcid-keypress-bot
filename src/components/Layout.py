import customtkinter as ctk
import time
import threading

class Layout:
    
    bgSecondary = "transparent"
    tpH = 35
    tpMD = 355
    ftH = 50
    padding = 20
    sidebarWidth = 200
    centerWidth = 520
    rightWidth = 200

    def __init__(self, root):
        self.root = root
        self.root.title("DCID Keypress BOT")
        self.root.geometry("1000x520")
        self.root.resizable(False, False) 

        mode = ctk.get_appearance_mode()

        if mode == 'Light':
            self.bgSecondary = "#e7e7e7"
        
        self.brandTp = ctk.CTkFrame(
            self.root, 
            width=self.sidebarWidth,
            height=self.tpH,
            fg_color=self.bgSecondary
        )
        self.brandTp.place( 
            x=self.padding, 
            y=self.padding 
        )

        self.centerTP = ctk.CTkFrame(
            self.root,
            width=self.centerWidth,
            height=self.tpH,
            fg_color=self.bgSecondary
        )
        self.centerTP.place(
            x=self.padding+self.sidebarWidth+self.padding, 
            y=self.padding
        )

        self.msg = ctk.CTkFrame(
            self.root,
            width=self.centerWidth,
            height=12,
            fg_color="transparent"
        )
        self.msg.place(
            x=self.padding+self.sidebarWidth+self.padding, 
            y=self.padding+32
        )

        self.rightTP = ctk.CTkFrame(
            self.root,
            width=self.rightWidth,
            height=self.tpH,
            fg_color=self.bgSecondary
        )
        self.rightTP.place(
            x=self.padding+self.sidebarWidth+self.padding+self.centerWidth+self.padding,  
            y=self.padding
        )

        self.sidebarMD = ctk.CTkFrame(
            self.root,
            width=self.sidebarWidth,
            height=self.tpMD,
            fg_color=self.bgSecondary
        )
        self.sidebarMD.place(
            x=self.padding, 
            y=self.padding+self.tpH+self.padding
        )

        self.rightMD = ctk.CTkFrame(
            self.root,
            width=self.rightWidth,
            height=self.tpMD,
            fg_color=self.bgSecondary
        )
        self.rightMD.place(
            x=self.padding+self.sidebarWidth+self.padding+self.centerWidth+self.padding, 
            y=self.padding+self.tpH+self.padding
        )

        self.containerMD = ctk.CTkScrollableFrame(
            self.root,
            width=self.centerWidth-23,
            height=self.tpMD-12,
            fg_color=self.bgSecondary
        )
        self.containerMD.place(
            x=self.padding+self.sidebarWidth+self.padding, 
            y=self.padding+self.tpH+self.padding
        )

        self.sidebarFT = ctk.CTkFrame(
            self.root,
            width=self.sidebarWidth,
            height=self.ftH,
            fg_color=self.bgSecondary
        )
        self.sidebarFT.place(
            x=self.padding, 
            y=self.padding+self.tpH+self.padding+self.tpMD+self.padding
        )

        self.containerFT = ctk.CTkFrame(
            self.root,
            width=self.centerWidth,
            height=self.ftH,
            fg_color=self.bgSecondary
        )
        self.containerFT.place(
            x=self.padding+self.sidebarWidth+self.padding, 
            y=self.padding+self.tpH+self.padding+self.tpMD+self.padding
        )

        self.rightFT = ctk.CTkFrame(
            self.root,
            width=self.rightWidth,
            height=self.ftH,
            fg_color=self.bgSecondary
        )
        self.rightFT.place(
            x=self.padding+self.sidebarWidth+self.padding+self.centerWidth+self.padding,   
            y=self.padding+self.tpH+self.padding+self.tpMD+self.padding
        )

    def setTitle(self, title):
        self.clearFrame(self.centerTP)
        theTitle = ctk.CTkLabel(self.centerTP, text=title, font=("Arial", 22), width=self.centerWidth)
        theTitle.pack(padx=0)

    def Message(self, text):
        ctk.CTkLabel(self.msg, text=text, font=("Arial", 12, "bold")).pack(pady=0, padx=0)
        threading.Thread(
            target=lambda: self.clearFrame(self.msg, 10)
        ).start()

    def clearAllFrames(self):
        self.clearFrame(self.centerTP)
        self.clearFrame(self.rightTP)
        self.clearFrame(self.rightMD)
        self.clearFrame(self.rightFT)
        self.clearFrame(self.containerFT)
        self.clearFrame(self.containerMD)
    
    def clearContainers(self):
        self.clearFrame(self.rightMD)
        self.clearFrame(self.rightFT)
        self.clearFrame(self.containerFT)
        self.clearFrame(self.containerMD)

    def clearFrame(self, frame, t = 0):
        if t > 0:
            time.sleep(t)

        for widget in frame.winfo_children():
            widget.destroy()
    
    def Renderer(self, obj):
        self.clearContainers()

        if obj['title']:
            self.setTitle(obj['title'])

        if obj['rightMD']:
            self.setRightMD(obj['rightMD'])
    
    def setRightMD(self, obj):
        if obj['type'] == 'button':
            btn = ctk.CTkButton(
                self.rightMD, 
                text=obj['text'], 
                font=("arial", 14), 
                width=self.rightWidth
            )
            btn.pack()

