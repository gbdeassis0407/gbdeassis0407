from random import randint
from time import sleep


def jokenpo_game():

    jokenpo = ("PEDRA", "PAPEL", "TESOURA")
    computador = randint(0, 2)
    print("Suas opções:\n[ 0 ] PEDRA\n[ 1 ]PAPEL\n[ 2 ]TESOURA")
    try:
        jogada = int(input("Qual é a sua jogada ? "))
    except (TypeError, ValueError, SyntaxError):
        print("JOGADA INVALIDADE")
        jokenpo_game()
    # print("JO")
    # sleep(1)
    # print("KEN")
    # sleep(1)
    # print("PO!!!")
    # sleep(0.5)

    print("-=" * 25)
    print("O Computador jogou {}".format(jokenpo[computador]))
    print("O jogador jogou {}".format(jokenpo[jogada]))
    print("-=" * 25)
    sleep(0.5)

    if computador == 0:  # Computador jogou PEDRA
        if jogada == 0:
            print("EMPATE")
        elif jogada == 1:
            print("Vitoria do JOGADOR")
        elif jogada == 2:
            print("Vitoria do COMPUTADOR")
        else:
            print("Faça Uma jogada validade na proxima")
            jokenpo_game()
    elif computador == 1:  # computador jogou PAPEL
        if jogada == 0:
            print("Vitoria do COMPUTADOR")
        elif jogada == 1:
            print("EMPATE")
        elif jogada == 2:
            print("Vitoria do JOGADOR")
        else:
            print("Faça Uma jogada validade na proxima")
            jokenpo_game()
    elif computador == 2:
        if jogada == 0:  # computador jogou TESOURA
            print("Vitoria do JOGADOR")
        elif jogada == 1:
            print("Vitoria do COMPUTADOR")
        elif jogada == 2:
            print("EMPATE")
        else:
            print("Faça Uma jogada validade na proxima")
            jokenpo_game()


jokenpo_game()
