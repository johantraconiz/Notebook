"""
Haz condicionales
Crea un programa que imprima un mensaje solicitando al usuario un número entre el 1 y el 100:

a) Si el número es menor a 1, debe imprimir un mensaje "Favor de ingresar un número mayor a 0".
b) Si el número es mayor a 100, debe imprimir un mensaje "Favor de ingresar un número menor o igual a 100".
c) Si el número sí es entre 1 y 100, debe imprimir un mensaje "¡Muy bien! El <número> es una gran opción".
"""

while True:
    try:
        print("")
        print("*************************************")
        print("Ingresa un número entre 1 y 100.")
        print("Ingresa 'q' para salir.")

        user_input = input()

        if user_input == "q":
            print("Fin del programa.")
            break
        else:
            number = int(user_input)

            if number < 1:
                print("Ingresa un número mayor a 0.")
            elif number > 100:
                print("Ingresar un número menor o igual a 100.")
            else:
                print(f"¡Muy bien! El {number} es una gran opción.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
