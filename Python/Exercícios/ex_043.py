# Legenda para coloração do print
reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"

# Criação da classi calculo de IMC


def calculoimc():
    # Solicitação dos dados junto de captura de erros
    try:
        peso = float(input("Qual é o seu peso? (Kg) "))
        altura = float(input("Qual é sua altura? (m) "))
    except ValueError:
        print(green + "Por favor colocar valores validos =)" + reset_color)
        calculoimc()

    # Calculo do IMC
    imc = peso / (altura ** 2)

    # montagem da tabela de valores IMC
    print("-=" * 25, end="")
    print("TABELA DE IMC", end="")
    print("-=" * 25)
    print(cyan + "IMC Menor que 18,5     Abaixo do peso\nIMC Entre 18,5 e 24,9  Peso normal\nIMC Entre 25 e 29,9    Acima do peso (sobrepeso)")
    print("IMC Entre 30 e 34,9    Obesidade I \nIMC Entre 35 e 39,9    Obesidade II \nIMC Maior do que 40    Obesidade III" + reset_color)
    print("-=" * 50)

    # Amostra do calculo do IMC
    print("\nO IMC dessa pessoa é de " + green +
          "{:.2F}".format(imc) + reset_color)

    # Decisição da mensagem baseada no valor de IMC
    if imc <= 18.5:
        print("Você esta " + red +
              "MUITO ABAIXO DO PESO NORMAL, ATENÇÃO!!" + reset_color)
    elif imc < 25:
        print("Você esta com peso Ideal, " +
              green + "\nPARABENS!!!" + reset_color)
    elif imc < 30:
        print("Você esta acima do peso ideal, " +
              yellow + "\nSOBREPESO!" + reset_color)
    elif imc < 35:
        print("Você esta um pouco acima do peso, " +
              yellow + "CUIDADO \nOBESIDADE 1!" + reset_color)
    elif imc < 40:
        print("Você esta acima do peso ideal, " + red +
              "MUITO CUIDADO \nOBESIDADE 2!!" + reset_color)
    else:
        print("Você esta " + red +
              "MUITOOOOOO ACIMA DO PESO, RISCO A SUA SAUDE EXTREMO CUIDADO!!! OBESIDADE 3!!!" + reset_color)


calculoimc()
