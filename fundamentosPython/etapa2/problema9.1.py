#Suponha, agora, que você precise guardar também o número de telefone de cada um deles. Seria um espécie de agenda telefônica.

nomes=()
telefones=()

nome_amigo= str(input("Quem é a primeira pessoa?(digite sair para concluir)"))

while nome_amigo != "sair":
    
    telefones_amigo = str(input('Qual é o número desta pessoa? '))
    
    nomes += (nome_amigo,)
    
    telefones += (telefones_amigo,)
    
    nome_amigo= str(input("Quem é a próxima pessoa?(digite sair para concluir)"))
    

tamanho_lista_nome = len(nomes)
tamanho_lista_telefones = len(telefones)

if tamanho_lista_nome != tamanho_lista_telefones :
    print('A lista de nomes está com quantidade diferente da lista de telefone')
    
else:
    
    for i in range(0,tamanho_lista_nome):
        print(nomes[i],":",telefones[i])
    