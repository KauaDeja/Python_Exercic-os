#Este código tem o intuito de criar uma conexão de cliente TCP de forma simples e usual. 


import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Instanciamos o objeto socket e chamamos seus parametros, IPV4 e TCP.

client.connect((target_host,target_port)) #Conecta com o servidor

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") #Envia dados

response = client.recv(4096) #Recebe esses dados, decodifica e fecha a conexao.
print(response.decode())
client.close()
print(f"Conexão com o servidor {target_host} encerrada.")