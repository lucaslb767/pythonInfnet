import pygame
import psutil
import cpuinfo

def mostra_uso_cpu(s, l_cpu_percent):
    s.fill(gray)
    num_cpu = len(l_cpu_percent)
    x=y=10
    desl = 10
    alt = s.get_height() - 2*y
    larg = (s.get_width() - 2*x - (num_cpu+1)*desl)/num_cpu
    d = x +desl

    for i in l_cpu_percent:
        pygame.draw.rect(s,red, (d,y,larg,alt))
        pygame.draw.rect(s,blue,(d,y,larg,(1-i/100)*alt))
        d = d + larg + desl

    # parte mais abaixo da tela
    screen.blit(s, (0, screen_height / 5))

def mostra_texto(sN, nome, chave , pos_y):
    text = font.render(nome, True, black)
    sN.blit(text, (10, pos_y))

    if chave == 'freq':
        s = str(round(psutil.cpu_freq().current,2))

    elif chave == 'nucleos':
        s = str(psutil.cpu_count())
        s = s + '(' + str(psutil.cpu_count(logical=False)) + ')'

    else:
        s = str(info_cpu[chave])

    text = font.render(s, True, gray)
    sN.blit(text, (160, pos_y))


def mostra_info_cpu():
    s1.fill(white)
    mostra_texto(s1, 'Nome:', 'brand',10)
    mostra_texto(s1, 'Arquitetura:', 'arch', 30)
    mostra_texto(s1, 'Palavra (bits)', 'bits', 50)
    mostra_texto(s1, 'Frequência (MHz)', 'freq', 70)
    mostra_texto(s1, 'Núcleos (físicos):', 'nucleos', 90)
    screen.blit(s1,(0,0))

#obtém informações da CPU

info_cpu = cpuinfo.get_cpu_info()

#Cores

black = (0,0,0)
white = (255,255,255)
gray = (100,100,100)
red = (255,0,0)
blue = (0,0,255)

#iniciando a janela principal

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Informações de CPU')
pygame.display.init()

#Superficie para mostrar as informações:

s1 = pygame.surface.Surface((screen_width,screen_height/4))
s2 = pygame.surface.Surface((screen_width,3*screen_height/4))

#Para usar na fonte
pygame.font.init()
font = pygame.font.Font(None, 24)

#Cria relógio
clock = pygame.time.Clock()

#contador de tempo

cont = 60

terminou = False

# Repetição para capturar eventos e atualizar tela

while not terminou:
    #checar os eventos do mouse aqui
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    #fazer a atualiação a cada segundo
    if cont ==60:
        mostra_info_cpu()
        mostra_uso_cpu(s2,psutil.cpu_percent(percpu=True))
        cont = 0

    #atualiza o desenho na tela
    pygame.display.update()

    # 60 frames por segundo

    clock.tick(60)
    cont  += 1

#Finaliza a janela
pygame.display.quit()