"""
Elabora algunos ciclos
Ahora, crea un programa que:

1. Solicite al usuario que ingrese un texto (cualquiera).
2. Solicite después al usuario ingresar cuántas veces desea imprimirlo (e.g. 10).

Recuerda que el programa debe imprimir el texto ingresado el número de veces solicitado, y terminar.
"""

try:
    print("Ingresa un texto")
    texto = input()
    print("Ingresa un número de veces que desas imprimir tu texto")
    number = int(input())
    print("imprimiendo...")
    for n in range(0, number):
        print(n + 1, texto)
    print("Fin.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")
