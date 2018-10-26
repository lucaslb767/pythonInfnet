#3. Escreva uma função em Python que calcule o fatorial de um dado número N usando um for. O fatorial de N=0 é um. O fatorial de N é (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1. Por exemplo, para N=5 o fatorial é: 5 x 4 x 3 x 2 x 1 = 120. Se N for negativo, exiba uma mensagem indicando que não é possível calcular seu fatorial.

n = int(input('Digite o valor desejado para calcular o fatorial de N: '))

while n<0 :
    n = int(input('N precisa ser não negativo para calcular fatorial. Digite um valor positivo para n: '))
    
if n==0 :
    print('O valor fatorial de',n,'é 1')
    
else:
    
    resultado = 1
    for x in range(n,0,-1):
        resultado = resultado*x

    print('o valor fatorial de',n,'é',resultado)
    