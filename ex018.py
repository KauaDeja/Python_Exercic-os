import random
nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo aluno: '))
nome3 = str(input('Nome do terceiro aluno: '))
nome4 = str(input('Nome do quarto aluno: '))
lista = [nome1,nome2, nome3, nome4]
resultado = random.choice(lista)
print(f'O aluno escolhido foi {resultado}')