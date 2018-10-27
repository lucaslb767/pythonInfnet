#Faça uma função que desenhe o triângulo obtido na questão 7 com a ferramenta turtle.
import turtle
import math

turtle.speed('fastest')

def triangulo(x,y,z):
    if x>y+z or y>z+x or z>x+y :
        print('O tamanho de um dos lados é maior do que a soma dos outros 2')
    
    else:

        cosX = math.degrees(math.acos(((y * y) + (z * z) - (x * x)) / (2 * y * z)))
        cosY = math.degrees(math.acos(((z * z) + (x * x) - (y * y)) / (2 * z * x)))
        cosZ = math.degrees(math.acos(((x * x) + (y * y) - (z * z)) / (2 * x * y)))

        turtle.forward(x)
        turtle.left(int(180 - cosZ))
        turtle.forward(y)
        turtle.left(int(180 - cosX))
        turtle.forward(z)
        turtle.left(180 - cosY)
        
        
        
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