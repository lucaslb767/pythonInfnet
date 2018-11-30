import pygame



SCREEN_WIDTH = 500
SCREEN_HEIGHT= 500


RADIUS= 100

X = SCREEN_WIDTH//2
Y = SCREEN_HEIGHT//2
BLUE = (0,0,255)
BLACK = (0,0,0)
pygame.init()



win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Q11')



vel = 20

run = True
while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    X += vel

    #controla colisao

    if X > SCREEN_WIDTH - 50 :
        X = 0
    if X < 0 :
        X = SCREEN_WIDTH - 50

    win.fill(BLACK)
    pygame.draw.circle(win,BLUE,(X, Y ), RADIUS )
    pygame.display.update()

pygame.display.quit()

pygame.quit()