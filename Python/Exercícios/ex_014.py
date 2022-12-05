tc = float(input("Digite a temperatura em Celcius = "))

tf = (tc * (9/5) + 32)  # referencia da formula google

print(
    "Sua temperatura em celcisu {:.2f}°C equivale a {:.2f}°F em Fahrenheit".format(tc, tf))
