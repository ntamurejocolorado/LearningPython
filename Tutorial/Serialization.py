print("Serialization")

# Python provides built-in JSON libraries to encode and decode JSON
# In Python 2.5, the simplejson module is used, whereas in Python 2.7, the json module
# is used. Since this interpreter uses Python 2.7, we'll be using json.
# In order to use the json module, it must first be imported:

import json
import  pickle

#print(json.load('data.json'))
with open('data.json') as json_data:
    d = json.load(json_data)
    print(d)
    json_string = json.dumps([1,2,3,"a","b","c"]) # To encode a data structure to JSON, use dumps.
    print("dumps")
    print(json_string)
    pickled_string = pickle.dumps([1,2,3,"a","r","c"])
    print("Pickle")
    print(pickle.loads(pickled_string))

# The aim of this exercise is to print out the JSON string with key-value pair "Me":800 added to it
#import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
#def add_employee(salaries_json, name, salary):
 #   salaries = json.loads(salaries_json)
  #  salaries[name] = salary

  #  return json.dumps(salaries)

# test code
# salaries = '{"Alfred" : 300, "Jane" : 400 }'
# new_salaries = add_employee(salaries, "Me", 800)
# decoded_salaries = json.loads(new_salaries)
# print(decoded_salaries["Alfred"])
# print(decoded_salaries["Jane"])
# print(decoded_salaries["Me"])
