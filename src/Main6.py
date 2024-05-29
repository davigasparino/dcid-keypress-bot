import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Exemplo de Checkbutton")

    # Variável para armazenar o estado do Checkbutton
    checkbox_var = tk.BooleanVar()

    # Defina o valor padrão como True (marcado)
    checkbox_var.set(True)  # Altere para False se desejar desmarcar por padrão

    # Crie o Checkbutton
    checkbox = tk.Checkbutton(root, text="Random", variable=checkbox_var)
    checkbox.pack(side="left", padx=5)

    # Função para exibir o estado do Checkbutton
    def mostrar_estado():
        print("Estado do Checkbutton:", checkbox_var.get())

    # Botão para verificar o estado
    btn_verificar = tk.Button(root, text="Verificar Estado", command=mostrar_estado)
    btn_verificar.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
