import turtle

def quadrado():
    turtle.speed('fastest')
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)

def triangulo():
    
    angulo = 120
    
    turtle.speed('fastest')
    turtle.forward(100)
    turtle.left(angulo)
    turtle.forward(100)
    turtle.left(angulo)
    turtle.forward(100)
    
def circulo():
    turtle.circle(50)
    

turtle.listen()

turtle.onkey(quadrado,"q")
turtle.onkey(triangulo,"t")
turtle.onkey(circulo,"c")
