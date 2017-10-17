print("Set")

# Sets are lists with no duplicate entries.
# Let's say you want to collect a list of words used in a paragraph.
print(set("my name is Eric and Eric is my name".split()))
# split separa las palabras
print(set("my name is Eric and Eric is my name"))
# en este caso se muestran las letras por separado, si una ya está no se repite.


# Sets are powerful tool in Python since they have the ability to calculate differences
# and intersections between other sets. For example, say you have a list of participants
# in events A and B:

a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)

# To find out which members attended both events, you may use the "intersection" method:
print("Intersection")
print(a.intersection(b))
print(b.intersection(a))

# To find out which members attended only one of the events, use the "symmetric_difference" method:
print("symmetric_difference")
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# To finde out which members attended only one event and not the other, use the "difference" method:
print("Difference")
print(a.difference(b))
print(b.difference(a))

# To receive a list of all participants, use the "union" method:
print("Union")
print(a.union(b))

# In the exercise below, use the given lists to print out a set containing
#  all the participants from event A which did not attend event B.

print("Difference")
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

A = set(a)
B = set(b)

print(A.difference(B))