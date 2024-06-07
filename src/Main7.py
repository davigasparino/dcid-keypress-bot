import customtkinter as ctk

window = ctk.CTk()
window.title("DCID - Keypress BOT")
window.geometry("900x500")
window.minsize(width=500, height=400)

#window._set_appearance_mode("light") # light, dark e system

#sidebar = ctk.CTkFrame(master=window, width=200, height=430).place(x=10, y=60)
#ctk.CTkFrame(master=window, width=200, height=430).place(x=220, y=60)
#ctk.CTkFrame(master=window, width=200, height=430).place(x=430, y=60)

# tabView = ctk.CTkTabview(window, width=600)
# tabView.pack()
# tabView.add("Pincipal")
# tabView.add("Procedures")
# tabView.add("Settings")
# tabView.tab("Pincipal").grid_columnconfigure(0, weight=1)
# tabView.tab("Procedures").grid_columnconfigure(0, weight=1)
# tabView.tab("Settings").grid_columnconfigure(0, weight=1)

# title = ctk.CTkLabel(tabView.tab("Procedures"), text="Gerenciar Procedures")
# title.pack()

# textbox = ctk.CTkTextbox(window, width=300, height=200)
# textbox.pack()
# textbox.insert("0.0", "texto")

# selectItemValue = ctk.StringVar(value="escolha uma opção")
# def selectItem(item):
#     print(f'O item selecionado foi {item}')

# select = ctk.CTkOptionMenu(window, values=[
#     "Primeiro opção",
#     "Segunda opção"
# ], command=selectItem, variable=selectItemValue)
# select.pack()

window.mainloop()
