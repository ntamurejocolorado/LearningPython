# Variables and types

myint = 7
print(myint)
print("Value int:", myint)

myfloat = 7.0
print("Value float:", myfloat)

myfloat2 = float(7)
print("Value float 2:", myfloat2)

# strings
print("Strings in python")
print("-----------------")

myString = "Hello"  # The difference between the two is that using double quotes makes it easy to include apostrophes

myStringWithApostrophes = "Don't worry about apostrophes"

print(myString + " " + myStringWithApostrophes)

# There are additional variations on defining strings that make it easier to include things such as carriage returns,
# backslashes and Unicode characters.

one = 1
two = 2
three = one + two
four = two * two
five = two * two + one

# print(one + " " + two) It's an error. If we want to print int or float we have to use comma such as next line
print(one, two,three,four,five)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Mixing operators between numbers and strings is not supported
# print(one+two+hello)

# EXERCISE 2
# The target of this exercise is to create a string, an integer, and a floating point number.

print("Exercise 2:")
myStringExercise = "Hello"
myfloatExercise = float(10)
myintExercise = 20

# testing code
if myStringExercise == "Hello":
    print("String: %s" % myStringExercise)

if isinstance(myfloatExercise,float) and myfloatExercise == 10.0:
    print("Float: %f" % myfloatExercise)

if isinstance(myintExercise,int) and myintExercise == 20:
    print("Int: %d" % myintExercise)