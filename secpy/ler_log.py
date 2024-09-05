import re
import os
import os.path

# print(os.listdir())
# print(os.getcwd())
arquivo = ""
conteudo = ""
ip_encontrados = []
arquivo_existe = (os.path.exists(r'C:\Users\kauak\Desktop\Python_Exercicios\secpy\access.log'))

def filtrar_ip(conteudo):
    regex = r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})'
    for linha in conteudo.splitlines():
        match = re.search(regex, linha)
        if match:
            ip_encontrados.append(match.group())
            print(f"Ip encontrado: {match.group()}")
    return ip_encontrados

if arquivo_existe:
    print("Arquivo existe, lendo arquivo: Procurando por endereços...\n")
    arquivo = open(r'C:\Users\kauak\Desktop\Python_Exercicios\secpy\access.log', 'r')
    conteudo = arquivo.read()
    filtrar_ip(conteudo)
    arquivo.close()

else:
    print("Arquivo não existe!")