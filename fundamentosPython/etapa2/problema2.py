#1 litro de tinta para cada 3 metros quadrado
#Cada lata de tinta tem 18 litros e custa 80 reais
#Faça um algoritmo que calcule a quantidade de latas necessárias

area = int(input('Qual é a area em metros quadrados que precisa ser pintada?'))

tinta_necessaria = float(area/3)

if tinta_necessaria % 3 == 0:
    total_latas = int(tinta_necessaria/18)
                 
else:
    total_latas = int(tinta_necessaria/18) + 1
                 

custo = str(float(total_latas * 80))

total_custo = 'R$' + custo


if total_latas == 1:
    print('Você precisará de ', tinta_necessaria, ' litros de tinta. Para tanto, é necessária ', total_latas, 'lata, que custará, no total,', total_custo)
else:
    print('Você precisará de ', tinta_necessaria, ' litros de tinta. Para tanto, são necessárias ', total_latas, 'latas, que custará, no total,', total_custo)
                 

