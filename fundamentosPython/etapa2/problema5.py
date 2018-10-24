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
    base = float(1/base)
    
    expoente = expoente *(-1)
    
    while expoente > contador :#importante não colocar >=, pois isso gera um ciclo de repetição a mais, dado que o contador começa do 0.
        
        resultado = resultado * base
        
        contador += 1
    
print('O resultado é', resultado)        
        
        
    