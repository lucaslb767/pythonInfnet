#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro no centro da tela. (código e printscreen)

import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

blue = (0,0,255)

pygame.draw.circle(screen,blue, (int(screen_width/2),int(screen_height/2)), 100)

done = False

while not done:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.display.quit()

pygame.quit()
