import numpy as np 

class Calculator():
    """ Simple class for calculate sum, resta, multiplicacion and division """
    def __init__(self):
        print(f"Initializer Calculator")

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicador(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except:
            return "Error"