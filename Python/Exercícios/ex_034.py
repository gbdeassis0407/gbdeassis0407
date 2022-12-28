salario = float(input("Digite o valor do salario do funcionario R$"))

if salario >= 1250.00:
    reajuste = salario * 1.10
else:
    reajuste = salario * 1.15

print("O Novo valor de aumento do salario de R${}, depois do reajuste agora e R${}".format(
    salario, reajuste))
