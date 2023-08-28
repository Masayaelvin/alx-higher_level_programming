#!/usr/bin/python3
#elvin interger

def safe_print_integer(value):
    try:
        interger = int(value)
        print("{:d}".format(interger))
        return True
    except ValueError TypeError:
        return False
