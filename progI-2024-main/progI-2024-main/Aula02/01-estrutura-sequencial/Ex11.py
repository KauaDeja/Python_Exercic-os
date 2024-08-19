"""
Exercício 11 – Peça ao usuário dois números e verifique se ambos são pares,
se ambos são ímpares e se um é par e o outro ímpar.

Entrada:
Digite o primeiro número: 4
Digite o segundo número: 7

Saída:
Ambos são pares? False
Ambos são ímpares? False
Um é par e o outro ímpar? True
"""

num1 = int(input("Digite o primeiro numero: \n"))
num2 = int(input("Digite o segundo numero: \n"))

print(f"Ambos são pares? {(num1 % 2) == 0 and (num2 % 2) == 0}")
print(f"Ambos são ímpares? {(num1 % 2) != 0 and (num2 % 2) != 0}")
if (num1 % 2 == 0 and num2 % 2 != 0) or (num1 % 2 != 0 and num2 % 2 == 0):
    print("Um número é par e o outro é ímpar.")
else:
    print("Ambos os números são pares ou impares.")