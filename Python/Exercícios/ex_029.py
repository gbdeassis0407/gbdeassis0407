from colorama import Fore, Style

vel = int(input("Qual é a velocidade atual do carro? "))

if vel <= 79:
    print(Fore.GREEN + Style.BRIGHT +
          "Tenha um bom dia! Dirija com segurança!" + Style.RESET_ALL)
else:
    multa = ((vel-80) * 7) + 120
    print(Fore.RED + Style.BRIGHT +
          "MULTADO! Você exedeu o limite permitido de 80Km/h' \nVocê deve pagar uma multado em {}R$".format(multa) + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT +
          "Tenha um bom dia! Dirija com segurança!" + Style.RESET_ALL)
