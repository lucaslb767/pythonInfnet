import turtle

def cima():
    turtle.setheading(90)
    turtle.forward(50)
    
def direita():
    turtle.setheading(0)
    turtle.forward(50)
    
def baixo():
    turtle.setheading(270)
    turtle.forward(50)
    
def esquerda():
    turtle.setheading(180)
    turtle.forward(50)
    

turtle.listen()

turtle.onkey(cima,"Up")
turtle.onkey(direita,"Right")
turtle.onkey(baixo,"Down")
turtle.onkey(esquerda,"Left")