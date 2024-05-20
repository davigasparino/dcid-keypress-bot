import tkinter as tk

def ir_para_home():
    # Insira o código que você deseja executar quando o botão "Home" for clicado
    print("Clicou em Home!")

def abrir_configuracoes():
    # Insira o código que você deseja executar quando o botão "Configurações" for clicado
    print("Clicou em Configurações!")

def abrir_conteudo(tipo_conteudo):
    # Insira o código que carrega o conteúdo específico (ex: página, imagem, etc.)
    # de acordo com o tipo_conteudo ("home" ou "configuracoes")
    print(f"Abrindo conteúdo: {tipo_conteudo}")

def exibir_campo_configuracoes():
    """
    Exibe o campo de entrada de texto para configurações.
    """
    # Cria o campo de entrada de texto
    campo_configuracoes = tk.Entry(frame_conteudo, width=50)
    campo_configuracoes.pack(pady=20)

    # Cria um botão para enviar os dados do campo de texto
    botao_enviar = tk.Button(frame_conteudo, text="Enviar", command=lambda: enviar_dados_configuracoes(campo_configuracoes.get()))
    botao_enviar.pack(pady=10)

def enviar_dados_configuracoes(texto_entrada):
    """
    Função para enviar os dados do campo de entrada de texto.

    :param texto_entrada: Texto digitado no campo de entrada.
    """
    print(f"Dados de configuração enviados: {texto_entrada}")
    # Insira aqui o código para realmente enviar os dados (ex: para um servidor, arquivo, etc.)


def abrir_configuracoes():
    """
    Exibe o campo de entrada de texto para configurações.
    """
    exibir_campo_configuracoes()

def atualizar_texto_conteudo(texto):
    """
    Cria ou atualiza a label com o texto especificado dentro do frame_conteudo.

    :param texto: Texto a ser exibido na label.
    """
    global conteudo_label

    if texto == '':
        texto = "Olá, você está na Home!"
    

    if not conteudo_label:
        conteudo_label = tk.Label(frame_conteudo, text=texto, font=("Arial", 16))
        conteudo_label.pack(pady=20)
    else:
        conteudo_label.config(text=texto)


# Função para atualizar o conteúdo
def atualizar_conteudo(tipo_conteudo):
    """
    Atualiza o conteúdo do frame_conteudo de acordo com o tipo_conteudo.

    :param tipo_conteudo: Tipo de conteúdo a ser exibido ("home" ou "configuracoes").
    """
    # Limpa o conteúdo atual do frame_conteudo
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    # Carrega o novo conteúdo de acordo com o tipo_conteudo
    if tipo_conteudo == "home":
        atualizar_texto_conteudo("Olá, você está na Home!")
    elif tipo_conteudo == "configuracoes":
        abrir_configuracoes()


# Criando a janela principal
janela = tk.Tk()
janela.title("Minha Interface")
janela.geometry("500x500")

# Criando o quadrado principal (frame_total)
frame_total = tk.Frame(janela, width=500, height=500, background="red")
frame_total.pack()

# Criando o retângulo superior para os botões (frame_botoes)
frame_botoes = tk.Frame(frame_total, width=500, height=50, background="lightblue")
frame_botoes.pack(side="top", fill="x")

# Criando os botões dentro do frame_botoes
link_home = tk.Button(frame_botoes, text="Home", command=lambda: atualizar_conteudo("home"))
link_home.pack(side="left", padx=20, pady=10)

link_configuracoes = tk.Button(frame_botoes, text="Configurações", command=lambda: atualizar_conteudo("configuracoes"))
link_configuracoes.pack(side="right", padx=20, pady=10)

# Criando o retângulo inferior para o conteúdo (frame_conteudo)
frame_conteudo = tk.Frame(frame_total, width=500, height=450, background="yellow")
frame_conteudo.pack(side="bottom", fill="both", expand=True)

# Conteúdo inicial (pode ser um texto de placeholder)
inicial = tk.Label(frame_conteudo, text="Conteúdo Inicial", font=("Arial", 16))
inicial.pack(pady=20)

# Executando a interface
janela.mainloop()
