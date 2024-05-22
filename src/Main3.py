import tkinter as tk
configs_container = {
    "width": 500, 
    "height": 450, 
    "background": "#f5f5f5"
}
configs_sidebar = {
    "width": 150, 
    "height": 450, 
    "background": "#d5d5d5"
}
configs_navbar = {
    "width": 650, 
    "height": 50, 
    "background": "#b2b2b2"
}
btn_styles = {
    "foreground": "blue", 
    "background": "white",
    "activebackground": "blue",
    "activeforeground": "yellow",
    "borderwidth": 0
}

profiles = [
    {
        "title": "primeiro Profile",
        "name": "p_0",
        "keys": [
            {"Tecla": "w", "Tempo": 12},
            {"Tecla": "d", "Tempo": 9},
            {"Tecla": "s", "Tempo": 7},
            {"Tecla": "a", "Tempo": 5}
        ],
        "press": 8
    },
    {
        "title": "segundo Profile",
        "name": "p_1",
        "keys": [
            {"Tecla": "space", "Tempo": 5},
            {"Tecla": "q", "Tempo": 2},
            {"Tecla": "2", "Tempo": 4},
            {"Tecla": "5", "Tempo": 6}
        ],
        "press": 18
    }
]

def exibir_campo_configuracoes():
    """
    Exibe o campo de entrada de texto para configurações.
    """
    print(profiles[0])
    conteudo_label = tk.Label(FrameContainerContent, text="Configurações", font=("Arial", 20), width=450)
    conteudo_label.pack(pady=20)
    
    # Cria o campo de entrada de texto
    campo_configuracoes = tk.Entry(FrameContainerContent)
    campo_configuracoes.pack(pady=20)

    # Cria um botão para enviar os dados do campo de texto
    botao_enviar = tk.Button(FrameContainerContent, text="Enviar", command=lambda: enviar_dados_configuracoes(campo_configuracoes.get()))
    botao_enviar.pack(pady=10)

def enviar_dados_configuracoes(texto_entrada):
    """
    Função para enviar os dados do campo de entrada de texto.

    :param texto_entrada: Texto digitado no campo de entrada.
    """
    print(f"Dados de configuração enviados: {texto_entrada}")

def profileSaveConfigs(values):
    print(values)

    for v in values:
        print(f"Items: {v['entry'].get()} \n Objeto inteiro: {v}")
    # Insira aqui o código para realmente enviar os dados (ex: para um servidor, arquivo, etc.)


def abrir_configuracoes():
    """
    Exibe o campo de entrada de texto para configurações.
    """
    exibir_campo_configuracoes()

def createDynamicFields(frame, title, name):
    # Create the title label
        title_label = tk.Label(frame, text=f"{title}")
        title_label.pack()

        # Create the entry field and store it in the dictionary
        entry = tk.Entry(frame)

        # Prepopulate the entry field with the value
        entry.insert(0, name)

        # Pack the entry field
        entry.pack(pady=10)
        # Cria o campo de entrada de texto

        return entry

def profileEdit():
    conteudo_label = tk.Label(FrameContainerContent, text="Perfis", font=("Arial", 20), width=450)
    conteudo_label.pack(pady=20)

    values = []
    i = 0
    for p in profiles:

        entry = createDynamicFields(FrameContainerContent, p['title'], p['name'])
        values.append(p)
        values[i]['entry'] = entry

        table_frame = tk.Frame(FrameContainerContent)
        table_frame.pack()
        
        for row_num, row_data in enumerate(p['keys']):
            for col_num, (col_name, col_value) in enumerate(row_data.items()):
                row_label = tk.Label(table_frame, text="")
                row_label.grid(row=row_num + 1, column=col_num, sticky="nsew")

                row_label = createDynamicFields(row_label, col_name, col_value)
                print("col_value", col_value)
                print(" - - - - - - - - - - - - ")

        # for k in p['keys']:
        #     entry = createDynamicFields(FrameContainerContent, 'Tecla', k[0])
        #     entry = createDynamicFields(FrameContainerContent, 'Tempo', k[1])

        i += 1

    print(values)
    
    # Cria um botão para enviar os dados do campo de texto
    botao_enviar = tk.Button(FrameContainerContent, text="Salvar", command=lambda: profileSaveConfigs(values))
    botao_enviar.pack(pady=10)

def OpenProfileEdit():
    """
    Exibe o campo de entrada de texto para configurações.
    """
    profileEdit()

def atualizar_texto_conteudo(texto):
    """
    Cria ou atualiza a label com o texto especificado dentro do FrameContainerContent.

    :param texto: Texto a ser exibido na label.
    """
    conteudo_label = ''

    if not conteudo_label:
        conteudo_label = tk.Label(FrameContainerContent, configs_container, text=texto, font=("Arial", 16))
        conteudo_label.pack(pady=20)
    else:
        conteudo_label.config(text=texto)


# Função para atualizar o conteúdo
def atualizar_conteudo(tipo_conteudo):
    """
    Atualiza o conteúdo do FrameContainerContent de acordo com o tipo_conteudo.

    :param tipo_conteudo: Tipo de conteúdo a ser exibido ("home" ou "configuracoes").
    """
    # Limpa o conteúdo atual do FrameContainerContent
    for widget in FrameContainerContent.winfo_children():
        widget.destroy()

    # Carrega o novo conteúdo de acordo com o tipo_conteudo
    if tipo_conteudo == "home":
        atualizar_texto_conteudo("Olá, você está na Home!")
    elif tipo_conteudo == "configuracoes":
        abrir_configuracoes()
    elif tipo_conteudo == "EditPerfil":
        OpenProfileEdit()
    elif tipo_conteudo == "EditPerfil":
        OpenProfileEdit()


# Criando a janela principal
janela = tk.Tk()
janela.title("Minha Interface")
janela.geometry("650x500")

# Criando o quadrado principal (frame_total)
frame_total = tk.Frame(janela, width=650, height=500, background="red")
frame_total.pack()

# Criando o retângulo superior para os botões (FrameNavbar)
FrameNavbar = tk.Frame(frame_total, configs_navbar)
FrameNavbar.pack(side="top", fill="x")

# Criando os botões dentro do FrameNavbar
link_home = tk.Button(FrameNavbar, text="Home", command=lambda: atualizar_conteudo("home"))
link_home.pack(side="left", padx=20, pady=10)

link_configuracoes = tk.Button(FrameNavbar, text="Configurações", command=lambda: atualizar_conteudo("configuracoes"))
link_configuracoes.pack(side="left", padx=20, pady=10)

link_config_perfis = tk.Button(FrameNavbar, text="Perfis", command=lambda: atualizar_conteudo("EditPerfil"))
link_config_perfis.pack(side="left", padx=20, pady=10)

# Criando o retângulo inferior para o conteúdo (FrameContainerContent)
FrameContainer = tk.Frame(frame_total, width=650, height=450, background="gray")
FrameContainer.pack(side="bottom", fill="both", expand=True)

FrameContainerSidebar = tk.Frame(FrameContainer, configs_sidebar)
FrameContainerSidebar.pack(side="left", fill="both", expand=True)

FrameContainerContent = tk.Frame(FrameContainer, configs_container)
FrameContainerContent.pack(side="right", fill="both", expand=True)



# Conteúdo inicial (pode ser um texto de placeholder)
#inicial = tk.Label(FrameContainerContent, text="Conteúdo Inicial", font=("Arial", 16))
#inicial.pack(pady=20)

# Executando a interface
janela.mainloop()
