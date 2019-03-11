import socket

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 9991  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = input("Digite qualquer comando para receber dados sobre armazenamento:\n")
udp.sendto(msg.encode('ascii'), dest)

(mensagem_servidor, servidor)=udp.recvfrom(2048)
print(servidor, mensagem_servidor.decode('ascii'))

udp.close()