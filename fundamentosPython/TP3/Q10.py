#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado vermelho de 100 px de lado no centro da tela. O quadrado deve ser capaz de se movimentar vertical e horizontalmente através de teclas do computador. Pode ser ‘a’,’s’,’d’,’w’ ou as setas do teclado. (código e printscreen)

import pygame, sys
from pygame.locals import *

screen_width = 800
screen_height = 600

black = (0,0,0)
blue = (255,255,0)
red = (255,0,0)
square_position = [int(screen_width/2 - 50),int(screen_height/2 - 50)]
velocity = 5

square = pygame.draw.rect(SCREEN,red, (square_position[0], square_position[1], 100, 100))

def draw_background():
    SCREEN.fill(black)

def square_move(keys, square_pos):
    if keys[0] and square_pos[1]> 100:
        square_pos[1] -= velocity

    elif keys[1] and square_pos[1] <500:
        square_pos[1] += velocity

    elif keys[2] and square_pos[0] > 0:
        square_pos[0] -= velocity

    elif keys[3] and square_pos[0] < 700:
        square_pos[0] += velocity

    return square_pos

def draw_square(square_pos):
    SCREEN.blit(square)

def main():

    pygame.init()
    global SCREEN

    SCREEN = pygame.display.set_mode((screen_width,screen_height))


    #indices 0,1,2,3 sao respectivamente w,s,a,d
    keys =[False, False, False, False]
    done = False

    clock = pygame.time.Clock()

    while not done:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # Enquanto estiver pressionado, o coelho vai se mexer
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    keys[0] = True
                elif event.key == K_a:
                    keys[1] = True
                elif event.key == K_s:
                    keys[2] = True
                elif event.key == K_d:
                    keys[3] = True

            # No momento que parou de pressionar a tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    keys[0] = False
                elif event.key == pygame.K_a:
                    keys[1] = False
                elif event.key == pygame.K_s:
                    keys[2] = False
                elif event.key == pygame.K_d:
                    keys[3] = False


        draw_background()
        square_move(keys,square_position)
        draw_square(square_position)
        pygame.display.update()

        clock.tick(60)
    pygame.display.quit()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()