import customtkinter as ctk

class Templates:
    
    bgSecondary = "transparent"
    tpH = 35
    tpMD = 355
    ftH = 50
    padding = 20
    sidebarWidht = 200
    centerWidht = 520
    rightWidht = 200

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
            width=self.sidebarWidht,
            height=self.tpH,
            fg_color=self.bgSecondary
        )
        self.brandTp.place( 
            x=self.padding, 
            y=self.padding 
        )

        self.centerTP = ctk.CTkFrame(
            self.root,
            width=self.centerWidht,
            height=self.tpH,
            fg_color=self.bgSecondary
        )
        self.centerTP.place(
            x=self.padding+self.sidebarWidht+self.padding, 
            y=self.padding
        )

        self.msg = ctk.CTkFrame(
            self.root,
            width=self.centerWidht,
            height=12,
            fg_color="transparent"
        )
        self.msg.place(
            x=self.padding+self.sidebarWidht+self.padding, 
            y=self.padding+32
        )

        self.rightTP = ctk.CTkFrame(
            self.root,
            width=self.rightWidht,
            height=self.tpH,
            fg_color=self.bgSecondary
        )
        self.rightTP.place(
            x=self.padding+self.sidebarWidht+self.padding+self.centerWidht+self.padding,  
            y=self.padding
        )

        self.sidebarMD = ctk.CTkFrame(
            self.root,
            width=self.sidebarWidht,
            height=self.tpMD,
            fg_color=self.bgSecondary
        )
        self.sidebarMD.place(
            x=self.padding, 
            y=self.padding+self.tpH+self.padding
        )

        self.rightMD = ctk.CTkFrame(
            self.root,
            width=self.rightWidht,
            height=self.tpMD,
            fg_color=self.bgSecondary
        )
        self.rightMD.place(
            x=self.padding+self.sidebarWidht+self.padding+self.centerWidht+self.padding, 
            y=self.padding+self.tpH+self.padding
        )

        self.containerMD = ctk.CTkScrollableFrame(
            self.root,
            width=self.centerWidht-23,
            height=self.tpMD-12,
            fg_color=self.bgSecondary
        )
        self.containerMD.place(
            x=self.padding+self.sidebarWidht+self.padding, 
            y=self.padding+self.tpH+self.padding
        )

        self.sidebarFT = ctk.CTkFrame(
            self.root,
            width=self.sidebarWidht,
            height=self.ftH,
            fg_color=self.bgSecondary
        )
        self.sidebarFT.place(
            x=self.padding, 
            y=self.padding+self.tpH+self.padding+self.tpMD+self.padding
        )

        self.containerFT = ctk.CTkFrame(
            self.root,
            width=self.centerWidht,
            height=self.ftH,
            fg_color=self.bgSecondary
        )
        self.containerFT.place(
            x=self.padding+self.sidebarWidht+self.padding, 
            y=self.padding+self.tpH+self.padding+self.tpMD+self.padding
        )

        self.rightFT = ctk.CTkFrame(
            self.root,
            width=self.rightWidht,
            height=self.ftH,
            fg_color=self.bgSecondary
        )
        self.rightFT.place(
            x=self.padding+self.sidebarWidht+self.padding+self.centerWidht+self.padding,   
            y=self.padding+self.tpH+self.padding+self.tpMD+self.padding
        )

    def setTitle(self, title):
        self.clearFrame(self.centerTP)
        theTitle = ctk.CTkLabel(self.centerTP, text=title, font=("Arial", 22), width=self.centerWidht)
        theTitle.pack(padx=0)

    def Message(self, text):
        ctk.CTkLabel(self.msg, text=text, font=("Arial", 12, "bold")).pack(pady=0, padx=0)

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

    def clearFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()