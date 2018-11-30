import pygame, sys
from pygame.locals import *

#CONSTANTES
#constantes para tamanho de tela

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

#será utilizada para velocidade do jogo

FPS = 200

#Valores para o desenho das paletas e do fundo
LINE_WIDTH = 10
BAR_HEIGHT = 50
BAR_PADDING = 20

#CORES
BLACK = (0,0,0)
WHITE = (255,255,255)

def arena_draw():
    DISPLAYSURF.fill(BLACK)

    #desenha a quadra

    pygame.draw.rect(DISPLAYSURF, WHITE,((0,0),(SCREEN_WIDTH,SCREEN_HEIGHT)), LINE_WIDTH*2)
    pygame.draw.line(DISPLAYSURF, WHITE, ((SCREEN_WIDTH // 2), 0), ((SCREEN_WIDTH // 2), SCREEN_HEIGHT),(LINE_WIDTH // 4))

def draw_bar(bar):

    #impede da paleta ir além da borda do fundo
    if bar.bottom > SCREEN_HEIGHT - LINE_WIDTH:
        bar.bottom = SCREEN_HEIGHT - LINE_WIDTH

    #impede da paleta ir além da borda do topo

    if bar.top < LINE_WIDTH:
        bar.top = LINE_WIDTH

    #desenha a paleta

    pygame.draw.rect(DISPLAYSURF,WHITE, bar)

def draw_ball(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)



def move_ball(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY

    return ball

#verifica se existe colisão com as bordas
#Retorna uma nova posição caso exista colisão

def colision_detection(ball, ballDirX, ballDirY):
    if ball.top == (LINE_WIDTH) or ball.bottom == (SCREEN_HEIGHT - LINE_WIDTH):
        ballDirY *= -1

    if ball.left == (LINE_WIDTH) or ball.right == (SCREEN_WIDTH - LINE_WIDTH):
        ballDirX *= -1

    return ballDirX,ballDirY



def main():

    pygame.init()
    global DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('PONG')

    #iniciando as variáveis nas posições iniciais
    #Estas variáveis serão alteradas ao longo da execução
    bolaX = SCREEN_WIDTH//2 - LINE_WIDTH//2
    bolaY = SCREEN_HEIGHT//2 - LINE_WIDTH//2

    playerOne_position =(SCREEN_HEIGHT-BAR_HEIGHT)//2
    playerTwo_position = (SCREEN_HEIGHT - BAR_HEIGHT)//2

    #criando rentagulos para a bola e paletas
    bar1 = pygame.Rect(BAR_PADDING, playerOne_position,LINE_WIDTH, BAR_HEIGHT)
    bar2 = pygame.Rect(SCREEN_WIDTH - BAR_PADDING - LINE_WIDTH,playerTwo_position, LINE_WIDTH, BAR_HEIGHT)
    ball = pygame.Rect(bolaX,bolaY,LINE_WIDTH,LINE_WIDTH)

    #altera posição da bola
    ballDirX = -1
    ballDirY = -1

    #desenhando as posições iniciais da arena
    arena_draw()
    draw_bar(bar1)
    draw_bar(bar2)
    draw_ball(ball)

    done = False

    while not done:


        #checa os eventos do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            #move o jogador
            if event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
                bar1.y = mouseY

        arena_draw()
        draw_bar(bar1)
        draw_bar(bar2)
        draw_ball(ball)

        ball = move_ball(ball, ballDirX, ballDirY)
        ballDirX, ballDirY = colision_detection(ball, ballDirX, ballDirY)
        # atualiza o desenho na tela

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    #finaliza o display
    pygame.display.quit()

    #finaliza o pygame

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()