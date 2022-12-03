real = float(input("Quanto dinheiro você tem na carteira ? R$"))

dolar = real / 5.22

print("Com R${:.2f}, Você pode comprar U${:.2f} em dolar".format(real, dolar))
