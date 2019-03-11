'''
Crie um programa cliente que:
conecte-se a um servidor via UDP de mesmo IP e porta 9991.
Peça ao servidor que envie a quantidade total e disponível de armazenamento do disco principal.
Receba e exiba a informação.
'''

import socket
import psutil

HOST = socket.gethostname() # Endereco IP do Servidor
PORT = 9991                 # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Esperando receber na porta', PORT, '...')
(msg, cliente) = udp.recvfrom(2048)

path = 'C:'
total_disk = psutil.disk_usage(path).total
free_disk = psutil.disk_usage(path).free
msg_to_client = 'A quantidade total de armazenamento do disco principal eh de {} bytes. A quantidade disponivel eh de {} bytes'.format(total_disk,free_disk)
print(cliente, msg.decode('ascii'))

udp.sendto(msg_to_client.encode('ascii'),cliente)
udp.close()
input('Pressione qualquer tecla para sair...')
