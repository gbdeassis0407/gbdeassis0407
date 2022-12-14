frs = str(input("Digite uma Frase: ")).upper().strip()

print("A letra A parece {} vezes na frase".format(frs.count("A")))

print("A primeira letra A apareceu na posição {}".format(frs.find("A")+1))

print("A ultima letra A aparece na posição {}".format(frs.rfind("A")+1))
