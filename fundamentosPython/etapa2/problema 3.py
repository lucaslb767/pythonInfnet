#Escreva um programa em Python que leia um número e exiba o dia correspondente da semana (1 - Domingo, 2 - Segunda, etc.). Se digitar outro valor, indicar "Valor Inválido".

dia = input('Qual é o dia da semana?(digite o número que o represente) ')

if dia == "1":
    print('Domingo')

elif dia =="2":
    print('Segunda-Feira')

elif dia =="3":
    print('Terça-Feira')

elif dia =="4":
    print('Quarta-Feira')

elif dia =="5":
    print('Quinta-Feira')

elif dia =="6":
    print('Sexta-Feira')

elif dia =="7":
    print('Domingo')
    
else:
    print('Valor inválido')
