import random


def mostrar_menu():
    print("")
    print("*** Adivina si el dado tiene un valor Par o Impar ***")
    print("1. Par")
    print("2. Impar")
    print("3. Salir")


def pedir_valor():
    print("Ingresa un valor")
    return int(input())


def tirar_dados():
    return random.randint(2, 12)


def imprimir_resultado(input, dados):
    if input == 1 and dados % 2 == 0:
        print("Ganaste, el número es", dados)
    elif input == 2 and dados % 2 != 0:
        print("Ganaste, el número es", dados)
    else:
        print("Perdiste, el número es", dados)


while True:
    mostrar_menu()
    intent = pedir_valor()

    if intent == 3:
        break
    elif intent == 1 or intent == 2:
        dados = tirar_dados()
        imprimir_resultado(intent, dados)
    else:
        print("Opción invalida, intenta de nuevo.")

print("Gracias por jugar.")
