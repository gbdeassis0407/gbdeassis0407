import datetime

reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"


def alistamento():
    try:
        sexo = int(
            input("Digite seu SEXO \n[1-MASCULINO]\n[2-FEMINIO]\nSEXO: "))
    except (ValueError, TypeError):
        print(red + "Favor digitar um valor valido" +
              reset_color + ", Tente Novamente")
        return alistamento()

    if sexo == 2:
        print(red + "VOCÊ NÃO PRECISA SE ALISTAR" + reset_color)

    elif sexo == 1:

        nascido = int(input("Ano de nascimento: "))
        hoje = datetime.date.today().year
        idade = hoje - nascido

        print("Quem nasceu em " + green +
              "{} tem {} anos em {}.".format(nascido, idade, hoje) + reset_color)

        if idade == 18:
            print("Você tem que se alistar " + red +
                  "IMEDIATAMENTE!" + reset_color)
        elif idade < 18:
            rest = 18 - idade
            print("Você ainda não tem 18 Anos, Ainda faltam " + green + "{}".format(rest) +
                  reset_color + " anos para se alistar")
            print("Seu alistamento será em " +
                  green + "{}.".format((rest + hoje)))
        elif idade > 18:
            rest = idade - 18
            print("Você já deveria ter se alistadó há " +
                  red + "{} anos".format(rest))
            print(reset_color + "Seu alistamento foi em " +
                  green + "{}.".format((hoje - rest)) + reset_color)


alistamento()
