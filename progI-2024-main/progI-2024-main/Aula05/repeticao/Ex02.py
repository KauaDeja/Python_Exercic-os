"""
Exercício 02 - Crie um programa que solicite um número inteiro positivo e,
em seguida, imprima todos os números ímpares entre 0 e o número escolhido.
Entrada:
Digite um número inteiro positivo: 10
Saída:
1
3
5
7
9
"""

def calc_laco(num):
    qtd_count = 1

    while(qtd_count <= num):
        if (qtd_count % 2 != 0):
            print(qtd_count)
            qtd_count +=1
        else:
            qtd_count +=1
    pass

def main():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
    except:
        print("Erro inesperado!")   
    calc_laco(numero)
if __name__ == "__main__":
    main()