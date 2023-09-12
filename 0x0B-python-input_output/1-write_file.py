#!/usr/bin/python3
""" this function defines reading a file"""


def write_file(filename="", text=""):
    """ defines writiing a file"""
    with open(filename, 'w') as f:
        f.write(text)

    y = text
    count = 0

    for i in y:
        for x in i:
            count += 1

    return count
