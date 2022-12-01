algo = input("Digite qualquer coisa: ")

print("O tipo primitivo desse valor = ", type(algo))  # retorna o que e algo
print("So tem espaços ? ", algo.isspace())  # E so espaço
print("E um numero ? ", algo.isnumeric())
print("E alfabetico ? ", algo.isalpha())
print("E alfanumérico ? ", algo.isalnum())
print("Esta em maiuscula ? ", algo.isupper())
print("Esta em minuscula ? ", algo.islower())
print("Esta capitalizada ? ", algo.istitle())
