from math import radians,sin, cos, tan
a = float(input('Digite o ângulo que vc deseja: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print(f'O angulo de {a} tem o cosseno de {seno:.2f}')
print(f'O angulo de {a} tem o SENO de {cosseno:.2f}')
print(f'O angulo de {a} tem o tangente de {tangente:.2f}')
