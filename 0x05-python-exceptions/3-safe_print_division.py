#!/usr/bin/python3
# elvin bites

def safe_print_division(a, b):
    try:
        quo = a / b
        return (quo)
    except (ZeroDivisionError, TypeError):
        quo = None
        return (quo)
    finally:
        print("Inside result:{}".format(quo))
