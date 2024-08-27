import socket

#Temos que instanciar o objeto e os parametros

host = "127.0.0.1"
port = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"teste", (host, port))
data, addr = client.recvfrom(4096)
print(data)
client.close()
