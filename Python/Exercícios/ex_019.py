from random import choice
n = int(input("Digite numero de alunos que deseja sortear: "))
aluno = []

for i in range(0, n):
    nome = str(input("{}° Aluno: ".format(i+1)))
    aluno.append(nome)

sortudo = choice(aluno)
print("O Aluno escolhido foi: {}".format(sortudo))
