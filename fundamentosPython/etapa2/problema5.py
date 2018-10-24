#Escreva um programa em Python que peça dois números, base e expoente, calcule e mostre o primeiro elevado ao segundo número. Não utilize a função potência da linguagem.

base = int(input('Qual é a base? '))

expoente = int(input('Qual é o expoente'))

contador = 0

resultado = 1




    
if expoente >= 0 : 
    
    while expoente > contador :#importante não colocar >=, pois isso gera um ciclo de repetição a mais, dado que o contador começa do 0.
        
        resultado = resultado * base
        
        contador += 1
        
        
        
        
else :
    print('O número tem que ser maior que 0')
    
print('O resultado é', resultado)        
        
        
    