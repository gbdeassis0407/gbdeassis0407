nome = str(input("Digite seu Nome Completo: ")).strip()

nome_upper = nome.upper()
nome_lower = nome.lower()
nome_len = len(nome)-nome.count(' ')
separa = nome.split()

print("Analisando seu Nome....")
print("Seu nome em maiúsculo fica: {}".format(nome_upper))
print("Seu nome em minusculo fica: {}".format(nome_lower))
print("Seu nome tem ao todo {} letras".format(nome_len))
print("Seu primeiro nome é {}, e tem {} letras".format(
    separa[0], len(separa[0])))
