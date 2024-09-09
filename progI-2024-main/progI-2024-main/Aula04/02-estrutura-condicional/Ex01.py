"""
Exercício 01 – Crie um programa que solicita um número inteiro para o usuário.
Após isso, verifique se o número é par ou ímpar.
Crie uma função chamada eh_par que recebe um número inteiro e retorna True se o número for par e False se for ímpar.

Entrada:
Digite um número inteiro: 5

Saída:
5 é um número ímpar.
"""
num1 = int(input("Digite um número:\n"))

def eh_par(numero1):
    
    return (numero1 % 2 == 0)

def EhImpar(numero1):

    return (numero1 % 2 != 0)


if (eh_par(num1)):
    print(f"O numero é par")
elif (EhImpar(num1)):
    print(f"O número é impar")
else:
    print(f"Erro")
