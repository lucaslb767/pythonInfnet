#Escreva um programa em Python que leia da entrada cada nome em inglês de cores e os armazene em uma tupla. O término das entradas ocorre quando o usuário digitar “sair”. Faça com que a tartaruga gere um desenho similar ao problema 7, considerando um polígono possuindo a quantidade de lados referente a quantidade de cores adicionadas.

import turtle


cores = ()

cores_digitadas = str(input('Digite a cor desejada(em ingles) ou sair para terminar o processo '))
    

while cores_digitadas != "sair":
    
    cores += (cores_digitadas,)
    
    cores_digitadas = str(input('Digite a cor desejada(em ingles) ou sair para terminar o processo '))
    

retas = int(input('Quantas retas deseja? '))
tamanho_cores = len(cores)

for i in range(0, retas+1):
    
    turtle.forward(1+i)
    turtle.left((360/tamanho_cores)+1)
    turtle.color(cores[i%tamanho_cores])
    