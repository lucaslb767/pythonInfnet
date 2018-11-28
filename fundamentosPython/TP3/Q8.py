#Faça uma funçãoum programa em Python que simula um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor. Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores (1-6) e uma função do módulo 'random' de Python para gerar números aleatórios, simulando os lançamentos dos dados. (código)
import random

def lanca_dado(quantidade_lancamento):
    lista = []

    for lancamento in range(1, quantidade_lancamento +1):
        dado = random.randint(1,6)

        lista.append(dado)

    print('Jogadas individuais', lista)
    print('Tamanho da lista', len(lista))

    quantidade_numeros = {'1': lista.count(1), '2': lista.count(2), '3': lista.count(3), '4': lista.count(4), '5': lista.count(5), '6': lista.count(6)}

    print(quantidade_numeros)

lanca_dado(100)

