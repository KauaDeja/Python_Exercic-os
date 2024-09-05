"""
Exercício 09 – Crie um programa que recebe o preço de venda do produto e custo do produto.
Calcule o valor do lucro e exiba com duas casas decimais.

Entrada:
Digite o preço de venda: 100
Digite o custo do produto: 50

Saída:
O lucro é de: 50.00
"""

preco = float(input("Preço de venda: \n"))
custo = float(input("Custo do produto: \n"))

print(f"O lucro é: {preco - custo:.2f}")