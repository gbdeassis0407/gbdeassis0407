from colorama import Fore, Style

dist = float(input("Qual é a distância da sua viagem em KM ? "))
'''
if dist <= 200:
    taxa = dist * 0.50
elif dist >= 200:
    taxa = dist * 0.45
'''

taxa = dist * 0.50 if dist <= 200 else dist * 0.45

print("Você esta preste a começar uma viagem de" + Fore.GREEN +
      Style.BRIGHT + " {:.1f}KM".format(dist) + Style.RESET_ALL)
print("E o preço da sua passagem será " + Fore.GREEN +
      Style.BRIGHT + " R${:.2f}".format(taxa) + Style.RESET_ALL)
