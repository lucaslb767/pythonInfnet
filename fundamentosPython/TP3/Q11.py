import pygame



SCREEN_WIDTH = 500
SCREEN_HEIGHT= 500
RADIUS = 100

BLUE = (0,0,255)
pygame.init()


win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Q11')



vel = 5

run = True
while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.circle(win,BLUE,(SCREEN_WIDTH//2 , SCREEN_HEIGHT//2 ), RADIUS )
    pygame.display.update()

pygame.display.quit()

pygame.quit()