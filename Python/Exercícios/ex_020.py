from random import shuffle
n = int(input("Quantos alunos vão apresentar: "))

aluno = []

for i in range(0, n):
    nome = str(input("{}° alunos a apresentar: ".format(i+1)))
    aluno.append(nome)

shuffle(aluno)
print("A ordem de apresentação será ")
print(aluno)
