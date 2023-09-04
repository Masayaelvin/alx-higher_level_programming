#!/usr/bin/python3
def add_integer(a, b=98):
    '''defines addition of 2 intergers'''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    
    return int(a) + int(b)
