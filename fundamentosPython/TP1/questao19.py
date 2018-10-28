
import turtle

def quadrado_continuo(n):
    
    turtle.speed('fastest')
    turtle.pencolor('red')
    turtle.shape('turtle')
    turtle.fillcolor('red')
    
    if n <= 0 :
        print('é necessário que n seja positivo')
    else:
        
        for i in range(0,n+1):
            turtle.forward(i)
            turtle.left(90)
        

n = int(input('Quantos lados deseja? '))

quadrado_continuo(n)
            