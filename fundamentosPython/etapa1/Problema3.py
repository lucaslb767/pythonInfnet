nota = float(input('Entre com uma nota entre 0 e 10: '))

while nota<0 or nota>10 :
    nota= float(input('Nota inválida. Dê uma nota entre 0 e 10.'))
    
print('A nota dada é', nota )
