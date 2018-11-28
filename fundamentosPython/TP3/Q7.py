#Escreva um programa em Python que realiza operações de inclusão e remoção em listas. Seu programa deve perguntar ao usuário qual operação deseja fazer: (código)

list = ['a', '2', 'True']


input_usuario = str(input('\nO que deseja?\nDigite "a": Mostrar lista \n"b": Adicionar item a lista \n"c": remover elemento \n"d": Apagar todos os elementos da lista \n"sair": sair do programa'))


while input_usuario != 'sair':

    if input_usuario == 'a':
        #a) Mostrar lista;
        print(list)
        input_usuario = str(input('\nO que deseja?\nDigite "a": Mostrar lista \n"b": Adicionar item a lista \n"c": remover elemento \n"d": Apagar todos os elementos da lista \n"sair": sair do programa'))

    elif input_usuario == 'b':
        #b) incluir elemento
        elemento = str(input('Qual novo elemento gostaria de acrescentar? '))
        list.append(elemento)
        print('Elemento adicionado com sucesso:', list)
        input_usuario = str(input(
            '\nO que deseja?\nDigite "a": Mostrar lista \n"b": Adicionar item a lista \n"c": remover elemento \n"d": Apagar todos os elementos da lista \n"sair": sair do programa'))

    elif input_usuario == 'c':
        #c) Remover elemento
        elemento = str(input('Qual elemento gostaria de remover? '))
        list.remove(elemento)
        print("Elemento removido com sucesso", list)
        input_usuario = str(input(
            '\nO que deseja?\nDigite "a": Mostrar lista \n"b": Adicionar item a lista \n"c": remover elemento \n"d": Apagar todos os elementos da lista \n"sair": sair do programa'))

    elif input_usuario == 'd':
        #d) Apagar todos os elementos da lista
        list =[]
        print('Operação concluída')
        print(list)
        input_usuario = str(input(
            '\nO que deseja?\nDigite "a": Mostrar lista \n"b": Adicionar item a lista \n"c": remover elemento \n"d": Apagar todos os elementos da lista \n"sair": sair do programa'))

    else:
        input_usuario = str(input(
            '\nO que deseja?\nDigite "a": Mostrar lista \n"b": Adicionar item a lista \n"c": remover elemento \n"d": Apagar todos os elementos da lista \n"sair": sair do programa'))


