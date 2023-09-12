#!/usr/bin/python3
import json
""" returns json representatin of the object string"""


def to_json_string(my_obj):
    """conserts python dict to json string"""
    x = json.dumps(my_obj)

    return x
