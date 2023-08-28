#!/usr/bin/python3
# elvin bites

def safe_print_division(a, b):
    try:
        quo = a/b
    except ZeroDivisionError:
        quo = None
    finally:
        print("Inside result:{}".format(quo))
