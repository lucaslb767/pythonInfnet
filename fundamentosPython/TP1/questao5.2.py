
#2 - Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.

tupla_original = ("teste1","teste2","teste3","teste4")
metade_primeira = ()
metade_segunda = ()



tamanho_tupla_original = len(tupla_original)

if tamanho_tupla_original%2 == 0:
    for i in range(0,int(tamanho_tupla_original/2)):
        metade_primeira += (tupla_original[i],)
        
    for j in range(int(tamanho_tupla_original/2), tamanho_tupla_original):
        metade_segunda +=(tupla_original[j],)
        
else:
    for i in range(0,(int(tamanho_tupla_original/2))+1):
        metade_primeira += (tupla_original[i],)
        
    for j in range((int(tamanho_tupla_original/2))+1, tamanho_tupla_original):
        metade_segunda +=(tupla_original[j],)
        
print(metade_primeira)
print(metade_segunda)