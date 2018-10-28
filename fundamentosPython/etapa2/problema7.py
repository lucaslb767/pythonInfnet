#Escreva um programa em Python que armazene em uma tupla o nome em inglês de distintas cores. Utilize essa tupla para trocar a cor da tartaruga como a imagem

import turtle
turtle.shape('turtle')
turtle.bgcolor('black')
cores = ('red','yellow','orange','green','blue','purple')



retas = int(input('Quantas retas deseja que tenha a imagem? '))


for i in range(0,retas+1):
    turtle.forward(i+1)
    turtle.left(61)
    turtle.speed('fastest')
    
    turtle.color(cores[i%6])
    
        



    