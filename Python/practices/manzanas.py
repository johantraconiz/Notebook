"""
Ahora necesito que crees un programa que:

1. Imprima un mensaje, dando la bienvenida al usuario y le preguntará su nombre.
2. Ahora el usuario deberá ingresar su nombre.
3. Imprima mensaje, saludando al usuario por su nombre, e indicando que actualmente tiene 20 manzanas disponibles, cada una por un precio de $5.

4. Imprima un mensaje, preguntando al usuario cuántas manzanas quiere comprar.
5. Ahora el usuario deberá ingresar cuántas manzanas quiere.
6. Imprima un mensaje indicando cuántas manzanas compró el usuario, y cuál fue el precio total.
7. Finalmente que imprima un mensaje indicando cuántas manzanas le quedaron disponibles después de la venta.
"""

inventory = []

apple = {"name": "Manzana", "stock": 20, "price": 5}
inventory.append(apple)


def name_question():
    print("Bienvenido, ¿Cual es tu nombre? ")
    name = input()
    return name


def greetin(user_name, inventory):
    print(f"Hola, {user_name}. Contamos con:")
    for product in inventory:
        print(f"{product["stock"]} {product["name"]} a un precio de ${product["price"]}")



while True:
    name = name_question()
    if name == "q":
        break
    greetin(name, inventory)
    