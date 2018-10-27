#10. Faça uma função no Python que, utilizando a ferramenta turtle, desenhe um quadrado de lado N.

import turtle

def quadrado(n):
    turtle.speed('fastest')
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)

n = int(input('Qual é o tamanho do lado desejado? '))

quadrado(n)