import pygame

pygame.init() #metodo necessario para começar o pygame

largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela,altura_tela))

amarelo = (255,255,0)
vermelho = (255,0,0)

#desenha um retangulo não preenchido com linha amarela

pygame.draw.rect(tela,amarelo,(10,10,200,100),3)

#desenha um retangulo todo preenchido de vermelho

pygame.draw.rect(tela,vermelho,(400,300,50,50))


terminou = False

while not terminou:

    #Atualia o desenho na tela
    pygame.display.update()

    #checar os eventos de mouse daqui

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

pygame.display.quit()
pygame.quit() #metodo necessario para terminar o pygame