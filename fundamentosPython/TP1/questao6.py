import turtle

angulo = 0
acrescimo=15
tamanho_raio = 200
turtle.speed('fastest')


for i in range(0,int(360/15)):
    turtle.setheading(angulo)
    turtle.forward(tamanho_raio)
    turtle.write(angulo)
    turtle.backward(tamanho_raio)
    
    angulo = angulo + acrescimo