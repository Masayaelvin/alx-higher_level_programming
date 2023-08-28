#!/usr/bin/python3
# safe priting elvin

def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        while n < x:
            print("{}".format(my_list[n]), end="")
            n += 1
    except IndexError:
        break
