filas = input("Enter the number of rows: ")

try:
    filas = int(filas)
    for i in range(filas):
        print(" " * (filas - i - 1) + "*" * (i * 2 - 1))
except ValueError:
    print("Please enter a valid number")
