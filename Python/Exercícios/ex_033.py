first = int(input("Primeiro Valor: "))
second = int(input("Segundo Valor: "))
third = int(input("Terceiro Valor: "))

numbers = [first, second, third]
'''
max = numbers[0]
min = numbers[0]

for i in range(0, len(numbers)):
    if (numbers[i] > max):
        max = numbers[i]

    if (numbers[i] < min):
        min = numbers[i]
'''
print("O maior numero = {}".format(max(numbers)))
print("O menor numero = {}".format(min(numbers)))
