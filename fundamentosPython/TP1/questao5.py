#1 - Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o indice do mesmo
#2 - Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.
#3 - Dada uma tupla e um elemento, elimine esse elemento da tupla.
#4 - Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.

#1
def existe_na_tupla(tupla,elemento):
    if elemento in tupla:
        index_elemento = tupla.index(elemento)
        
        print('O index do elemento', elemento,'é', index_elemento)
    else:
        print('elemento não encontrado')
        
        
tupla = ("vermelho", "sushi", 456, "armario")

existe_na_tupla(tupla, 456)