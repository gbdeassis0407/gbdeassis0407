print("=" * 15, "Loja Guanabara", "=" * 15)

valor = float(input("Preço da Compras: R$"))

try:
    print("FORMAAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque")
    print("[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão")
    opcao = int(input("Qual a forma de pagamento? "))
except ValueError:
    print("Por favor selecionar uma forma de pagamento valida!!")


def formardepagamento(opcao):

    if opcao == 1:
        total = valor - (valor * 0.10)
        print("A compra de R${:.2f}, com desconto de 10% pelo pagamento a vista em dinheiro fica no total de R${:.2f}".format(
            valor, total))

    elif opcao == 2:
        total = valor - (valor * 0.05)
        print("A compra de R${:.2f}, com desconto de 5% pelo pagamento a vista no cartão R${}".format(
            valor, total))

    elif opcao == 3:
        parcela = valor/2
        print("Em 2x no cartão, a parcela fica em R${:.2f}, no total de R${:.2f}".format(
            parcela, valor))

    elif opcao == 4:
        try:
            vezes = int(input("Em quantas Parcelas ? "))
        except ValueError:
            print("Por favor digitar o valor da parcela corretamente")

        parcela = (valor/vezes) * 1.20
        total = parcela * vezes

        print("Sua compra será parcelada em {}x de {:.2f} COM JUROS ".format(
            vezes, parcela))
        print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(
            valor, total))

    else:
        print("OPÇÃO INVALIDADE DE PAGAMENTO!!!\nPor favor selecionar uma forma de pagamento valida!!!")
        formardepagamento()


formardepagamento(opcao)
