import turtle

numero_quadrados = int(input('Deseja quantos quadrados? '))
tamanho_retas = 100
turtle.speed('fastest')
angulo_quadrado = 90

for i in range(0,numero_quadrados):
    turtle.forward(tamanho_retas)
    turtle.left(angulo_quadrado)
    turtle.forward(tamanho_retas)
    turtle.left(angulo_quadrado)
    turtle.forward(tamanho_retas)
    turtle.left(angulo_quadrado)
    turtle.forward(tamanho_retas)
    turtle.left(angulo_quadrado)
    turtle.forward(tamanho_retas)
    
    