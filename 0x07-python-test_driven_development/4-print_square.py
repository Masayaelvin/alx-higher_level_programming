#!/usr/bin/python3
"this function prints a Square"

def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an interger")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an interger")
    else:
        for i in range(0, size):
            for x in range(0, size):
                print("#", end="")
            print()
