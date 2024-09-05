"""
Exercício 01 – Peça ao usuário dois números e verifique se ambos são pares, se ambos são ímpares e se um é par e o outro ímpar.
Defina uma função chamada ehPar.

"""
num1 = int(input("Digite um número:\n"))
num2 = int(input("Digite outro número:\n"))

def EhPar(numero1, numero2):
    
    return (numero1 % 2 == 0) and (numero2 % 2 == 0)

def EhImpar(numero1, numero2):

    return (numero1 % 2 != 0) and (numero2 % 2 != 0)


if (EhPar(num1, num2)):
    print(f"Ambos são pares: ")
elif (EhImpar(num1,num2)):
    print(f"Ambos são impares:")
else:
    print(f"Um número é par e outro é ímpar")