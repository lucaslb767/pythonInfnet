#Escreva um programa em Python que leia nomes de alunos e suas alturas em metros até que um nome de aluno seja o código de saída “Sair”. O programa deve possuir uma função que indica todos os alunos que tenham altura acima da média (a média aritmética das alturas de todos os alunos lidos). (código)

input_aluno = str(input('Qual é o nome do aluno?(digite "sair" para terminar) ').lower())

lista_alunos = []
lista_tamanho = []
while input_aluno != 'sair':

    input_tamanho = float(input('Qual é a altura do aluno em metros? '))
    lista_alunos.append(input_aluno)
    lista_tamanho.append(input_tamanho)

    input_aluno = str(input('Qual é o nome do próximo aluno?(digite "sair" para terminar) ').lower())

print('alunos', lista_alunos, '\ntamanhos', lista_tamanho)

def alunos_maior_media (lista_nomes, lista_tamanho):

    media_de_altura = sum(lista_tamanho)/len(lista_tamanho)
    print('A média de altura é:', media_de_altura)

    for tamanho in lista_tamanho:

        index_tamanho = lista_tamanho.index(tamanho)

        if tamanho > media_de_altura:


           print(lista_nomes[index_tamanho].title(), 'tem altura de', tamanho, 'e por isso é maior que a média')

        else:
            print(lista_nomes[index_tamanho].title(), 'tem altura de', tamanho, 'e por isso NÃO é maior que a média')

alunos_maior_media(lista_alunos, lista_tamanho)
