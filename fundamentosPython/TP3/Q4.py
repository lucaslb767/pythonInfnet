#Escreva um programa em Python que leia um vetor de números de tamanho t. Leia t previamente. Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele. (código)

vetor = [0,0,10,20,133,220]

t = len(vetor)

print('O vetor é:', vetor)
print('Este vetor tem ',t, 'elementos.')

print('O número 0 aparece', vetor.count(0), 'vezes.' )