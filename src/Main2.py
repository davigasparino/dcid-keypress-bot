import configparser
import json

from classes.keyboard import KeyBoard

pressedKey = KeyBoard('w', 5)

pressedKey.pressed()

def salvar_dado(valor: str, nome_arquivo: str = "data.txt"):
    """
    Salva um valor em um arquivo de texto interno da aplicação.

    Argumentos:
        valor (str): O valor a ser salvo no arquivo.
        nome_arquivo (str): O nome do arquivo de texto interno (opcional, padrão "dados.txt").
    """
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(valor)

def recuperar_dado(nome_arquivo: str = "data.txt") -> str:
    """
    Recupera o valor salvo em um arquivo de texto interno da aplicação.

    Argumentos:
        nome_arquivo (str): O nome do arquivo de texto interno (opcional, padrão "dados.txt").

    Retorno:
        str: O valor recuperado do arquivo.
    """
    try:
        with open(nome_arquivo, "r") as arquivo:
            valor_salvo = arquivo.read()
        return valor_salvo
    except FileNotFoundError:
        return ""

# Exemplo de uso
#valor_recebido = input("Digite o valor a ser salvo: ")
#salvar_dado(valor_recebido)

valor_recuperado = recuperar_dado()
print(f"Valor recuperado do arquivo: {valor_recuperado}")

# =========================================================================================


def salvar_configuracoes(configuracoes: dict, file_name: str = "configuracoes.ini"):
    """
    Salva as configurações em um arquivo INI interno da aplicação.

    Argumentos:
        configuracoes (dict): Um dicionário contendo as configurações chave-valor.
        file_name (str): O nome do arquivo INI interno (opcional, padrão "configuracoes.ini").
    """
    config = configparser.ConfigParser()
    config['Configuracoes'] = configuracoes
    with open(file_name, "w") as arquivo:
        config.write(arquivo)

def carregar_configuracoes(file_name: str = "configuracoes.ini") -> dict:
    """
    Carrega as configurações do arquivo INI interno da aplicação.

    Argumentos:
        file_name (str): O nome do arquivo INI interno (opcional, padrão "configuracoes.ini").

    Retorno:
        dict: Um dicionário contendo as configurações chave-valor.
    """
    config = configparser.ConfigParser()
    config.read(file_name)
    return config['Configuracoes']

def editar_configuracao(chave: str, novo_valor: str, file_name: str = "configuracoes.ini"):
    """
    Edita o valor de uma configuração específica no arquivo INI.

    Argumentos:
        chave (str): A chave da configuração a ser editada.
        novo_valor (str): O novo valor para a configuração.
        file_name (str): O nome do arquivo INI interno (opcional, padrão "configuracoes.ini").
    """
    configuracoes = carregar_configuracoes(file_name)
    configuracoes[chave] = novo_valor
    salvar_configuracoes(configuracoes, file_name)

# Exemplo de uso
configuracoes_iniciais = {
    "background": "gold",
    "color": "red",
    "title": "blue"
}

salvar_configuracoes(configuracoes_iniciais)

# Carregar e exibir as configurações
configuracoes_carregadas = carregar_configuracoes()
print(configuracoes_carregadas)

# Editar a configuração "background"
editar_configuracao("background", "white")

# Carregar e exibir as configurações após a edição
configuracoes_carregadas = carregar_configuracoes()
print(configuracoes_carregadas)
