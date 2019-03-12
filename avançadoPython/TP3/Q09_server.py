'''
Associado à questão anterior, crie um programa servidor que:
Espere conexões UDP de processos na porta 9991.
Aguarde indefinidamente conexão de clientes.
Sirva cada cliente com a informação da quantidade total e disponível de armazenamento do disco principal (diretório corrente que o processo servidor está executando).
'''

import socket
import psutil

HOST = socket.gethostname() # Endereco IP do Servidor
PORT = 9991                 # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Esperando receber na porta', PORT, '...')

while True:
    (msg, cliente) = udp.recvfrom(2048)

    path = 'C:'
    total_disk = psutil.disk_usage(path).total
    free_disk = psutil.disk_usage(path).free
    msg_to_client = 'A quantidade total de armazenamento do disco principal eh de {} bytes. A quantidade disponivel eh de {} bytes'.format(total_disk,free_disk)
    print(cliente, msg.decode('ascii'))

    udp.sendto(msg_to_client.encode('ascii'),cliente)

    saida = str(input('digite sair para terminar...')).lower()
    if saida == 'sair':


        break

udp.close()