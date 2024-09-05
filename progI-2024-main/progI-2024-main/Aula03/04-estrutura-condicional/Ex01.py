"""
Exercício 01 – Crie um programa que solicita um número inteiro para o usuário.
Após isso, verifique se o número é par ou ímpar.

Entrada:
Digite um número inteiro: 5

Saída:
5 é um número ímpar.

"""
num1 = int(input("Digite um número:\n"))

def EhPar(numero1):
    
    return (numero1 % 2 == 0)

def EhImpar(numero1):

    return (numero1 % 2 != 0)


if (EhPar(num1)):
    print(f"O numero é par")
elif (EhImpar(num1)):
    print(f"O número é impar")
else:
    print(f"Erro")

