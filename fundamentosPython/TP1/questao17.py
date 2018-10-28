# 17. Escreva uma função que receba uma string e um número inteiro x e rotacione a string x posições para a esquerda. Assuma que a string tem pelo menos x caracteres.



def reverte_string(string, posicao):
    
    lista_string= list(string)
    
    tamanho_string = len(lista_string)
    
    lista1=[]
    
    if posicao > (tamanho_string - 1):
        print('a string selecionada não tem a posição desejada')
        
    else:
        
        for i in range(posicao, tamanho_string):
            lista1 += lista_string[i]
            
        for j in range(0, posicao):
            lista1 += lista_string[j]
    
    nova_string = ''.join(lista1)
    
    print(nova_string)
    
palavra = str(input('Qual é a string desejada? '))

posicao = int(input('Qual a posicao que deve comecar ordenar? '))

reverte_string(palavra, posicao)