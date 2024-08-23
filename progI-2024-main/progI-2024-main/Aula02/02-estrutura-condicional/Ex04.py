"""
Exercício 04 - Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.
Entrada:
Digite um número inteiro: 5

Saída:
5 é um número positivo.

"""

num_int = int(input("Digite um numero inteiro: \n"))

if(num_int == 0):
    print(f"{num_int} É nulo")
elif(num_int >= 1 ):
    print(f"{num_int} É positivo")
elif(num_int <= -1 ):
    print(f"{num_int} É negativo")
else:
    print("O aluno está de recuperação")