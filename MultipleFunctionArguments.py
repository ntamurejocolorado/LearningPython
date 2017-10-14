print("Multiple Function Arguments")

# Todas las funciones en Python reciben un numero de argumentos predefinidos.
# Ejemplo:
# def myfunction(first,second,third):

# Es posible declarar funciones que reciban un numero variable de argumentos,
# para ello hay que usar la siguiente sintaxis:
# def foo(first,second,third, *therest):
#     print("First:%s" %first)
#     print("Second:%s" %second)
#     print("Third:%s" % third)
#     print("And all the rest... %s" % list(therest))

# La variable THEREST es una lista de variables, la cual recibe todos los argumentos
# que vienen de foo despues del tercer argumento.

def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1,2,3,4,5)

# Es posible enviar funciones por keyword, de forma que el orden de los argumentos no importe
# usando la siguiente sintaxis.
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))



print("Example 3:")

# Rellena foo and bar para que ellas puedan recibir una variable de 3 argumentos o mas.
# Foo debe devolver los argumentos extra recibidos.
# Bar debe ser True si los keyword magicnumber es 7 y False de otro modo.

# edit the functions prototype and implementation
def foo2(a, b, c,*args):
    return len(args)


def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo2(1,2,3,4) == 1:
    print("Good.")
if foo2(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")

