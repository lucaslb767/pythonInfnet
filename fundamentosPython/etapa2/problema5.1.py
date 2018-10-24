#Calcule fatorial de um número

fatorial = int(input('Qual valor gostaria de saber o fatorial? '))


cont = fatorial
resultado = fatorial

if fatorial > 1:
    
    while cont > 1:
        
        cont -= 1
    
        resultado = resultado*(fatorial - (fatorial-cont))
    
        
        
    print('O valor de',fatorial,'! é ', resultado)
    
elif fatorial == 1:
    print('Fatorial de 1 é 1')
    
else:
    print('Para fazer fatorial, é necessário números positivos')
    
