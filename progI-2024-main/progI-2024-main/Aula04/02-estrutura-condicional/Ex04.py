"""
Exercício 04 - Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.
Definir as funções eh_positivo, eh_negativo e eh_zero.

Entrada:
Digite um número inteiro: 5

Saída:
5 é um número positivo.
"""

# Solicitando número ao usuário
numero = int(input("Digite um número inteiro: "))

def eh_negativo(a):
    return a < 0

def eh_positivo(a):
    return a > 0

def eh_zero(a):
    return a == 0

if eh_negativo(numero):
    print(f"{numero} é negativo")
elif eh_positivo(numero):
    print(f"{numero} é positivo")
else:
    eh_zero(numero)
    print(f"{numero} é nulo")