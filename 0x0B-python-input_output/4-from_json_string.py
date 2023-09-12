#!/usr/bin/python3
import json
""" converts json string to python obj"""


def from_json_string(my_str):
    """ converts json string to python ob"""
    return json.loads(my_str)
