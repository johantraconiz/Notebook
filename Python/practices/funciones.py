"""
Practica hacer funciones.
Para empezar, define una nueva función que reciba 3 parámetros. Esta función debe usar el primer parámetro para decidir qué operación hacer (suma, resta, multiplicación o división) y aplicarlo sobre los 2 parámetros restantes.

Ejemplo: resultado = tufuncion(“multiplicar”, 5, 4). (El resultado debería ser igual a 20)
Nota: Aquí estoy considerando que la función se llama “tufuncion”. En tu ejercicio pon el nombre que gustes a tu función.
"""


def calculadora(opcion, a, b):
    if opcion == "suma":
        return a + b
    elif opcion == "resta":
        return a - b
    elif opcion == "multiplicacion":
        return a * b
    elif opcion == "division":
        return a / b
    else:
        return "Operación invalida."


while True:
    try:
        print("")
        print("Escribe: suma, resta, multiplicacion o division")
        print("Escribe 'q' para salir.")
        operacion = input()

        if operacion == "q":
            print("Fin del programa.")
            break
        else:
            print("Escribe el primer número")
            a = float(input())
            print("Escribe el segundo número")
            b = float(input())
            resultado = calculadora(operacion, a, b)
            print(f"El resultado de la {operacion} es: {resultado}")
    except ValueError:
        print("Entrada inválida.")
