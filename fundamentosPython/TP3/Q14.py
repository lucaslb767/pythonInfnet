#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado de tamanho 50 no centro da tela. Quando o usuário clicar em alguma área da janela, o quadrado deve se mover para a posição clicada. (código e printscreen)

import pygame



SCREEN_WIDTH = 500
SCREEN_HEIGHT= 500

width = 50
height= 50

X = SCREEN_WIDTH//2 - width//2
Y = SCREEN_HEIGHT//2 - height//2
RED = (255,0,0)
BLACK = (0,0,0)
pygame.init()



win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Q14')



vel = 5

run = True
while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            X = mouseX - width//2
            Y = mouseY - height//2

    win.fill(BLACK)
    pygame.draw.rect(win,RED,(X, Y,width,height ) )

    pygame.display.update()

pygame.display.quit()

pygame.quit()

