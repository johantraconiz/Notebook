"""
Realiza estructuras de datos
Crea un programa que servirá como lista para el supermercado.

Este programa debe solicitar al usuario ingresar qué quiere agregar a su lista.
Debe contener también una opción para imprimir la lista (imprimiendo primero algún encabezado por ejemplo *** TU LISTA ***).
Al final debe tener una opción para salir del programa.
"""

lista_de_compras = []


def imprimir_menu():
    print("")
    print("***** Elige una opción *****")
    print("1. Añade un producto a tu lista de compras.")
    print("2. Elimina un producto de tu lista de compras.")
    print("3. Imprimit lista de compras")
    print("4. Salir")


def agregar_producto(producto):
    lista_de_compras.append(producto)


def eliminar_producto(producto):
    if producto in lista_de_compras:
        lista_de_compras.remove(producto)
    else:
        print(f"Producto '{producto}' no encontrado en la lista.")


def imprimir_lista(lista):
    for producto in lista:
        print(producto)


while True:
    imprimir_menu()

    try:
        opcion = input()

        if opcion == "1":
            print("¿Qué producto quieres agregar?")
            add_producto = input()
            agregar_producto(add_producto)
            print(f"{add_producto} agregado exitosamente a la lista de compras.")
        elif opcion == "2":
            print("¿Qué producto quieres eliminar?")
            remove_producto = input()
            eliminar_producto(remove_producto)
            print(f"{remove_producto} eliminado exitosamente de la lista de compras.")
        elif opcion == "3":
            print("Tu lista de compras es:")
            imprimir_lista(lista_de_compras)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
    except ValueError:
        print("Error: Entrada inválida.")
