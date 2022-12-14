from colorama import Fore, Style

num = int(input(Fore.BLUE + Style.DIM +
          "Me dia um número qualquer: " + Style.RESET_ALL))

if num % 2 == 0:
    print("O Número {} é".format(num) + Fore.GREEN +
          Style.BRIGHT + " PAR" + Style.RESET_ALL)
else:
    print("O Número {} é".format(num) + Fore.RED +
          Style.BRIGHT + " IMPAR" + Style.RESET_ALL)
