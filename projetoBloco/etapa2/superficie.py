import pygame
import psutil

#iniciando a tela principal

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Exemplo Surface')
pygame.display.init()

blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)
white=(255,255,255)

s1 = pygame.surface.Surface((screen_width,screen_height/3))
s2 = pygame.surface.Surface((screen_width,screen_height/3))
s3 = pygame.surface.Surface((screen_width,screen_height/3))

bar_width = screen_width - 2*20

pygame.draw.rect(s1, blue,(20,50, bar_width, 70 ))
screen.blit(s1,(0,0))
pygame.draw.rect(s2, blue,(20,50, bar_width, 70 ))
screen.blit(s2,(0,screen_height/3))
pygame.draw.rect(s3, blue,(20,50, bar_width, 70 ))
screen.blit(s3,(0,2*screen_height/3))

#cria relogio

clock = pygame.time.Clock()

terminou = False

while not terminou:

    #checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    #Atualia o desenho na tela
    pygame.display.update()

    #60frames por segundo
    clock.tick(60)

#finaliza a janela
pygame.display.quit()
