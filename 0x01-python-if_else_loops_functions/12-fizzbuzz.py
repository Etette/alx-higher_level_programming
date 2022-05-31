#!/usr/bin/python3
def fizzbuzz():
    """prints from 1 to 100 separated by a space
    prints fizz for multiples of three
    prints buzz for multiples of five
    prints fizzbuzz for multiples of both three and five
    """
    for num in range(1, 100):
        if (num % 3 == 0 and num % 5 == 0):
            print("fizzbuzz ", end="")
        elif num % 3 == 0:
            print("fizz ", end="")
        elif num % 5 == 0:
            print("buzz ", end="")
        else:
            print("{}".format(num), end"")
