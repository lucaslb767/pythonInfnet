#Escreva um programa em Python que receba três valores reais X, Y e Z, guarde esses valores numa tupla e verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste caso, retorne qual o tipo de triângulo formado.
#Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento de cada lado de um triângulo deve ser menor do que a soma do comprimento dos outros dois lados. Além disso, o programa deve identificar o tipo de triângulo formado observando as seguintes definições:
#Triângulo Equilátero: os comprimentos dos três lados são iguais.
#Triângulo Isósceles: os comprimentos de dois lados são iguais.
#Triângulo Escaleno: os comprimentos dos três lados são diferentes

def triangulo(x,y,z):
    if x>y+z or y>z+x or z>x+y :
        print('O tamanho de um dos lados é maior do que a soma dos outros 2')
    
    else:
        valores = (x,y,z)
        if x==y and y==z :
            print('Triângulo Equilátero')
        elif x==y or y==z or x==z:
            print('Triângulo Isósceles')
            
        elif x!=y and y!=z and x!=z:
            print('Triângulo Escaleno')

a = int(input('Qual é o tamanho do primeiro lado? '))
b = int(input('Qual é o tamanho do segundo lado? '))
c = int(input('Qual é o tamanho do terceiro lado? '))

triangulo(a,b,c)

            