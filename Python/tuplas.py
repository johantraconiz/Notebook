"""
Las tuplas son similares a las listas.
Las tuplas no se pueden modificar.
Las tuplas están, entre paréntesis, en lugar de corchetes.

Podemos usar tuplas para estructuras que no deseamos modificar y asignarlas a otra estructura más grande si se desea.
"""

lista = ["Johan", 1999, True]
lista.append("Agosto")
print(lista)

tupla = ("Johan", 1999, True)
# tupla.append("Agosto") No esta permitido
print(tupla)

usuarios = []
usuarios.append(tupla)
print(usuarios)