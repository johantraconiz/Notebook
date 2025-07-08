# Funciones


def saludar(name):
    print("Hola,", name)


# saludar("Johan")


def convertir_a_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


while True:
    print("Conversor de Celsius a Fahrenheit")
    print("1. Convertir a Fahrenheit")
    print("2. Salir")
    opcion = input()

    if opcion == "1":
        print("Ingresa una temperatura en Celsius")
        celsius = float(input())
        resultado = convertir_a_fahrenheit(celsius)
        print(resultado)
    else:
        break

print("Fin del programa")

import random

resultado = random.randint(1, 10)
print("Número random:", resultado)


def sumar(num1, num2=0):
    return num1 + num2


print("Sumando 2 numeros:", sumar(5, 3))
print("Sumando 1 número más el opcional (0):", sumar(5))
