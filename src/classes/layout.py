import tkinter as tk

class Layout:
    """
    KeyBoard Classe
    """
    def Window(title, size):
        janela = tk.Tk()
        janela.title(title)
        janela.geometry(size)
    
        return janela

    def Div(parent, attr={}, position='left'):
        div = tk.Frame(parent, attr)
        div.pack(side=position, fill="x")
        return div

    def ClearDiv(frame):
        for widget in frame.winfo_children():
            widget.destroy()
            return frame

    def Router( frame, route):
        for widget in frame.winfo_children():
            widget.destroy()
        # Carrega o novo conteúdo de acordo com o tipo_conteudo
        if route == "home":
            conteudo_label = tk.Label(frame, text="Configurações", font=("Arial", 20), width=450)
            conteudo_label.pack(pady=20)
        elif route == "EditPerfil":
            print("Estamos editando um perfil")

    def atualizar_conteudo(frame, content, sizeW):
        for widget in frame.winfo_children():
            widget.destroy()
        
        conteudo_label = tk.Label(frame, text=content['title'], font=("Arial", 20), width=sizeW)
        conteudo_label.pack(pady=20)

    def Links(self, args):
        print()
        link_home = []
        for n, l in enumerate(args['links']):
            print(n, l)
            link_home.append(tk.Button(
                args['side_in'], 
                text=l['title'], 
                command=lambda content=l, self=self: self.atualizar_conteudo(args['side_out'], content, args['sizeW'])
            ))
            link_home[n].pack(side="left", padx=20, pady=10)
