"""
Exercício 03 – Peça ao usuário três números inteiros
e exiba qual é o maior e qual é o menor entre eles.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5
Digite o terceiro número: 8

Saída:
O maior número é 10.
O menor número é 5.

"""
num1_int = int(input("Digite um numero inteiro: \n"))
num2_int = int(input("Digite um numero inteiro: \n"))
num3_int = int(input("Digite um numero inteiro: \n"))

#Verificar qual dos 3 numeros é maior
maior = num1_int
if( num2_int > num1_int and num2_int > num3_int ):
    maior = num2_int

if( num3_int > num1_int and  num3_int >= num2_int ):
    maior = num3_int

#Verificar qual dos 3 numeros é menor
menor = num1_int
if( num2_int < num1_int and num2_int < num3_int ):
    menor = num2_int

    
if( num3_int <= num1_int and num3_int < num2_int ):
    menor = num3_int

print(f"O menor numéro é {menor}")
print(f"O maior numéro é {maior}")
