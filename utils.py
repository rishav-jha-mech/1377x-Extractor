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


def select_file():
    file_list = os.listdir(OUTPUT_FOLDER)
    if not file_list:
        print("No files found in the outputs directory.")
        return None

    print("Files in the output directory:")
    for i, filename in enumerate(file_list):
        print(f"{i+1}. {filename}")

    while True:
        selection = input("Enter the number of the file you want to select (or 'q' to quit): ")
        if selection.lower() == "q":
            return None

        try:
            index = int(selection) - 1
            if 0 <= index < len(file_list):
                return os.path.join(OUTPUT_FOLDER, file_list[index])
            else:
                print("Invalid file number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid file number.")
