import customtkinter as ctk

class Layout:
    AllTabs = []

    def __init__(self, root):
        self.primaryColor = "#4e88a4"   
        self.primaryColorHover = "#5f99b5"
        self.primaryBgColor = "#1a1a1a"   
        self.root = root
        self.root.title("DCID - Keypress BOT")
        self.root.geometry("950x750")
        self.root.resizable(width=False, height=False) 
        self.root._set_appearance_mode("dark") # light, dark e system
        self.root.configure(bg=self.primaryBgColor)
        self.Width = 950
        self.Height = 750

        self.mainContainer = ctk.CTkFrame(
            self.root,
            bg_color=self.primaryBgColor,
            fg_color=self.primaryBgColor
        )
        self.mainContainer.pack()

        self.tabView = ctk.CTkTabview(
            self.mainContainer, 
            width=self.Width,
            height=self.Height,
            corner_radius=20,
            border_width=2,
            border_color=self.primaryColor,
            segmented_button_fg_color=self.primaryBgColor,
            segmented_button_selected_color=self.primaryColor,
            segmented_button_selected_hover_color=self.primaryColorHover,
            segmented_button_unselected_color=self.primaryBgColor,
            segmented_button_unselected_hover_color=self.primaryColorHover,
            bg_color=self.primaryBgColor,
            fg_color=self.primaryBgColor
        )
        self.tabView.pack(pady=20, padx=20)
        
    def setTabs(self, args):
        self.AllTabs = args
        for a in args:
            print(a[0])
            self.tabView.add(a[0])
            titulo_guia = ctk.CTkLabel(self.tabView.tab(a[0]), text=a[1])
            titulo_guia.pack()

    def getTemplate(self, template):

        if template == 'procedures':
            sframe = ctk.CTkScrollableFrame(
                self.tabView.tab("procedures"),
                height=self.Height,
                width=self.Width,
                bg_color=self.primaryBgColor,
                fg_color=self.primaryBgColor,
                scrollbar_fg_color=self.primaryBgColor,
                label_fg_color="green",
                border_color="orange"
            )
            sframe.pack()

            list_frame = ctk.CTkFrame(
                sframe,
                bg_color=self.primaryBgColor,
                fg_color=self.primaryBgColor
            )
            

            for item in ["Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3","Item 1", "Item 2", "Item 3"]:
                label = ctk.CTkLabel(list_frame, text=item)
                label.pack(pady=5)

            list_frame.pack(fill=ctk.BOTH, expand=1)

        """ 
        
        self.tabView.add("Principal")
        self.tabView.add("Procedures")
        self.tabView.add("Settings")
        self.tabView.tab("Principal").grid_columnconfigure(0, weight=3)
        self.tabView.tab("Procedures").grid_columnconfigure(0, weight=6)
        self.tabView.tab("Settings").grid_columnconfigure(0, weight=1)

        
        """
        
        