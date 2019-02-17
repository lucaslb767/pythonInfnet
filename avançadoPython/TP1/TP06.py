import os

path = os.path.abspath('C:/Users/Lucas/Downloads/python-3.7.2.exe')

path_split = os.path.split(path)

file_extension = path_split[1].split('.')

print('Extensão do arquivo selecionado é: ',file_extension[-1])