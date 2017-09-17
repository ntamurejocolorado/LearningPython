# Basic Operators
# Arithmetic Operators

number = 1 + 2 * 3 /4
print("Value %f" % number)

# Using two multiplication symbols makes a power relationship

a = 7
b = 2
squared = a ** 2
cubed = b ** 3

# Para mostrar varias variables en python 3 hay que poner %(var1,var2,varn)
print("El cuadrado de %d es %d" %(a,squared))
print("El cubo de %d es %d" %(b,cubed))

# Using Operators with strings
print("Python supports concatenating string using the addition operator.")
helloWorld = "hello"+ " "+"world"
print(helloWorld)

print("Python also supports multiplying strings to form a string with a repeating sequence")
lotsofhellos = "hello, " * 10
print(lotsofhellos)

print("Lists can be joined with the addition operators")
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print("All numbers con concatenacion de listas:")
print(all_numbers)

print([1,2,3] * 3) # permite repetir 3 veces la lista


# Exercise
# The target of this exercise is to create two lists called x_lists and y_list, which contain 10 instances
# of the variables x and y, respectively. You are also required to create a list called big_list, which contains
# the variables x and y, 10 times each, by concatenating the two lists you have created.

print("Exercise:")
x = object()
y = object()

# TODO: change this code
x_list= [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")

if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
