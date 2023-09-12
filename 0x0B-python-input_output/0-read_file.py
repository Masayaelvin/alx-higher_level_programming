#!/usr/bin/python3
""" thie method defines reading a file"""


def read_file(filename=""):
    """defines the read text"""
    with open(filename) as f:
        x = f.read()

    return print(x, end='')
