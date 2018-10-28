#20. Baseando no código criado na questão anterior, crie uma função na qual dado um N obtido através do usuário, sua tartaruga gire 90 + N graus.


import turtle

def quadrado_continuo(retas, angulo):
    
    turtle.speed('fastest')
    turtle.pencolor('red')
    turtle.shape('turtle')
    turtle.fillcolor('red')
    
    if retas <= 0 :
        print('é necessário que o número de retas seja positivo')
    else:
        
        for i in range(0,n+1):
            turtle.forward(i)
            turtle.left(90 + angulo)
        

n = int(input('Quantos lados deseja? '))

angulo = int(input('Qual a quantidade de angulos que deseja alterar? '))

quadrado_continuo(n, angulo)
            
