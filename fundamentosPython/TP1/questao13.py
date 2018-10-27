import turtle


def quadrado(lado):
    
    turtle.speed('fastest')
    proporcao_quadrados_menores = 0.4
    distancia_quadrado_maior = .2
 
    turtle.forward(lado)
    turtle.left(90)
    turtle.forward(lado)
    turtle.left(90)
    turtle.forward(lado)
    turtle.left(90)
    turtle.forward(lado)
    turtle.left(90)
    
    while lado > 4:
        turtle.penup()
        turtle.forward(int(lado*distancia_quadrado_maior))
        turtle.left(90)
        turtle.forward(int(lado*distancia_quadrado_maior))
        turtle.right(90)
        turtle.pendown()
        
        lado = lado*proporcao_quadrados_menores
        
        turtle.forward(lado)
        turtle.left(90)
        turtle.forward(lado)
        turtle.left(90)
        turtle.forward(lado)
        turtle.left(90)
        turtle.forward(lado)
        turtle.left(90)
        

lado = int(input("Qual é o tamanho do lado?"))

quadrado(lado)
        