"""valor = int(input("Digite um numero para visualizar a tabuada: "))

print('-' * 20)

for i in range(11):
    res = (valor * i)
    print(" {} x {} = {}".format(valor, i, res))
print('-' * 20)"""

print("Tabuada do 1 ao 10 ")

for i in range(1, 11):
    print("-" * 10)
    for j in range(1, 11):
        print(" {:2} x{:2} = {:2}".format(i, j, (i*j)))
