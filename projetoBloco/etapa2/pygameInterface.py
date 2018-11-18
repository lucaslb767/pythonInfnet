import pygame

#iniciando a janela principal

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Uso de memória")
pygame.display.init()

#Cria relógio

clock = pygame.time.Clock()

terminou = False

while not terminou:
    #checar os eventos do mouse aqui
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    #atualiza o desenho na tela
    pygame.display.update()

    #60 frames por segundo

    clock.tick(60)

#finaliza a janela
pygame.display.quit()