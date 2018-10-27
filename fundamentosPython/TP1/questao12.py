#12. Faça uma função no Python que, utilizando a ferramenta turtle, desenhe um círculo de raio N.

import turtle

turtle.speed('fastest')

def circulo(raio):
    turtle.circle(raio)
    

n = int(input('Qual é o tamanho do raio? '))

circulo(n)