"""
Exercício 04 – Crie um programa que receba uma pontuação entre 0 a 60 pontos, calcule a nota entre 0 a 10.00
e exiba a nota usando duas casas decimais.

Entrada:
Digite a pontuação: 30

Saída:
A nota é: 5.00
"""

pontuacao = float(input("Digite a pontuacao entre 0 a 60: \n"))

if pontuacao <= 60:
    nota = (pontuacao / 60)*10
    print(f"A nota é: {nota:.2f}")
else:
    print(f"Pontuacao não esperada")