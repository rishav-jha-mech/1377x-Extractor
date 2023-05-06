import os
import re
from vars import OUTPUT_FOLDER
import json

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

def postProcessToJson(filePath):
    print('\nPOST PROCESSING TO JSON ....\n')
    with open(filePath, 'r') as file:
        contents = file.read()

    modified_contents = re.sub(r'\[|\]', '', contents)
    modified_contents = '[' + modified_contents.replace('\n', ',') + '{}]'
    modified_contents = modified_contents.replace(',{}', '')

    with open(filePath, 'w') as file:
        file.write(modified_contents)

def checkAndCreateFolder(folderName):
    try:
        if os._exists(folderName):
            return
        os.mkdir(folderName)
    except Exception as e:
        pass