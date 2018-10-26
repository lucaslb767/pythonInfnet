#4. Escreva um programa em Python que calcule o fatorial de um dado número N usando um while. Use as mesmas especificações do item anterior.

n = int(input('Digite o valor desejado para calcular o fatorial de N: '))

while n<0 :
    n = int(input('N precisa ser não negativo para calcular fatorial. Digite um valor positivo para n: '))
    
if n==0 :
    print('O valor fatorial de',n,'é 1')
    
else:
    
    resultado = 1
    cont = n
    while cont>0:
        resultado = resultado*cont
        cont -= 1

    print('o valor fatorial de',n,'é',resultado)