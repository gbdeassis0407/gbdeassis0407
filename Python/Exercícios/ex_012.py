valor = float(input("Qual o preeço do produto ? R$"))

#desc = valor - (valor * (5/100))
desc = valor - (valor * 0.05)

print("O pruoduto que custava R${:.2f}, na promoção com desconto de 5% vai custar {:.2f}".format(
    valor, desc))
