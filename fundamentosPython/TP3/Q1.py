
#a

lista = []


#b

for i in range(1,6):
    lista.append(i)

#c
print(lista)

#d

def remove_da_lista(lista, elemento):

    if elemento in lista:
        lista.remove(elemento)
    else:
        print('Elemento não encontrado')

remove_da_lista(lista, 3)
remove_da_lista(lista,6)

#e

print('lista modificada',lista)

#f
tamanho = len(lista)
print('tamanho da lista',tamanho)

#g

lista[tamanho -1 ] = 6
print('lista com ultimo número modificado', lista)

