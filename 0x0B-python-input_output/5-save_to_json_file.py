#!/usr/bin/python3
import json
"""converts and stores python obj to json file"""

def save_to_json_file(my_obj, filename):
    """saves python object to json file in json format"""

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
