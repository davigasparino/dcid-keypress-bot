import customtkinter as ctk

window = ctk.CTk()
window.title("DCID - Keypress BOT")
window.geometry("900x500")
window.minsize(width=500, height=400)

#window._set_appearance_mode("light") # light, dark e system

sidebar = ctk.CTkFrame(master=window, width=200, height=430).place(x=10, y=60)
ctk.CTkFrame(master=window, width=200, height=430).place(x=220, y=60)
ctk.CTkFrame(master=window, width=200, height=430).place(x=430, y=60)

window.mainloop()
