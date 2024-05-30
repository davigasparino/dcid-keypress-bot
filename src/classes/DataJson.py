import json
import os

class DataJson:

    jsonFile = os.path.join(os.getcwd()+'\data', 'profiles.json')
    BD = os.path.join(os.getcwd()+'\data', 'bd.json')

    def ReadItems(self):
        with open(self.jsonFile, 'r') as arquivo_json:
            dados_json = json.load(arquivo_json)
        return dados_json


    def insertItem(self, items):
        # Leitura do arquivo JSON
        with open(self.jsonFile, 'r') as arquivo_json:
            dados_json = json.load(arquivo_json)

        sequence = self.getSequence()

        # Abrindo o arquivo para escrita (novo bloco `with`)
        with open(self.jsonFile, 'w') as arquivo_json_escrita:
            # Inserindo o novo nó na lista
            dados_json.append({
                "id": sequence,
                "data": items
            })

            # Gravando as modificações no arquivo
            json.dump(dados_json, arquivo_json_escrita, indent=4)

    def updateItem(self, position):
        import json

        # Carregue o conteúdo do JSON em um objeto Python
        with open(self.jsonFile, 'r') as arquivo_json:
            dados_json = json.load(arquivo_json)

        # Acesse o segundo nó
        segundo_no = dados_json[position]

        # Altere os valores desejados
        segundo_no["pressed"] = 74
        segundo_no["random"] = "false"

        # Atualize o arquivo JSON com as modificações
        with open(self.jsonFile, 'w') as arquivo_json:
            json.dump(dados_json, arquivo_json, indent=4)

    def getSequence(self):
        with open(self.BD, 'r') as data:
            sequence = json.load(data)
        
        sequence[0]['sequence'] = sequence[0]['sequence'] + 1
        
        with open(self.BD, 'w') as upSeq:
            json.dump(sequence, upSeq, indent=4)

        return sequence[0]['sequence']
