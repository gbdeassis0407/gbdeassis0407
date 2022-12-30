from colorama import Fore, Style


def conversor():

    decimal = int(input("Digite um numero inteiro: "))
    print("Escolha uma das bases para converter seu numero:")
    print("[ 1 ] Converter para BINARIO \n[ 2 ] Converter para OCTAL \n[ 3 ] Converter para HEXADECIMAL")
    choice = int(input("Sua Escolha:"))

    if choice == 1:
        print("O Numero Decimal {} convertido para BINARIO é = ".format(decimal)
              + Fore.GREEN + Style.BRIGHT + "{}".format(bin(decimal)[2:]) + Style.RESET_ALL)
    elif choice == 2:
        print("O Numero Decimal {} convertido para OCTAL é = ".format(decimal)
              + Fore.GREEN + Style.BRIGHT + "{}".format(oct(decimal)[2:]) + Style.RESET_ALL)
    elif choice == 3:
        print("O Numero Decimal {} convertido para HEXADECIMAL é = ".format(decimal)
              + Fore.GREEN + Style.BRIGHT + "{}".format(hex(decimal)[2:]) + Style.RESET_ALL)
    else:
        print("Por favor escolha uma opção valida para converter :)")
        conversor()


conversor()
