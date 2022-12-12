num = int(input("Digite um numero inteiro: "))

num_uni = num // 1 % 10
num_dez = num // 10 % 10
num_cen = num // 100 % 10
num_mil = num // 1000 % 10

print("Seu Numero tem {} Unidades".format(num_uni))
print("Seu Numero tem {} dezenas".format(num_dez))
print("Seu Numero tem {} centenas".format(num_cen))
print("Seu Numero tem {} milhar".format(num_mil))
