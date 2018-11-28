#Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada. Indique quais frases apresentam a palavra “eu”. (código)

input_usuario = str(input('Digite sua frase (digite "sair" para terminar): '))

lista_frases = []

while input_usuario != 'sair':

    lista_frases.append(input_usuario)
    input_usuario = str(input('Digite sua próxima frase (digite "sair" para terminar): '))

for frases in lista_frases:

    list = frases.split(' ')

    if "eu" in list:
        print('A frase "', frases, '" possui a palavra  "eu"')