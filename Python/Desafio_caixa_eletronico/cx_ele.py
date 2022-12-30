def Saque():
    print("Cedulas disponivel: R$2 R$5, R$10, R$20, R$50, R$100")
    valor = input("Por Favor digite o valor que quer sacar ? \nR$")
    try:
        valor = int(valor)
    except ValueError:
        print("Favor digitar um valor inteiro sem centavos")
        return Saque()

    total = valor
    cedula = 100
    total_cedula = 0

    if total % 2 == 0:
        while True:
            if total >= cedula:
                total -= cedula
                total_cedula += 1
            else:
                if total_cedula > 0:
                    print(
                        f"Foram sacadas total de {total_cedula} de cedulas de R$ {cedula}")
                if cedula == 100:
                    cedula = 50

                elif cedula == 50:
                    cedula = 20

                elif cedula == 20:
                    cedula = 10

                elif cedula == 10:
                    cedula = 5

                elif cedula == 5:
                    cedula = 2

                total_cedula = 0
                if total == 0:
                    break
        print("Muito obrigado pela preferencia\nTenha um otimo dia :)")
    else:
        print("Cedulas Indisponivel Para Valor")
        return Saque()
