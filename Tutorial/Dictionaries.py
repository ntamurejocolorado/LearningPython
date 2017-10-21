# Dictionaries

# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
# Each value stored in a dictionary can be accessed using a key, which is any type of object
# (string,number,list,etc) instead of using its index to address it.

print("Dictionaries: ")

print("Example 1:")

# Creamos un dictionario se usan llaves
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

print(phonebook)

# Otra forma de inicializar un dictionario es:
phonebook2 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook2)

print("Para iterar por los diccionarios")
# Se puede iterar por ellos como si fueran una lista. Hay que iterar por los items
for name,number in phonebook2.items():
    print("Phone number of %s is %d" %(name,number))

print("Remove a value")
# Para eliminar un valor concreto hay que hacerlo del siguiente modo:
del phonebook["John"] # se le da la palabra clave
print(phonebook)
#phonebook.pop("John")
print(phonebook)

print("EXERCISE:")

phonebook4 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook4["Jake"] = 938273443
del phonebook4["Jill"]

# testing code
if "Jake" in phonebook4:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook4:
    print("Jill is not listed in the phonebook.")