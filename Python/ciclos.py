# Cliclo, bucle, iteracion

# While
"""
numero = 0
while numero < 5:
    print(numero)
    numero = numero + 1

print("Fin del bucle")

i = 0
while i < 10:
    if i < 5:
        print("El numero", i, "es menor a 5")
    else:
        print("El numero", i, "es mayor o igual a 5")
    i += 1
"""

# For
"""
for x in range(10):
    print(x)
"""

while True:
    print("1. Continuar")
    print("2. Salir")
    print("Escribe una opción")

    opcion = input()

    if opcion == "1":
        print("Continuando...")
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Escribe 2 para salir")

print("Fin del programa")