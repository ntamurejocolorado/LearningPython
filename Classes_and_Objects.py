print("Classes and Objects")

# Objects are an encapsulation of variables and function into a single entity.
# Objects get their variables and functions from classes.
# Classes are essentially a template to create your objects.

print(" A very basic class would look something like this: ")

class MyClass:
    variable = "Blah"

    def function(self):
        print("This is a message inside the class")

# To assign the above class(template) to an object you would do the following
myobjectx = MyClass()

# Now the variable "myobjectx" holds an object of the class "MyClass" that contains the variable
# and function defined within the class called "MyClass"

print("Accessing Object Variables")

# To access the variable inside of the newly created object "myobjectx":
#print(myobjectx.variable)

# Each object contains independent copies of the variables defined in the class.
# For instance, if we were to define another object with the "MyClass" class and then
# change the string in the variable:
myobjecty = MyClass()

myobjecty.variable = "yackity"
print(myobjectx.variable)
print(myobjecty.variable)

print("ACCESSING OBJECT FUNCTIONS")
# To access a function inside of an object you use notation similar to accessing a variable:
myobjectx.function()

print("EXERCISE CLASSES AND OBJECTS")

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()

car1.color = "red"
car1.value = 60000.00
car1.name = "Fer"

car2.name = "Jump"
car2.color = "blue"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())




