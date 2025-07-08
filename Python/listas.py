# listas = Una varieble que contiene un arreglo de varios valores

names = ["Carter", "Emile", "Cath", "Jorge", "Jun", "Noble 6"]
print(names)

names[2] = "Kat"
print(names)

names.append("Rosenda")
print(names)


names.remove("Jun")
print(names)

del names[0]
print(names)

print("Kat" in names)
print("Thom" in names)

for name in names:
    print(name)
