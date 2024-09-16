"""
Exercício 07 - Crie um programa que verifica a senha inserida pelo usuário, permitindo um número limitado de tentativas.
Instruções:
Definir uma senha correta (por exemplo, "1234").
Solicitar ao usuário que insira a senha.
Usar um loop while para verificar se a senha está correta, com um limite de 3 tentativas.
Informar o usuário se a senha estiver incorreta e solicitar outra tentativa.
Após o loop, verificar se a senha está correta.
Exibir "Senha correta. Acesso concedido" se a senha estiver correta.
Se o número de tentativas exceder 3, exibir "Você excedeu o número de tentativas permitidas. Acesso negado."

Exemplo:
Digite a senha: 123
Senha incorreta. Tente novamente.
Digite a senha: 234
Senha incorreta. Tente novamente.
Digite a senha: 122
Senha incorreta. Tente novamente.
Você esgotou suas tentativas. Acesso negado.
"""

def senha():
    password = "Kaua123"
    tentativas = 0

    while(True):
        password_user = input("Digite a sua senha: ")
        tentativas +=1
        if(tentativas == 3):
            print("Você excedeu o número de tentativas permitidas. Acesso negado.")
            break
        elif(password_user != password):
            print("Senha incorreta. Tente novamente.")
        else:
            print("Senha correta. Acesso concedido")
            break
    pass

senha()