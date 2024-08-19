# co = float(input('Comprimento do cateto oposto:'))
# ca = float(input('Comprimento do cateto adjacente:'))
# h = (co ** 2 + ca ** 2) ** (1/2)
# print(f'A hipotenusa vale {h:.2f}')

from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = hypot(ca, co)
print(f'A hipotenusa vale {h:.2f}')
