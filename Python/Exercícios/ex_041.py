import datetime
from colorama import Fore, Style

nasc = int(input("Digite o ano de nascimento: "))
hoje = datetime.date.today().year
idade = hoje - nasc

print("O atleta tem " + Fore.GREEN + Style.BRIGHT +
      "{} anos".format(idade) + Style.RESET_ALL)

if idade <= 9:
    print("Classificação: " + Fore.GREEN +
          Style.BRIGHT + "MIRIM" + Style.RESET_ALL)
elif idade <= 14:
    print("Classificação: " + Fore.GREEN +
          Style.BRIGHT + "INFANTIL" + Style.RESET_ALL)
elif idade <= 19:
    print("Classificação: " + Fore.GREEN +
          Style.BRIGHT + "JUNIOR" + Style.RESET_ALL)
elif idade <= 25:
    print("Classificação: " + Fore.GREEN +
          Style.BRIGHT + "SÊNIOR" + Style.RESET_ALL)
else:
    print("Classificação: " + Fore.GREEN +
          Style.BRIGHT + "MASTER" + Style.RESET_ALL)

'''print("O atleta tem {} anos".format(idade))
print("Classificação: MASTER")
'''
