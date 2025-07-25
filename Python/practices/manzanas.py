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

inventory = [{"name": "Manzana", "stock": 20, "price": 5}]


def welcome_and_get_name():
    print("Bienvenido, ¿cuál es tu nombre?")
    name = input()
    return name


def greet_and_show_inventory(user_name, current_inventory):
    print(f"\nHola, {user_name}. Contamos con:")
    for product in current_inventory:
        print(
            f"- {product['stock']} {product['name']} a un precio de ${product['price']} cada una."
        )


def process_shopping(current_inventory):
    apple_product = current_inventory[0]

    while True:
        try:
            print("\n¿Cuántas manzanas quieres comprar?")
            quantity_str = input()
            quantity = int(quantity_str)

            if quantity < 0:
                print("No puedes comprar una cantidad negativa. Inténtalo de nuevo.")
                continue

            if quantity == 0:
                print("No has comprado nada. ¡Vuelve pronto!")
                return

            if quantity > apple_product["stock"]:
                print(
                    f"Lo siento, no tenemos suficientes manzanas. Solo nos quedan {apple_product['stock']}."
                )
                continue

            total_price = quantity * apple_product["price"]
            apple_product["stock"] -= quantity

            print(f"\nCompraste {quantity} manzanas, el total es: ${total_price}.")
            print(
                f"Ahora restan {apple_product['stock']} manzanas en nuestro inventario."
            )
            print("¡Gracias por tu compra!")
            break

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")


def main():
    """Función principal para ejecutar el programa de la tienda."""
    user_name = welcome_and_get_name()

    greet_and_show_inventory(user_name, inventory)

    process_shopping(inventory)


if __name__ == "__main__":
    main()
