#criar dicionario onde a chave é o nome do arquivo e o valor é uma lista de dados contendo: tamanho do arquivo, data de criação, data de modificação

import os
from datetime import datetime

arquivos = os.listdir()
print(arquivos)


dicionario ={}

for arquivo in arquivos:
    print(os.path.isfile(arquivo))
    if os.path.isfile(arquivo):
        dicionario[arquivo] = []
        dicionario[arquivo].append(os.stat(arquivo).st_size)
        dicionario[arquivo].append(datetime.fromtimestamp(os.stat(arquivo).st_atime).strftime('%Y-%m-%d %H:%M:%S'))
        dicionario[arquivo].append(datetime.fromtimestamp(os.stat(arquivo).st_mtime).strftime('%Y-%m-%d %H:%M:%S'))
        print('O arquivo', arquivo,'com os seguintes valores', dicionario[arquivo])