numeros = [129,220,87123,88282,4]

menor = 8718728171

for i in range(len(numeros)):
    if numeros[i] < menor:
        print(numeros[i],'é menor que',menor)
        menor = numeros[i]
        
print('O menor número é: ', menor)        
