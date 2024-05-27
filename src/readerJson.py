import json

jsonFile = 'src/data/profiles.json'

def insertItem():
    # Leitura do arquivo JSON
    with open(jsonFile, 'r') as arquivo_json:
        dados_json = json.load(arquivo_json)

    # Preparando o novo nó
    novo_no = {"key": "d", "pressed": 5, "random": "true"}

    # Abrindo o arquivo para escrita (novo bloco `with`)
    with open('src/data/profiles.json', 'w') as arquivo_json_escrita:
        # Inserindo o novo nó na lista
        dados_json.append(novo_no)

        # Gravando as modificações no arquivo
        json.dump(dados_json, arquivo_json_escrita, indent=4)

def updateItem(position):
    import json

    # Carregue o conteúdo do JSON em um objeto Python
    with open(jsonFile, 'r') as arquivo_json:
        dados_json = json.load(arquivo_json)

    # Acesse o segundo nó
    segundo_no = dados_json[position]

    # Altere os valores desejados
    segundo_no["pressed"] = 74
    segundo_no["random"] = 'false'

    # Atualize o arquivo JSON com as modificações
    with open(jsonFile, 'w') as arquivo_json:
        json.dump(dados_json, arquivo_json, indent=4)

updateItem(0)