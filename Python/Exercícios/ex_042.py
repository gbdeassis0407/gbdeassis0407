reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"

t1 = float(input("Digite o primeiro valor do triângulo: "))
t2 = float(input("Digite o segundo valor do triângulo: "))
t3 = float(input("Digite o terceiro valor do triângulo: "))

'''
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    #print("Com esse valores e possivel formar um triángulo", end="")
    if t1 == t2 == t3:
        print("E possivel formar um Triângulo com esse valores, é o triângulo e " +
              blue + "EQUILÁTERO" + reset_color)
    elif t1 == t2 != t3 or t1 == t3 != t2 or t2 == t3 != t1:
        print("E possivel formar um triângulo com esse valores, é o triângulo e " +
              magenta + "ISÓSCELES" + reset_color)
    else:
        print("E possivel formar um triãngulo com esse valores, é o triângulo e " +
              cyan + "ESCALENO" + reset_color)
else:
    print("Com esse valores" + red +
          " NÃO E POSSIVEL FORMAR UM TRIÂNGULO" + reset_color)
'''

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print(green + "Com esse valores e possivel formar um triángulo" +
          reset_color, end=" ")
    if t1 == t2 == t3:
        print(blue + "EQUILÁTERO!" + reset_color)
    elif t1 == t2 != t3 or t1 == t3 != t2 or t2 == t3 != t1:
        print(magenta + "ISÓSCELES!" + reset_color)
    else:
        print(cyan + "ESCALENO!" + reset_color)
else:
    print("Com esse valores" + red +
          " NÃO E POSSIVEL FORMAR UM TRIÂNGULO" + reset_color)
