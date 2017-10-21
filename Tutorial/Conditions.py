# Conditions

# Python uses boolean variables to evaluate conditions.
x = 2
print(x == 2) # prints out True
print( x == 3) # prints out False
print( x < 3) # prints out True

# "and" y "or" boolean operators allow building complex boolean expressions

name = "Noelia"
age = 28

if name == "Noelia" and age == 28:
    print("Your name is %s and you are also % d years old" %(name,age))

if name == "Noelia" or name == "Victor":
    print("Your name is either %s or Victor" % name)


# The "in" operator could be used to check if a specified objects exists within an iterable object.

name2 = "Victor"
if name2 in ["Victor","Rick"]:
    print("Your name is Victor or Rick")

if name2 is "Noelia":
    print("Ok, es Noelia")
elif name2 is"Victor": # else if
    print("Ok, es Victor")
else:
    print("No es ni Victor ni Noelia")
#
# if <statement is="" true="">:
#     <do something="">
#     ....
#     ....
# elif <another statement="" is="" true="">: # else if
#     <do something="" else="">
#     ....
#     ....
# else:
#     <do another="" thing="">
#     ....
#     ....
# </do></do></another></do></statement>


# The operator "is"

# Unlike the double equals operator " == " the "is" operator doesn't match the values of the variables
# but the instances themselves.

x = [1,2,3]
y = [1,2,3]

print(x == y) #prints out True

print( x is y) # print out False

# The operator "not"

print (not False) #prints out True

print((not False) == (False)) # prints out False

# Exercise

print("Change the variables in the first section, so that each if statement resolves as True")

number = 16
second_number = False
first_array = [1,3,2]
second_array = [1,2,]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")






















