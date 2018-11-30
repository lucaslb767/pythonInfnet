import pygame



SCREEN_WIDTH = 500
SCREEN_HEIGHT= 500


RADIUS= 100

X = SCREEN_WIDTH//2
Y = SCREEN_HEIGHT//2
YELLOW = (255,255,0)
BLACK = (0,0,0)
pygame.init()


direction = ''
win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Q12')



vel = 20

run = True
while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
       direction = 'up'

    if keys[pygame.K_s]:
        direction = 'down'

    if keys[pygame.K_a]:
        direction = 'left'

    if keys[pygame.K_d]:
        direction = 'right'

    #faz o circulo se mover constantemente
    if direction == 'up':
        Y -= vel
    if direction == 'down':
        Y += vel
    if direction == 'left':
        X -= vel
    if direction == 'right':
        X += vel



    #controla colisao

    if X > SCREEN_WIDTH - 50 :
        X = 0

    if X < 0 :
        X = SCREEN_WIDTH - 50

    if Y > SCREEN_HEIGHT - 50:
        Y = 0

    if Y < 0:
        Y = SCREEN_HEIGHT - 50

    win.fill(BLACK)
    pygame.draw.circle(win,YELLOW,(X, Y ), RADIUS )
    pygame.display.update()

pygame.display.quit()

pygame.quit()