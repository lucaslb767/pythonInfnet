import turtle #Importa a biblioteca Turtle

def geraPontos(i):#Essa função cria quadrados utilizando pontos no mapa cartesiano. O primeiro par representa o lado inferior, direito, superior e esquerdo.
   """ Gera pontos para quadrados de qualquer tamanho """
   return [(i, 0), (i, i), (0, i), (0, 0)] 

def desenhaPoligono(inicio, pontos, corLinha="black", corRecheio="white"): #definição da função desenhaPoligono. Esta aceita os parametros inicio,pontos, corLinha e
                                                                                                                                                        #corRecheio   
   turtle.pencolor(corLinha)  #o metodo .pencolor permite trocar a cor da linha. A cor será aquela que for usada como parametro corRecheio                                                                                                                          
   turtle.fillcolor(corRecheio) #o metodo .fillcolor muda a cor do da turtle que realiza o desenho. Ela mudará para a cor que o parametro corRecheio estiver.

   turtle.penup()#o método .penup é utilizado para parar de desenhar e poder mover a turtle sem deixar rastros

   turtle.goto(inicio)#utilizando o metodo .goto podemos mandar a turtle se locomover para um ponto especifico do mapa cartesiano

   turtle.pendown() #o metodo .pendown é o oposto do penup. Utilizado para voltar a deixar rastros e assim desenhar.
   turtle.begin_fill()

   x, y = inicio

   for ponto in pontos:  
       dx, dy = ponto
       turtle.goto(x + dx, y + dy)
   turtle.goto(inicio)  

   turtle.end_fill()
   turtle.penup()


def teste():
   # Primeiro quadrado
   quadrado = [(50, 0), (50, 50), (0, 50), (0, 0)]
   desenhaPoligono((200, 200), quadrado)

   # Segundo quadrado
   quadrado_maior = geraPontos(100)
   desenhaPoligono((-200, 200), quadrado_maior, corLinha="green")

   # Triangulo
   triangulo = [(200, 0), (100, 100), (0, 0)]
   desenhaPoligono((100, -100), triangulo, corLinha="green")


def main():
   teste()
   turtle.done()

main()