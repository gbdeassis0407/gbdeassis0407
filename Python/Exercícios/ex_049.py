num = int(input("Digite o número para ver sua a tabuada: "))
for i in range(1, 11):
    print("{} x {:2} = {}".format(num, i, num*i))
