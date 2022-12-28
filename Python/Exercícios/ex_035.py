from colorama import Fore, Style
print(Fore.CYAN + Style.BRIGHT + "-=-" * 25 + Style.RESET_ALL)
print("    " * 6 + Fore.GREEN + Style.BRIGHT +
      "Analisando Triângulo" + Style.RESET_ALL)
print(Fore.CYAN + Style.BRIGHT + "-=-" * 25 + Style.RESET_ALL)

t1 = float(input("Digite o primeiro seguemento de reta: "))  # A
t2 = float(input("Digite o segundo seguemento de reta: "))   # B
t3 = float(input("Digite o terceiro seguemento de reta: "))  # C

if ((t2 - t3) < t1 < (t2 + t3)) and ((t1 - t3) < t2 < (t1 + t3)) and ((t1 - t2) < t3 < (t1 + t2)):
    print("E possivel format um" + Fore.GREEN + Style.BRIGHT +
          " TRIÂNGULO COM ESSE VALORES" + Style.RESET_ALL)
else:
    print("Com esse valores" + Fore.RED + Style.BRIGHT +
          " NÃO E POSSIVEL FORMAR UM TRIÃNGULO COM ESSE VALORES" + Style.RESET_ALL)
