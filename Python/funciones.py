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
