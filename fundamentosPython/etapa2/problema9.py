#Escreva um programa em Python que leia da entrada cada nome de um amigo e os armazene em uma tupla. O término das entradas ocorre quando o usuário digitar “sair”. Imprima cada elemento da tupla separadamente no final.

nomes = ()

nomes_input = str(input('Qual é a primeira pessoa a ser cadastrada(digite sair para terminar o cadastro) ? '))

while nomes_input != "sair":
    
    nomes += (nomes_input,)
    
    nomes_input = str(input('Quem é a próxima(digite sair para terminar o cadastro) ? '))
    
tamanho_nomes = len(nomes)

for i in range(0, tamanho_nomes):
    print(nomes[i])