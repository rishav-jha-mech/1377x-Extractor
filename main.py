import json
import time
import requests
from bs4 import BeautifulSoup
from options import subDataOptions, dataListOptions
from crawler import extractSubData, extractDataList
from utils import get_key_from_value, sanitize_filename, checkAndCreateFolder, select_file, postProcessToJson
from vars import OUTPUT_FOLDER, ERRORS_FOLDER, DATABASE_FOLDER
from magnetSnatcher import magnetSnatcher


def main():
    opt = int(
        input(
            """\nWelcome to X-Tractor
This is a simple web scraper for 1337x.to
Please select an option:
1. Extract sub data from a list of pages
2. Extract data from a list of pages
3. Extract magnet links from generateed .json file in outputs directory\n"""
        )
    )
    checkAndCreateFolder(OUTPUT_FOLDER)
    checkAndCreateFolder(ERRORS_FOLDER)
    checkAndCreateFolder(DATABASE_FOLDER)
    if opt == 1:
        try:
            optionNo = int(
                input(
                    f"""{json.dumps(subDataOptions(), indent=4)}\n\nSelect Category enter the number of the selected option and press enter """
                )
            )
            optionName = get_key_from_value(subDataOptions(), optionNo)
            if optionName is None:
                raise Exception("Invalid option")

            start = int(input("Enter start page: "))
            stop = int(input("Enter stop page: "))
            if start < 1 or stop < 1 or stop < start:
                raise Exception("Invalid page number")

        except Exception as e:
            print("Invalid input : ", e)
            return
        extractSubData(range(start, stop + 1), optionNo, optionName)
    elif opt == 2:
        try:
            optionNo = int(
                input(
                    f"""{json.dumps(dataListOptions(), indent=4)}\n\nSelect Category enter the number of the selected option and press enter """
                )
            )

            optionName = get_key_from_value(dataListOptions(), optionNo)
            if optionName is None:
                raise Exception("Invalid option")
            start = int(input("Enter start page: "))
            stop = int(input("Enter stop page: "))
            if start < 1 or stop < 1 or stop < start:
                raise Exception("Invalid page number")

        except Exception as e:
            print("Invalid input: ", e)
            return
        extractDataList(range(start, stop + 1), optionNo, optionName)
    elif opt == 3:
        try:
            results = []
            filePath = select_file()
            fileName = filePath.split("/")[-1]
            with open(filePath, "r") as f:
                datas = json.load(f)
            for i,data in enumerate(datas):
                print(f"Processing {i+1}/{len(datas)}")
                values = magnetSnatcher(data,fileName)
                if values is not None:
                    results.append(values)
            print("Writing to file ...")
            fileName = f'{DATABASE_FOLDER}{fileName}'
            with open(fileName, "a") as f:
                json.dump(results, f)
                f.write("\n")
        except Exception as e:
            print("Invalid input: ", e)
            return

if __name__ == "__main__":
    main()
