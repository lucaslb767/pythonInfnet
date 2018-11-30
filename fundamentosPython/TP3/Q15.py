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

pygame.display.set_caption('Q15')



vel = 5

run = True
while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    win.fill(BLACK)

    pygame.draw.polygon(win, RED, [(40, 40), (60, 40), (65, 50), (50, 60),(35,50)])

    pygame.draw.polygon(win,RED, [(40,40),(60,40),(50, 20)])
    pygame.draw.polygon(win, RED, [(60, 40), (65, 50), (80, 45)])
    pygame.draw.polygon(win, RED, [(65, 50), (50, 60), (62, 70)])
    pygame.draw.polygon(win, RED, [(50, 60), (35, 50), (32, 70)])
    pygame.draw.polygon(win, RED, [(35, 50), (40, 40), (20, 45)])


    pygame.display.update()

pygame.display.quit()

pygame.quit()