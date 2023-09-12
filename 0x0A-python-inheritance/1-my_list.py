#!/usr/bin/python3
# 1-my_list.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
       return print(sorted(self))
