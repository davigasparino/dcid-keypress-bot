import customtkinter as ctk

class Templates:
    
    bgSecondary = "#333"
    tpH = 35
    tpMD = 355
    ftH = 50
    padding = 15

    def __init__(self, root):
        self.root = root
        self.root.title("DCID Keypress BOT")
        self.root.geometry("980x500")
        self.root.resizable(False, False) 

        #self.root._set_appearance_mode("light")
        
        self.brandTp = ctk.CTkFrame(
            self.root, 
            width=180,
            height=self.tpH,
            fg_color=self.bgSecondary
        ).place( x=self.padding, y=self.padding )

        self.centerTP = ctk.CTkFrame(
            self.root,
            width=500,
            height=self.tpH,
            fg_color=self.bgSecondary
        ).place(x=self.padding+180+self.padding, y=self.padding)

        self.msg = ctk.CTkFrame(
            self.root,
            width=755,
            height=12,
            fg_color=self.bgSecondary
        ).place(x=self.padding+180+self.padding, y=self.padding+36)

        self.rightTP = ctk.CTkFrame(
            self.root,
            width=240,
            height=self.tpH,
            fg_color=self.bgSecondary
        ).place(x=self.padding+695+self.padding, y=self.padding)

        self.sidebarMD = ctk.CTkFrame(
            self.root,
            width=180,
            height=self.tpMD,
            fg_color=self.bgSecondary
        ).place(x=self.padding, y=self.padding+self.tpH+self.padding)

        self.containerMD = ctk.CTkScrollableFrame(
            self.root,
            width=730,
            height=self.tpMD-20,
            fg_color=self.bgSecondary
        ).place(x=self.padding+180+self.padding, y=self.padding+self.tpH+self.padding)

        self.sidebarFT = ctk.CTkFrame(
            self.root,
            width=180,
            height=self.ftH,
            fg_color=self.bgSecondary
        ).place(x=self.padding, y=self.padding+self.tpH+self.padding+self.tpMD+self.padding)

        self.containerFT = ctk.CTkFrame(
            self.root,
            width=755,
            height=self.ftH,
            fg_color=self.bgSecondary
        ).place(x=self.padding+180+self.padding, y=self.padding+self.tpH+self.padding+self.tpMD+self.padding)

