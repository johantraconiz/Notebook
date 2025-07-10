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

# Se mantiene la estructura de inventario para futura extensibilidad.
inventory = [{"name": "Manzana", "stock": 20, "price": 5}]


def welcome_and_get_name():
    """Da la bienvenida y solicita el nombre del usuario."""
    print("Bienvenido, ¿cuál es tu nombre?")
    name = input()
    return name


def greet_and_show_inventory(user_name, current_inventory):
    """Saluda al usuario y muestra el inventario."""
    print(f"\nHola, {user_name}. Contamos con:")
    for product in current_inventory:
        # Usamos 's' para pluralizar si el stock no es 1. Simple pero efectivo.
        plural = "s" if product["stock"] != 1 else ""
        print(
            f"- {product['stock']} {product['name']}{plural} a un precio de ${product['price']} cada una."
        )


def process_shopping(current_inventory):
    """Procesa la compra de manzanas, validando la entrada y actualizando el stock."""
    # Asumimos que solo vendemos manzanas por ahora, como en el código original.
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
                return  # Salimos de la función si no compra nada.

            if quantity > apple_product["stock"]:
                print(
                    f"Lo siento, no tenemos suficientes manzanas. Solo nos quedan {apple_product['stock']}."
                )
                continue

            # Si la entrada es válida, procesamos la compra
            total_price = quantity * apple_product["price"]
            apple_product["stock"] -= quantity

            print(f"\nCompraste {quantity} manzanas, el total es: ${total_price}.")
            print(
                f"Ahora restan {apple_product['stock']} manzanas en nuestro inventario."
            )
            print("¡Gracias por tu compra!")
            break  # Salimos del bucle de compra

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")


def main():
    """Función principal para ejecutar el programa de la tienda."""
    user_name = welcome_and_get_name()

    greet_and_show_inventory(user_name, inventory)

    process_shopping(inventory)


if __name__ == "__main__":
    main()
