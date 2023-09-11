#!/usr/bin/python3
""" checks whether the passed values are instances of the class or subclass"""

def is_kind_of_class(obj, a_class):
   """defines the method"""
   if isinstance(obj, a_class) or issubclass(type(obj), a_class):
       return True 
   else:
       return False
