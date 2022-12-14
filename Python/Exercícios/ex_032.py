import datetime
from colorama import Fore, Style

ano = int(input("Que ano quer analisar ? Coloque 0 para analisar o ano atual: "))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("O ano {} é ".format(ano) + Fore.GREEN + Style.BRIGHT +
          "BISSEXTO" + Style.RESET_ALL)
else:
    print("O ano {} ".format(ano) + Fore.RED + Style.BRIGHT +
          "NÃO e BISSEXTO" + Style.RESET_ALL)
