dias = int(input("Quantos dias foi alugado o carro ? "))
km = float(input("Quantos KM foram rodados pelo carro ? "))

total = ((dias * 60) + (km * 0.15))

print("O total a pagar e de R${:.2f}". format(total))
