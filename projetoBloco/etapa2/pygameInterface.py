import pygame
import psutil

#iniciando a janela principal

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Uso de memória")
pygame.display.init()

pygame.font.init()
font = pygame.font.Font(None, 32)

#Mostra uso de memória

def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = screen_width - 2*20
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,0,255),(20,50,larg,70))

    larg2 = larg*mem.percent/100
    pygame.draw.rect(screen,(255,0,0),(20,50,larg2,70))
    total = round(mem.total/(1024*1024*1024),2)

    texto_barra = "Uso de Memória (Total: " + str(total) + "GB): "
    text = font.render(texto_barra,1, (255,255,255))
    screen.blit(text, (20,10))

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