#Escreva um programa em Python utilizando a ferramenta Turtle na qual o nosso ponteiro vai desenhar uma linha seguindo uma quantidade de passos, e esses passos serão guardados numa variável que irá incrementar em 1 a cada linha desenhada. Logo após desenhar a linha, o ponteiro deve girar 90 graus para a esquerda.

import turtle

turtle.shape('triangle')

linhas= int(input('Quantas linhas deseja? '))

contador = 0

while contador <= linhas:
    
    turtle.speed('fast')
    
    turtle.forward(1+contador)
    turtle.left(95)
    
    contador += 1