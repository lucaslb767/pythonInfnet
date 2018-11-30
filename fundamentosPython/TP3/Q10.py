import pygame



SCREEN_WIDTH = 500
SCREEN_HEIGHT= 500

width = 100
height= 100

X = SCREEN_WIDTH//2 - width//2
Y = SCREEN_HEIGHT//2 - height//2
RED = (255,0,0)
BLACK = (0,0,0)
pygame.init()



win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Q10')



vel = 5

run = True
while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        Y -= vel
    if keys[pygame.K_s]:
        Y += vel
    if keys[pygame.K_a]:
        X -= vel
    if keys[pygame.K_d]:
        X += vel

    win.fill(BLACK)
    pygame.draw.rect(win,RED,(X, Y,width,height ) )
    pygame.display.update()

pygame.display.quit()

pygame.quit()