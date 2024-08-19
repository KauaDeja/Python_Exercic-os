"""
Exercício 08 – Crie um programa que solicita dois números para o usuário,
e exibe a soma, subtração, multiplicação, divisão e resto da divisão entre eles.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 3

Saída:
10.0 + 3.0 = 13.0
10.0 - 3.0 = 7.0
10.0 * 3.0 = 30.0
10.0 / 3.0 = 3.33
10.0 % 3.0 = 1.0
"""
num1 = float(input("Digite um numero: \n"))
num2 = float(input("Digite outro numero: \n"))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2

print(f"{num1} + {num2} = {soma}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} = {mult}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} % {num2} = {mod}")