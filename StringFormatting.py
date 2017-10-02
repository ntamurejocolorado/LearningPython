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

print("------------------------------------------------------------")
print(" Basic String Operations ")

# Strings are bits of text. They can be defined as anything between quotes.

astring = "Hello World!"
astring2 = 'Hello world!'

# You can also use single quotes to assign a string. However, you will face
# problems if the value to be assigned itself contains single quotes.
# For example to assign the string in these bracket(single quotes are '') you
# need to use double quotes only like this.

astring3 = "Hello world!"
print("Single quotes are '' ")

print(len(astring3))

# That prints out 12, because "Hello world|" is 12 characters long, including
# punctuation and spaces.

print(astring3.index("o")) # That prints out 4, because the location of the first occurrence of the letter "o" is 4 character
                           # away from the firs character. Notice how there are actually
                           # two o's in the phrase - this method only recognizes the first.

# But why didn't it print out 5? Isn't "o" the fifth character in the string?
# To make things more simple, Python (and most other programming languages)
# start things at 0 instead of 1. So the index of "o" is 4.

print(astring3.count("l")) # Cuenta el numero de l que hay en el string.
print(astring3.count("L")) # Diferencia entre mayúsculas y minúsculas

print(astring3[3:7]) #imprime los caracteres situados entre los indices 3 al 7 incluidos los espacios.
print(astring3[:7]) # muestra desde el principio hasta ese indice.
print(astring3[3:]) # muestra desde el 3 hasta el final.

print(astring3[-3:]) # un indice negativo empieza desde atrás.

print(astring3[3:7:2]) # This prints the caracters of string from 3 to 7 skipping one caracter.
                        # This is extended slice syntax. The general form is
                        # [start:stop:step]

# There is no function like STRREV in C to reverse a string.
# But with the above mentioned type of slice syntax you can easily
# reverse a string like this
print(astring3[::-1]) # muestra !dlrow olleH

print(astring3.upper())
print(astring3.lower())

# This is used to determine whether the string stars with something or ends with something.
# The first one will print True, as the string starts with "Hello".
print(astring3.startswith("Hello")) # si empieza por hello devolverá true
# The second one will print False, as the string certainly does not end with "asdfasdfasdf"
print(astring3.endswith("asdfasdfasdf")) # si termina en esto devolvera true si no false.

# This splits the string into a bunch of strings grouped together in a list.
# Since this example splits at a space, the first item in the list will
# be "Hello", and the second will be "world!"

afewwords = astring3.split(" ")
print(afewwords)

# EXERCISE
# Try to fix the code to print out the correct information by changing the string.
print("--------------------------------------------------------------------------")

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))







