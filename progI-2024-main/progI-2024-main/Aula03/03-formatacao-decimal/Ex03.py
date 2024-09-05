"""
Exercício 03 - Modifique o exercício anterior adicionando o cálculo da margem do lucro em %.
Exiba o valor com duas casas decimais.

Entrada:
Digite o preço de venda: 100
Digite o custo do produto: 80

Saída:
O lucro é de: 20.00
A margem de lucro é de: 20.00%

"""

preco = float(input("Preço de venda: \n"))
custo = float(input("Custo do produto: \n"))

margen_lucro = preco % custo

print(f"O lucro é de: {preco - custo:.2f}\nA margem de lucro é de: {margen_lucro:.2f}%")