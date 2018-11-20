import pygame
import psutil
import cpuinfo
import sys

from pygame.locals import *
import os

#TODO refatorar tudo


#iniciando a tela principal

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('lucas_barrozo_TP3')
pygame.display.init()

pygame.font.init()
font = pygame.font.Font(None, 24)

blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)
white=(255,255,255)
gray = (100,100,100)
green= (100,255,100)

def main_screen():

    s1 = pygame.surface.Surface((screen_width,screen_height/4))
    s2 = pygame.surface.Surface((screen_width,screen_height/4))
    s3 = pygame.surface.Surface((screen_width,screen_height/4))
    s4 = pygame.surface.Surface((screen_width,screen_height/4))


    #Mostra uso de memória

    def mostra_uso_memoria():
        mem = psutil.virtual_memory()
        larg = screen_width - 2*20
        s1.fill(black)
        pygame.draw.rect(s1, blue,(20,50,larg,70))
        screen.blit(s1, (0, 0))

        larg2 = larg*mem.percent/100
        pygame.draw.rect(s1,red,(20,50,larg2,70))
        screen.blit(s1, (0, 0))
        total = round(mem.total/(1024*1024*1024),2)

        texto_barra = "Uso de Memória (Total: " + str(total) + "GB): "
        text = font.render(texto_barra,1, white)
        screen.blit(text, (20,10))

    #mostra uso de CPU

    def mostra_uso_cpu():
        capacity = psutil.cpu_percent(interval=0)
        larg = screen_width - 2*20

        pygame.draw.rect(s2, blue, (20,50, larg, 70))
        screen.blit(s2, (0,screen_height/4))

        larg = larg*capacity/100
        pygame.draw.rect(s2, red,(20,50, larg, 70))
        screen.blit(s2, (0, screen_height / 4))

        text = font.render("Uso  de CPU: ",1, white)
        screen.blit(text,(20,screen_height/4))

    #mostra uso de disco

    def mostra_uso_disco():
        disco = psutil.disk_usage('.')
        larg = screen_width - 2*20

        pygame.draw.rect(s3,blue,(20,50,larg,70))
        screen.blit(s3, (0, screen_height / 2))

        larg = larg*disco.percent/100
        pygame.draw.rect(s3,red,(20,50,larg,70))
        screen.blit(s3, (0, screen_height / 2))

        total = round(disco.total/(1024*1024*1024),2)
        texto_barra = "Uso de Disco: (Total: "+str(total)+ "GB: "
        text = font.render(texto_barra,1,white)
        screen.blit(text, (20,screen_height/2))

    #mostra ip da maquina

    def mostra_ip():
        dic_interfaces = psutil.net_if_addrs()
        texto_barra = "O seu ip é: " +str(dic_interfaces['Wi-Fi'][0].address)

        text = font.render(texto_barra,1,white)
        screen.blit(text, (20,3*screen_height/4))

    def resumo():
        mostra_uso_cpu()
        mostra_uso_memoria()
        mostra_ip()
        mostra_uso_disco()

    def cpu_screen():
        s1 = pygame.surface.Surface((screen_width, screen_height / 4))
        s2 = pygame.surface.Surface((screen_width, 3 * screen_height / 4))

        # obtém informações da CPU

        info_cpu = cpuinfo.get_cpu_info()

        def mostra_uso_cpu(s, l_cpu_percent):
            s.fill(black)
            num_cpu = len(l_cpu_percent)
            x = y = 10
            desl = 10
            alt = s.get_height() - 2 * y
            larg = (s.get_width() - 2 * x - (num_cpu + 1) * desl) / num_cpu
            d = x + desl

            for i in l_cpu_percent:
                pygame.draw.rect(s, green, (d, y, larg, alt))
                pygame.draw.rect(s, gray, (d, y, larg, (1 - i / 100) * alt))
                d = d + larg + desl

            # parte mais abaixo da tela
            screen.blit(s, (0, screen_height / 5))

        def mostra_texto(sN, nome, chave, pos_y):
            text = font.render(nome, True, black)
            sN.blit(text, (10, pos_y))

            if chave == 'freq':
                s = str(round(psutil.cpu_freq().current, 2))

            elif chave == 'nucleos':
                s = str(psutil.cpu_count())
                s = s + '(' + str(psutil.cpu_count(logical=False)) + ')'

            else:
                s = str(info_cpu[chave])

            text = font.render(s, True, gray)
            sN.blit(text, (160, pos_y))

        def mostra_info_cpu():
            s1.fill(white)
            mostra_texto(s1, 'Nome:', 'brand', 10 + 10)
            mostra_texto(s1, 'Arquitetura:', 'arch', 30 + 10)
            mostra_texto(s1, 'Palavra (bits)', 'bits', 50 + 10)
            mostra_texto(s1, 'Frequência (MHz)', 'freq', 70 + 10)
            mostra_texto(s1, 'Núcleos (físicos):', 'nucleos', 90 + 10)
            screen.blit(s1, (0, 0))

        def total_info():
            mostra_info_cpu()
            mostra_uso_cpu(s2, psutil.cpu_percent(percpu=True))

        # cria relogio

        clock = pygame.time.Clock()

        cont = 60

        terminou = False

        while not terminou:

            # checar os eventos do mouse aqui:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminou = True

            if event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    disk_screen()
                elif event.key == K_RIGHT:
                    memory_screen()
                elif event.key == K_SPACE:
                    main_screen()

            if cont == 60:
                total_info()

                cont = 0

            # Atualia o desenho na tela
            pygame.display.update()

            # 60frames por segundo
            clock.tick(60)

            cont += 1

        # finaliza a janela
        pygame.display.quit()

    def memory_screen():
        s1 = pygame.surface.Surface((screen_width, screen_height / 4))
        s2 = pygame.surface.Surface((screen_width, 3 * screen_height / 4))

        def mostra_texto(sN, nome, chave, pos_y):
            text = font.render(nome, True, black)
            sN.blit(text, (5, pos_y))

            s = ''
            if chave == 'total':
                s = str(round(psutil.virtual_memory().total / (1024 * 1024 * 1024), 2)) + 'GB'

            elif chave == 'available':
                s = str(round(psutil.virtual_memory().available / (1024 * 1024 * 1024), 2)) + 'GB'

            elif chave == 'used':
                s = str(round(psutil.virtual_memory().used / (1024 * 1024 * 1024), 2)) + 'GB'

            elif chave == 'free':
                s = str(round(psutil.virtual_memory().free / (1024 * 1024 * 1024), 2)) + 'GB'

            text = font.render(s, True, black)
            sN.blit(text, (250, pos_y))

        def mostra_info_memoria():
            s1.fill(white)
            mostra_texto(s1, 'Total:', 'total', 10 + 10)
            mostra_texto(s1, 'Memória disponível:', 'available', 30 + 10)
            mostra_texto(s1, 'Memória usada' + '( ' + str(psutil.virtual_memory().percent) + '% ):', 'used', 50 + 10)
            mostra_texto(s1, 'Memória disponível:', 'free', 70 + 10)

            screen.blit(s1, (0, 0))

        def mostra_uso_memoria():
            mem = psutil.virtual_memory()
            larg = screen_width - 2 * 20
            s2.fill(white)
            pygame.draw.rect(s2, gray, (20, 50, larg, 70))
            screen.blit(s2, (0, screen_width / 4))

            larg2 = larg * mem.percent / 100
            pygame.draw.rect(s2, green, (20, 50, larg2, 70))
            screen.blit(s2, (0, screen_height / 4))
            total = round(mem.total / (1024 * 1024 * 1024), 2)

            texto_barra = "Uso de Memória (Total: " + str(total) + "GB): "
            text = font.render(texto_barra, 1, black)
            screen.blit(text, (20, screen_height / 4))

        def total_memory():
            mostra_info_memoria()
            mostra_uso_memoria()

        # cria relogio

        clock = pygame.time.Clock()

        cont = 60

        terminou = False

        while not terminou:

            # checar os eventos do mouse aqui:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminou = True

            if event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    cpu_screen()
                elif event.key == K_RIGHT:
                    disk_screen()
                elif event.key == K_SPACE:
                    main_screen()
            if cont == 60:
                total_memory()

                cont = 0

            # Atualia o desenho na tela
            pygame.display.update()

            # 60frames por segundo
            clock.tick(60)

            cont += 1

        # finaliza a janela
        pygame.display.quit()

    def disk_screen():
        s1 = pygame.surface.Surface((screen_width, screen_height / 4))
        s2 = pygame.surface.Surface((screen_width, 3 * screen_height / 4))

        def mostra_texto(sN, nome, chave, pos_y):
            text = font.render(nome, True, black)
            sN.blit(text, (5, pos_y))

            s = ''
            if chave == 'total':
                s = str(round(psutil.disk_usage('.').total / (1024 * 1024 * 1024), 2)) + 'GB'

            elif chave == 'used':
                s = str(round(psutil.disk_usage('.').used / (1024 * 1024 * 1024), 2)) + 'GB'

            elif chave == 'free':
                s = str(round(psutil.disk_usage('.').free / (1024 * 1024 * 1024), 2)) + 'GB'

            text = font.render(s, True, black)
            sN.blit(text, (250, pos_y))

        def mostra_info_disco():
            s1.fill(white)
            mostra_texto(s1, 'Total:', 'total', 10 + 10)
            mostra_texto(s1, 'Espaço usado' + '( ' + str(psutil.disk_usage('.').percent) + '% ):', 'used', 50 + 10)
            mostra_texto(s1, 'Espaço disponível:', 'free', 70 + 10)

            screen.blit(s1, (0, 0))

        def mostra_uso_disco():
            disco = psutil.disk_usage('.')
            larg = screen_width - 2 * 20

            pygame.draw.rect(s2, gray, (20, 50, larg, 70))
            screen.blit(s2, (0, screen_height / 4))

            larg = larg * disco.percent / 100
            pygame.draw.rect(s2, green, (20, 50, larg, 70))
            screen.blit(s2, (0, screen_height / 4))

            total = round(disco.total / (1024 * 1024 * 1024), 2)
            texto_barra = "Uso de Disco: (Total: " + str(total) + "GB: "
            text = font.render(texto_barra, 1, white)
            screen.blit(text, (20, screen_height / 4))

        def disk_total():
            mostra_info_disco()
            mostra_uso_disco()

        # cria relogio

        clock = pygame.time.Clock()

        cont = 60

        terminou = False

        while not terminou:

            # checar os eventos do mouse aqui:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminou = True

            if event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    memory_screen()
                elif event.key == K_RIGHT:
                    cpu_screen()
                elif event.key == K_SPACE:
                    main_screen()

            if cont == 60:
                disk_total()

                cont = 0

            # Atualia o desenho na tela
            pygame.display.update()

            # 60frames por segundo
            clock.tick(60)

            cont += 1

        # finaliza a janela
        pygame.display.quit()
    # cria relogio

    clock = pygame.time.Clock()

    cont = 60

    terminou = False

    while not terminou:

        # checar os eventos do mouse aqui:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

        list_screen = [resumo(), ]

#TODO: melhorar a função atualizadora
        def atualizadora(list_screen):

            cont = 60

            contador = 0
            if event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    if contador == 0:
                        contador = len(list_screen)
                    else:
                        contador -= 1

                elif event.key == K_RIGHT:
                    if contador >= len(list_screen):
                        contador = 0
                    else:
                        contador += 1

                if cont == 60:
                    list_screen[contador]

                    cont = 0

        cont = cont

        # Atualia o desenho na tela
        pygame.display.update()

        # 60frames por segundo
        clock.tick(60)

        cont += 1

    # finaliza a janela
    pygame.display.quit()

main_screen()