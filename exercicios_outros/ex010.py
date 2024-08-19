largura = float(input('Largura da parede?'))
altura = float(input('Altura da parede?'))
area = largura * altura
litrosTinta = area /2
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m \nPara pintar a parede, você precisará de {litrosTinta}l de tinta')