
n = int(input('digite o valor para calcular o fatorial: '))
resultado = 1

for i in range(1, n+1):
    resultado = resultado*i
    
print('O fatorial de',n,'é',resultado)