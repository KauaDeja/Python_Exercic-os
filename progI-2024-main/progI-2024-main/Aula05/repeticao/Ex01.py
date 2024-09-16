"""
Exercício 01 - Crie um programa que solicite ao usuário um número inteiro positivo
e, em seguida, faça uma contagem regressiva desse número até 1.

Entrada:
Digite um número inteiro positivo: 5

Saída:
5
4
3
2
1
Contagem regressiva concluída.
"""

try:
    numero = int(input("Digite um número inteiro positivo: "))
except:
    print("Erro inesperado!")

def main(numero):
    while(numero > 0):
        print(numero)
        numero -=1
    return numero

if __name__ == "__main__":
    main(numero)
    
# implemente seu código aqui
