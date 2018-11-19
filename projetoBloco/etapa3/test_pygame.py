import pygame
import psutil
import cpuinfo

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

#iniciando a janela principal

screen_width = 800
scree_height = 600
screen = pygame.display.set_mode((screen_width,scree_height))
pygame.display.set_caption('Informações de CPU')
pygame.display.init()

#Superficie para mostrar as informações:

s1 = pygame.surface.Surface((screen_width,scree_height))

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
        cont = 0

    #atualiza o desenho na tela
    pygame.display.update()

    # 60 frames por segundo

    clock.tick(60)
    cont  += 1

#Finaliza a janela
pygame.display.quit()