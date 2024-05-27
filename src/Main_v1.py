import tkinter as tk
from classes.DataJson import DataJson as dj
import json

class MinhaAplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Layout Personalizado")
        self.root.geometry("800x500")

        self.FieldsList = []
        
        self.sidebar = tk.Frame(self.root, bg="#d9d9d9")
        self.sidebar.pack(side="left", fill="y", padx=20, pady=20)

        self.botao_home = tk.Button(self.sidebar, text="Home", command=self.CLearContainer)
        self.botao_home.pack(pady=10)

        self.botao_config = tk.Button(self.sidebar, text="Configurações")
        self.botao_config.pack(pady=10)

        self.botao_perfis = tk.Button(self.sidebar, text="Perfis", command=self.ViewProfiles)
        self.botao_perfis.pack(pady=10)

        self.Container = tk.Frame(self.root, bg="#e3e3e3")
        self.Container.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        

    def NewRow(self):
        
        row = tk.Frame(self.Container)
        row.pack(fill="x", pady=5)

        # Key
        key = tk.Label(row, text="Key:")
        key.pack(side="left", padx=5)
        
        # field de texto
        keyValue = tk.Entry(row)
        keyValue.pack(side="left", padx=5)

        # Rótulo
        pressTime = tk.Label(row, text="Times")
        pressTime.pack(side="left", padx=5)

        # field de texto
        pressTimeValue = tk.Entry(row)
        pressTimeValue.pack(side="left", padx=5)

        # Caixa de seleção
        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(row, text="Opção", variable=checkbox_var)
        checkbox.pack()

        self.FieldsList.append([
            keyValue,
            pressTimeValue,
            checkbox_var
        ])

    def saveItems(self):        
        items = []
        for n, field in enumerate(self.FieldsList):
            if n > 0:
                items.append({
                    "key": field[0].get(),
                    "pressed": field[1].get(),
                    "random": field[2].get()
                })

        sendJson = {
            "title": self.FieldsList[0][0].get(),
            "keys": items
        }

        try:
            saveJson = dj()
            saveJson.insertItem(sendJson)

            self.ViewProfiles("Inserido com sucesso!")
        except Exception as e:
            raise e
        

    def CLearContainer(self):
        for widget in self.Container.winfo_children():
            widget.destroy()

    def ViewProfiles(self, message = ""):
        self.CLearContainer()

        if message:
            m = tk.Label(self.Container, text=message)
            m.pack(side="top", padx=5)

        title = tk.Label(self.Container, text="Profiles")
        title.pack(side="top", padx=5)
        
        addProfile = tk.Button(self.Container, text="Add Profile", command=self.ViewAddProfile)
        addProfile.pack(pady=10)

    def ViewAddProfile(self):
        self.CLearContainer()

        title = tk.Label(self.Container, text="Title")
        title.pack(side="top", padx=5)
        titleValue = tk.Entry(self.Container)
        titleValue.pack(side="top", padx=5)
        self.FieldsList.append([
            titleValue
        ])
        
        self.btnNew = tk.Button(self.Container, text="Novo", command=self.NewRow)
        self.btnNew.pack(pady=10)

        self.btnSave = tk.Button(self.Container, text="Salvar", command=self.saveItems)
        self.btnSave.pack(side="bottom", pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = MinhaAplicacao(root)
    root.mainloop()
