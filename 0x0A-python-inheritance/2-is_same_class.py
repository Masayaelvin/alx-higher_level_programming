#!/usr/bin/python3
" defines a function that returns true if its an instance"

def is_same_class(obj, a_class):
    """this function takes 2 """
    if isinstance(obj, a_class):
        return True
    else:
        return False
