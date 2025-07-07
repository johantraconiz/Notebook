import random

resultado = random.randint(1, 10)
print("Número random:", resultado)


def sumar(num1, num2=0):
    return num1 + num2


print("Sumando 2 numeros:", sumar(5, 3))
print("Sumando 1 número más el opcional (0):", sumar(5))
