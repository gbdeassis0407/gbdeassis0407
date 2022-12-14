from random import randint
from time import sleep
from colorama import Fore
from colorama import Style

num_sort = randint(0, 5)  # Sorteira um numero de 0 a 5
print(Fore.YELLOW + "-=-" * 15)
print(Fore.CYAN + Style.BRIGHT +
      "Vou pensar em um número entre 0 e 5. TENTE ADIVINHAR SE VOCÊ E BOM MESMO....." + Style.RESET_ALL)
print(Fore.YELLOW + "-=-" * 15)
jogador = int(input(Fore.CYAN + Style.BRIGHT +
              "Em que número eu estou pensando? " + Style.RESET_ALL))

print(Fore.CYAN + Style.DIM + "PROCESSANDO..." + Style.RESET_ALL)
sleep(2)

if jogador == num_sort:
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT +
          "NÃOOOOOO DIOOOOOO DAAA, VOCÊ ACERTOUUUUUUU JOTAROUU" + Style.RESET_ALL)
else:
    print(Fore.RED + Style.DIM +
          "QUE PENA VOCÊ ERROU, O NUMERO CERTO ERA ESSE {} CONO DIO DAAAA KKKKKKKKKK".format(num_sort))
