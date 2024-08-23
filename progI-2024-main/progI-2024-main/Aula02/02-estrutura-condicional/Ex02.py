"""
Exercício 02 – Peça ao usuário dois números inteiros e exiba as comparações:
maior, menor, igual, diferente, maior ou igual, menor ou igual.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5

Saída:
10 é maior que 5.
10 não é menor que 5.
10 não é igual a 5.
10 é maior ou igual a 5.
10 não é menor ou igual a 5.

"""
num1_int = int(input("Digite um numero inteiro: \n"))
num2_int = int(input("Digite um numero inteiro: \n"))

#Verifica qual é maior
if (num1_int > num2_int):
    maior = num1_int
    print(f"{maior} É maior do que {num2_int} ")
elif (num2_int > num1_int):
    maior = num2_int
    print(f"{maior} É maior do que {num1_int} ")

#Verifica qual é menor
if (num1_int < num2_int):
    menor = num1_int
    print(f"{num2_int} não é menor que {menor}")
elif (num2_int < num1_int):
    menor = num2_int
    print(f"{num1_int} não é menor que {menor}")

#Verifica se é igual
if (num1_int != num2_int):
    print(f"{num2_int} não é igual a {num1_int}")
elif (num2_int != num1_int):
    print(f"{num2_int} não é igual a {num1_int}")

#Verifica qual é maior ou igual
if (num1_int >= num2_int):
    maior = num1_int
    print(f"{maior} É maior ou igual a  {num2_int} ")
elif (num2_int >= num1_int):
    maior = num2_int
    print(f"{maior} É maior ou igual a {num1_int} ")

#Verifica qual é menor ou igual a
if (num1_int <= num2_int):
    menor = num1_int
    print(f"{num2_int} É menor ou igual a  {menor}")
elif (num2_int <= num1_int):
    menor = num2_int
    print(f"{num1_int} É menor ou igual a {menor}")

