sal = float(input("Qual o salario de um funcionário ? R$"))

aum = sal + (sal * (15/100))

print("Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(
    sal, aum))
