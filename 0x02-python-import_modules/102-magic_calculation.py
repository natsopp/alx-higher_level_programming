#!/usr/bin/python3
def magic_calculation(a, b):
    add, sub = magic_calculation_102.add, magic_calculation_102.sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

# Placeholder for magic_calculation_102 module with add and sub functions
class magic_calculation_102:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def sub(a, b):
        return a - b
