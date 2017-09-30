# String Formatting

# Python uses C-Style string formatting to create new, formatted strings. The % operator
# is used to format a set of variables enclosed in a tuple(a fixed size list), together
# with a format string, which contains normal text together with argument specifiers
# special symbols like %s and %d.

print("Exercise 1: This print out hello, John ")

name = "John"
print("Hello,%s!\n" % name)

print("Exercise 2: Show two or more arguments, we use tuple")

name = "Noelia"
age = 28
print("%s is %d years old.\n" % (name,age))


print("Some basic aguments:\n")
print("1: %s - String or any object with a string representation, like numbers\n")
print("Example:")

num = 5
print("Esta variable es un entero pero lo representamos con string num: %s" % num)

print("2: %d -Integers\n")
num2 = 67

print("Un entero representado por %d:" % num2)

print("3: %f - Floating point numbers\n")

num3 = 67.78
print("Numero flotante: %f" % num3)

print("4: %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.\n")
num4 = 45.12345678

print("Flotante con un numero concreto de decimales %.4f" % num4)

print("5: %x%X -Integers in hex representation (lowercase/uppercase)\n")

print("EXERCISE: You will need to write a format string which prints out the data using the following syntax:")
print("Hello John Doe. Your current balance is $53.44")

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)


