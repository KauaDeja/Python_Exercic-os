"""
Exercício 08 – Crie um programa que solicita duas notas (n1 e n2)
e calcule a média aritmética dessas notas.
Exiba o resultado usando duas casas decimais.

Entrada:
Digite a primeira nota: 8
Digite a segunda nota: 7

Saída:
A média aritmética é: 7.50

"""
n1 = float(input("Digite a nota 1: \n"))
n2 = float(input("Digite a nota 2: \n"))

print(f"A média aritmética é: {(n1 + n2)/2:.2f}")
