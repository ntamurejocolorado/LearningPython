# NUMPY ARRAYS
print("Numpy arryas")

print("Example 1: Primero creamos dos listas en python. Segundo, importamos numpy  y creamos numpy arrays fuera de las listas")

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print("Element-wise calculations")

# Con numpy se pueden hacer operaciones muy rapidas con grandes numeros de elementos.

print("Calculate bmi con los pesos y alturas anteriores")
# Calcula de cada uno de los elementos por separado su bmi es decir
# es lo mismo que si hacemos un bucle y vamos leyendo cada elemento
# de la lista de height, hacemos su cuadrado y luego, dividimos el indice
# correspondiente del peso entre ese valor.
# Mientras que numpy lo hace en una sola linea lo de todos de forma infiviual.

bmi = np_weight / np_height ** 2

print(bmi)

print("Subsetting")
# Se pueden hacer subconjuntos. Por ejemplo, si queremos saber
# el bmi del array que son mayores de 23, rapidamente podemos hacer.

# For a boolean response
bmi > 23

# Print only those observations above 23
bmi[bmi>23]

print("EXERCISE:")

weight_kg_exercise = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
# Create a numpy array np_weight_kg from weight_kg
np_weight_kg_array = np.array(weight_kg_exercise)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg_array * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)















