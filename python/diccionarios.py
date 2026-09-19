person = {"name": "Johan", "lastName": "Traconiz", "age": 25}

print(person)
print(person["name"])

person["profession"] = "Engineer"
print(person)

print("name" in person)

print("Methods")
for key in person.keys():
    print(key)

for val in person.values():
    print(val)

for item in person.items():
    print(item)
