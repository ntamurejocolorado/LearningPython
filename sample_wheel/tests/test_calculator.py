#!/usr/bin/env python

"""Tests for sample_wheel package."""

from sample_wheel.Calculator import Calculator

def main():
    print("Test for Calculator class")
    calc = Calculator()
    resultado = calc.suma(4,5)
    print(f'La suma es: {resultado}')




if __name__ == '__main__':
    main()
    
