# Lists
#  Lists are very similar to arrays. They can contain any type of variable, and they
# can contain as many variables as you wish.

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist[0],mylist[1],mylist[2])

# Para recorrer una lista, podemos hacerlo con un bucle.
# En python no es necesario indicar el contador ni el final.
# En python sólo hay que decirle la variable (x) que sera la que recorrera
# la lista o array y la lista o array, tal como sigue en el ejemplo.

for x in mylist:
    print(x)

#Ejemplo 2

myListInt = [1,2,3]

myListFloat = [1.0,2.0,3.0]

myListString = ["hola","mundo"]

myListMerge = [myListInt,myListFloat,myListString]


#Show lists

print("My list Int:")
for x in myListInt:
    print(x)

print("My List Float")
for f in myListFloat:
    print(f)

print("My list String")
for s in myListString:
    print(s)

print("My List Merge:")
for m in myListMerge:
    print(m)


# EXERCISE 3 LISTS
#  Add the numbers 1,2 and 3 to the "numbers" list, and the words "hello" and "world"

numbers = []
strings = []
names = ["John","Eric","Jess"]

second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

print(numbers)
print(strings)

print("Second name: %s" % second_name)





















