"""
Exercício 07 - Escreva um programa que recebe o valor total
e aplica descontos em compras:
-5% para compras até R$100,
-10% para compras acima de R$100 até R$500, e
-15% para compras acima de R$500.
Exiba o valor original, o valor do desconto e o valor final.

Entrada:
Digite o valor total das suas compras (em R$): 200

Saída:
Valor total: R$ 200.00
Valor com desconto: R$ 180.00
Desconto: R$ 20.00
"""
valor_com_desconto = 0
desconto = 0

def calcular_desconto(valor_total):
    # implemente a função
    if valor_total <= 100:
        desconto = valor_total * 0.05
        valor_com_desconto = valor_total - desconto
    elif valor_total <= 500:
        desconto = valor_total * 0.1
        valor_com_desconto = valor_total - desconto
    else:
        desconto = valor_total * 0.15
        valor_com_desconto = valor_total - desconto
    return valor_com_desconto, desconto

valor_total = float(input("Digite o valor total das suas compras (em R$): "))

valor_com_desconto, desconto = calcular_desconto(valor_total)

print(f"Valor total: R$ {valor_total:.2f}")
print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
print(f"Desconto: R$ {desconto:.2f}")

