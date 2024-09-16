"""
Exercício 04 – Crie um programa que solicita ao usuário
para inserir uma série de números, e ele só irá somar
os números pares fornecidos. Use o comando continue.

Entrada:
Digite um número (ou 0 para sair): 5
Digite um número (ou 0 para sair): 4
Digite um número (ou 0 para sair): 1
Apenas números pares são somados. Tente novamente.
Digite um número (ou 0 para sair): 0

Saída:
A soma total dos números pares é: 4
"""
def calc_soma():
    soma_total = 0
    while(True):
        num = int(input("Digite um número (ou 0 para sair): "))
        if(num != 0 and num % 2 == 0):
            soma_total +=num
            print(soma_total)
        elif(num % 2 != 0):
            print("Apenas números pares são somados")
        else:
            print("Saindo...")
            print(f"A soma total dos pares é: {soma_total}")
            break
    pass

calc_soma()