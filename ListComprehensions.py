print("List Comprehensions")

# They are a very powerful tool, which create a new list based on another list, in a single, readable line.

# Example: Necesitamos crear una lista de enteros que especifique la longitud de cada palabra en una frase,
# pero solo si la palabra no es la palabra "the"

print("Example 1:")
# Esto es lo que hariamos de forma normal
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lenghts = []

for word in words:
    if word != "the":
        word_lenghts.append(len(word))

print(words)

print("Usando una list comprehension")
word_lenghtsLC = [len(word) for word in words if word != "the"]

print(words)

print("Example 2")
# Usando una list comprehension, crea una nueva lista llamada newlist
# fuera de la lista "numbers", la cual contenga únicamente los numeros
# positivos de la lista, como enteros.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [num for num in numbers if num > 0]
print(newlist)



















