#11. Faça uma função no Python que, utilizando a ferramenta turtle, desenhe um triângulo de lado N.

import turtle

def triangulo(lado):
    turtle.fillcolor('red')
    angulo = 120
    
    turtle.speed('fastest')
    turtle.forward(lado)
    turtle.left(angulo)
    turtle.forward(lado)
    turtle.left(angulo)
    turtle.forward(lado)
    
lado = int(input('Qual é o tamanho do lado do triangulo? '))

triangulo(lado)
    