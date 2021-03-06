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

#mostra uso do Disco

def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = screen_width - 2*20
    screen.fill(black)
    pygame.draw.rect(screen,blue,(20,50,larg,70))
    larg = larg*disco.percent/100
    pygame.draw.rect(screen,red,(20,50,larg,70))
    total = round(disco.total/(1024*1024*1024),2)
    texto_barra = "Uso de Disco: (Total: "+str(total)+ "GB: "
    text = font.render(texto_barra,1,white)
    screen.blit(text, (20,10))
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
        mostra_uso_disco()
        cont = 0

    #atualiza o desenho na tela
    pygame.display.update()

    #60 frames por segundo

    clock.tick(60)
    cont = cont +1

#finaliza a janela
pygame.display.quit()