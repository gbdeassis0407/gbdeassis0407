reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"

n1 = float(input("Digite a Primeira Nota: "))
n2 = float(input("Digite a Segunda Nota: "))

media = (n1 + n2)/2

if media >= 7.0:
    print("Aluno tirou a media " + green + "{:.1f}".format(media) +
          reset_color + " ,Então esta " + green + "APROVADO" + reset_color)
elif media < 7 and media >= 5:
    print("Aluno tirou a media " + yellow + "{:.1f}".format(media) + reset_color +
          " ,Então o aluno vai para " + yellow + "RECUPERAÇÃO" + reset_color)
elif media < 5:
    print("Alunoe tirou a media " + red + "{:.1f}".format(media) + reset_color +
          " , Então o aluno esta " + red + "REPROVADO" + reset_color)
