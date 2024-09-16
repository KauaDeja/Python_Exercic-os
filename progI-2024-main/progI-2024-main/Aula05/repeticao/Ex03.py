"""
Exercício 03 – Crie um programa que calcula a soma de
números inseridos pelo usuário até que o usuário decida parar.

Entrada:
Digite um número (ou 0 para sair): 5.5
Digite um número (ou 0 para sair): 3
Digite um número (ou 0 para sair): 0

Saída:
A soma total é: 8.5
"""


def calc_soma():
    soma_total = 0
    while(True):
        num = int(input("Digite um número (ou 0 para sair): "))
        if(num != 0):
            soma_total +=num
            print(soma_total)
        else:
            print("Saindo...")
            print(f"A soma total é: {soma_total}")
            break
    pass

calc_soma()