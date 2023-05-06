import os
import re

def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None 

def sanitize_filename(filename):
    """
    Sanitize a filename by replacing all non-alphanumeric characters with underscores.
    """
    return re.sub(r'[^\w\d]+', '_', filename)
