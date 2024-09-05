"""
Exercício 14 – Peça ao usuário dois números e verifique se o primeiro é divisível pelo segundo.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 3

Saída:
O primeiro número é divisível pelo segundo? False
"""
num1 = int(input("Digite um numero:\n"))
num2 = int(input("Digite outro numero:\n"))

def divisivel(valor1, valor2):
    
    return (valor1 % valor2 == True)

print(f"O primeiro número é divisível pelo segundo? {divisivel(num1, num2)}")