import pygame
import psutil

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
#iniciando a janela principal

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Uso de memória")
pygame.display.init()

pygame.font.init()
font = pygame.font.Font(None, 32)


#mostra uso de CPU

def mostra_uso_cpu():
    capacity = psutil.cpu_percent(interval=0)
    larg = screen_width - 2*20
    screen.fill(black)
    pygame.draw.rect(screen, blue, (20,110, larg, 130))
    larg = larg*capacity/100
    pygame.draw.rect(screen, red,(20,110, larg, 130))
    text = font.render("Uso  de CPU: ",1, white)
    screen.blit(text,(20,80))
#Cria relógio

clock = pygame.time.Clock()

cont = 60

terminou = False

while not terminou:
    #checar os eventos do mouse aqui
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    if cont == 60:

        mostra_uso_cpu()
        cont = 0

    #atualiza o desenho na tela
    pygame.display.update()

    #60 frames por segundo

    clock.tick(60)
    cont = cont +1

#finaliza a janela
pygame.display.quit()