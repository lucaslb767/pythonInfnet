import turtle

turtle.title("Nossa primeira função!")

turtle.shape('turtle')

def quadrado():
    for count in range(4):
        turtle.forward(100)
        turtle.left(90)
quadrado()