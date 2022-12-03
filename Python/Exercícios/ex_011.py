x = float(input("Qual a largura da parede em metros: "))
y = float(input("Qual a altura da parede em metros: "))

mq = (x * y)
tinta = (mq/2)

print(" Sua parede tem a dimensão de {:.2f}m x {:.2f}m e sua área e de {:.4f}m²".format(
    x, y, mq))

print(" Para pintar a parede, você precisa de {:.4f}l de tinta".format(tinta))
