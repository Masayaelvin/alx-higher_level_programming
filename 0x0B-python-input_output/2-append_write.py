#!/usr/bin/python3
""" function to append  file """


def append_write(filename="", text=""):
    """defines appending a file """
    with open(filename, 'a') as f:
        f.write(text)

    return len(text)
