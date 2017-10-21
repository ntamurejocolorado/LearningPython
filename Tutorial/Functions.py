# Functions

## Functions in python are defined using the block keyword "def" followed with the function's name as
# the block's name.
print("Example 1. Funtions: ")

def my_function():
    print("Hello From My Function!")

my_function()

print("Functions with arguments:")

def my_function_with_args(username,greeting):
    print("Hello, %s,From My Function!, I wish you %s" %(username,greeting))

my_function_with_args("Noelia","a great day!")

print("Functions returns values")

def sum_two_number(a,b):
    return a + b

value = sum_two_number(2,4)
print("Value sum return %d" %value)


print("------------------------------")
print("Exercise Functions:")
print("------------------------------")

# Modify this function to return a list of strings as define above

def list_benefits():
    benefits = ["More organized code","More readable code","Easier code reuse","Allowing programmers to share and connect code together"]
    return benefits

# Modify this function to concatenate to each benefit - " is a benefit of functions
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()






























