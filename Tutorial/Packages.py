print("Modules and packages")

# Para importar un modulo en python solo hay que poner import nombreModulo

import urllib

#use it
#urllib.urlopen()

# Two very important functions come in handy when exploring modules in Python - dir and help functions

# we can look for which functions are implemented in each module by using the dir function

dir(urllib)

help(urllib.open)

# Writing Python modules is very simple. To create a module of your own, simply create a new .py file with
# the module name, and then import it using the Python file name (without the .py extension) using the import
# command.


print("Packages")

# En este ejercicio buscamos en el paquete re los miembros que empiezan por find y los mostramos ordenamos alfabeticamente.
import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))