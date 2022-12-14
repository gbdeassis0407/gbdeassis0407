nome = str(input("Digite seu nome completo: ")).strip()

separa = nome.split()

print("Muito prazer {}".format(separa[0]))
print("Seu ultimo nome: {}".format(separa[len(separa)-1]))
