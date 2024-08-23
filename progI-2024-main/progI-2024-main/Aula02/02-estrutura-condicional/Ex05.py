"""
Exercício 05 - Faça um programa que recebe uma nota (0 a 10) e mostra se o aluno está reprovado (nota abaixo de 6),
de recuperação (nota entre 6 e 7) ou aprovado (nota acima de 7).

Entrada:
Digite a nota do aluno: 8

Saída:
O aluno está aprovado.

"""

nota = float(input("Digite uma nota de 0 a 10: \n"))

if(nota < 6):
    print("O aluno está reprovado.")
elif(nota > 7 ):
    print("O aluno está aprovado.")
else:
    print("O aluno está de recuperação")


