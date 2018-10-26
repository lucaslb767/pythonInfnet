#1. Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive. O número N deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma.

numeros_impares = []

input_usuario = str(input('Digite o numero desejado(digite sair para terminar) '))



while input_usuario != "sair":
    
    numero = int(input_usuario)
    
    if numero%2 != 0:
        
        numeros_impares += (numero,)
        
    input_usuario = str(input('Digite o próximo numero desejado(digite sair para terminar) '))
    
    

tamanho_impares = len(numeros_impares)

resultado = 0

for i in range(0,tamanho_impares):
    
    resultado = resultado + numeros_impares[i]
    

print("A soma dos números ímpares digitados é",resultado)