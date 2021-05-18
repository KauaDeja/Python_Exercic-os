dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
total = (60 * dias)+(km * 0.15)
print(f'O total a ser pago é de R${total:.2F}')