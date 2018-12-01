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
score = 0
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

def artificial_inteligency(ball, ballDirX, bar2):
    #movimentar a paleta quando a bola vem em direção da paleta
    if ballDirX == 1:
        if bar2.centery < ball.centery:
            bar2.y += 1
        else:
            bar2.y -= 1

    return bar2

#Verifica a colisão da bola com a paleta 1 e 2
def ball_collision(ball, bar1, bar2, ballDirX):
    if ballDirX == -1 and bar1.right == ball.left and bar1.top < ball.top and bar1.bottom > ball.bottom:
        return -1
    elif ballDirX == 1 and bar2.left == ball.right and bar2.top < ball.top and bar2.bottom > ball.bottom:
        return -1

    else: return 1

#verifica se um jogador fez ponto e retorna o novo valor do placar
def score_check(bar1, ball, score, ballDirX):
    #zera a contagem se a bola acerta a borda do jogador
    if ball.left == LINE_WIDTH:
        return 0
    elif ball.right == SCREEN_WIDTH - LINE_WIDTH:
        score += 10
        return score
    elif ballDirX == 1 and bar1.right == ball.left and bar1.top < ball.top and bar1.bottom > ball.bottom:
        score += 1
        return score

    else: return score

def draw_score(score):
    resultSurf = BASICFONT.render('Score = %s' %(score), True, WHITE)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (SCREEN_WIDTH - 150, 25)
    DISPLAYSURF.blit(resultSurf, resultRect)

def main():

    pygame.init()
    global DISPLAYSURF

    ##Informação da fonte
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('PONG')

    #iniciando as variáveis nas posições iniciais
    #Estas variáveis serão alteradas ao longo da execução
    bolaX = SCREEN_WIDTH//2 - LINE_WIDTH//2
    bolaY = SCREEN_HEIGHT//2 - LINE_WIDTH//2


    playerOne_position =(SCREEN_HEIGHT-BAR_HEIGHT)//2
    playerTwo_position = (SCREEN_HEIGHT - BAR_HEIGHT)//2

    score = int(0)

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
        ballDirX = ballDirX * ball_collision(ball, bar1, bar2, ballDirX)
        bar2 = artificial_inteligency(ball, ballDirX, bar2)
        score = score_check(bar1, ball, score , ballDirX)
        draw_score(score)
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