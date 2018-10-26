#3 - Dada uma tupla e um elemento, elimine esse elemento da tupla.

def elimina_elemento(tupla, elemento):
    
    list_tupla = list(tupla)
    
    
    if elemento in list_tupla:
        index_elemento = list_tupla.index(elemento)
        list_tupla.pop(index_elemento)
        print(list_tupla)
    
    else:
        print('elemento não encontrado')
        
        

tupla = ("teste1","teste2","teste3")

elimina_elemento(tupla,"teste2")

