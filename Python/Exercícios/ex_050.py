cont = 1
soma = 0
for i in range(1, 7):
    n = int(input("Digite o {}° a somar:".format(cont)))
    cont += 1
    if n % 2 == 0:
        soma += n
print("Resultado da sua soma = {}".format(soma))
