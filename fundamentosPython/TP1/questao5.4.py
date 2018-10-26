#4 - Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.

def inverte_tupla(tupla):
    tupla_invertida = ()
    
    tamanho_tupla = len(tupla)
    
    for i in range((tamanho_tupla -1),-1,-1):
        tupla_invertida += (tupla[i],)
    
    print('Inversão:',tupla_invertida )
    
tupla = (1,2,3,4,5)

inverte_tupla(tupla)
        
