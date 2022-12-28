reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"

casa = float(input("Valor da Casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))

prestacao = casa / (anos * 12)
minimo = salario * 0.30

print("Para pagar uma casa de R${:.2f} em {} anos, a prestação sera de R${:.2f}".format(
    casa, anos, prestacao))

# print("COMPARANDO tem que pagar {:.2f} e o mínimo é de {:.2f}".format(
#   prestacao, minimo))

if prestacao <= minimo:
    print("O valor do salario cobre 30%" " do valor da prestação," +
          green + " EMPRESTIMO APROVADO" + reset_color)
else:
    print("O valor do salario NÃO cobre os 30%" " do valor da prestação da prestação," +
          red + " EMPRESTIMO NEGADO" + reset_color)
