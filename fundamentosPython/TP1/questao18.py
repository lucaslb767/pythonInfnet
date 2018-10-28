#18. (desafio) Em jogos antigos era possível ver que os desenhos eram compostos por vários triângulos. Como uma maneira de treinar isso, a partir do N dado pelo usuário desenhe um polígono de lado N composto somente por triângulos como na figura:

import turtle
import math

def poligono(n):
    
    #turtle.speed('fastest')
    
    angulo_central = (360/n)
    angulo_b = int(180-angulo_central)/2
    angulo_c = int(180-angulo_central)/2
    
    lado2 = 100
    lado3 = 100
    
    lado1 = (lado2**2 + lado3**2 -2*(lado2*lado3*math.cos(math.radians(angulo_central))))**(1/2)
    print(lado1)
    
    for i in range(0,n):
        
        turtle.forward(lado1)
        turtle.left(180 - angulo_c)
        turtle.forward(lado2)
        turtle.left(180 - angulo_central)
        turtle.forward(lado3)
        turtle.left(180 - angulo_b)
        turtle.forward(lado1)
        turtle.left(angulo_central)
    
    
    
poligono(8)