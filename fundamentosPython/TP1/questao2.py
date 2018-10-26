#2. Faça uma função em Python que receba do usuário a idade de uma pessoa em anos, meses e dias e retorne essa idade expressa em dias. Considere que todos os anos têm 365 dias.

import time

data_atual = time.strftime("%d/%m/%Y")
data = data_atual.split('/')
dia_atual = int(data[0])
mes_atual=int(data[1])
ano_atual=int(data[2])
total_dias_atual = dia_atual + (mes_atual*30) + (ano_atual*365)

nascimento_dia = int(input('Qual dia você nasceu? '))
nascimento_mes = int(input('Qual mês você nasceu? '))
nascimento_ano = int(input('Qual ano você nasceu?(digitar ano com 4 digitos) '))
nascimento_total = nascimento_dia + (nascimento_mes*30)+(nascimento_ano*365)

idade_total = total_dias_atual - nascimento_total
idade_anos = int(idade_total/365)
idade_meses = int((idade_total - (idade_anos*365))/30)
idade_dias = int(idade_total-(idade_anos*365) - (idade_meses*30))

print('Você tem', idade_anos,', ',idade_meses,'meses e', idade_dias,'dias')





