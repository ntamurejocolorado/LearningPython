print("PANDAS BASICS")
print("-------------")
print("Pandas DataFrames")

# Pandas is a high-level data manipulation tool developed by Wes McKinney.
# It's built on the Numpy package and its key data structure is called the DataFrame.
# DataFrames allow you to store and manipulate tabular data in rows of observations
# and columns of variables.

print("Several ways to create a DataFrame")
print("On way is to use a dictionary:")

dict = {"country": ["Brazil","Rusia","India","China","South Africa"],
        "capital": ["Brasilia","Moscow","New Dehli","Beijin","Pretoria"],
        "area": [8516,1710,3286,9597,1221],
        "population":[200.4,143.5,1252,1357,52.98]}

import pandas as pd

brics = pd.DataFrame(dict) # Coloca las key (country,capital...) en columnas y su contenido en filas.
print(brics)

# Pandas ha asignado a cada key como valores numeros del 0-4.
# Si queremos tener indices diferentes, por ej, las dos letras de cada pais:
# Set the index for brics

brics.index =["BR","RU","IN","CH","SA"]

# Print out brics with new index values

print(brics)

print("============================================================")
print("Second way to use a DataFrame: It's importing a csv file using Pandas")

# Import the cars.csv data: cars
# cars = pd.read_csv('cars.csv')
# print(cars)

print("Indexing DataFrames")
# The easiest ways to do this is by using square bracket notation.
# You can use square brackets to select one column of the cars DataFrame.
# You can either use a single bracket or a double bracket.
# The single bracket with output a Pandas Series, while double bracket will
# output a Pandas DataFrame.

cars = pd.read_csv('cars.csv',index_col= 0)

# Print out country column as Pandas Series
print(cars['cars_per_cap'])

# Print out country column as Panda DataFrame
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap','country']])

# Print out firs 4 observations
print(cars[0:4])

print(cars[4:6])


# You can use loc and iloc
# loc: is label-based, which means that you have to specify rows and columns based on their row and columns labels.
# iloc: is integer index based, so you have to specify rows and columns by their integer index.

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])


















