#! /usr/bin/env python3

import requests
import os
import sys
import re

try:
    directory = sys.argv[1]
except IndexError:
    #raise Exception("No directory path provided")
    pass
    
url = input("Provide destination address:\n")

fields = []
fieldNumber = int(input("Enter ammount of expected fields in the file to be processed.\n"))
for x in range(1, fieldNumber+1):
    field = input(f"Name for field {x}:\n")
    fields.append(field)

success = 0
failed = {}

def processFile(file):
    filePath = os.path.join(file, directory)
    with open(filepath, "r") as openFile:
        parsedData = data.readlines()
    requestData = {}
    for index, field in enumerate(fields):
        requestData[field] = parsedData[index]
    # take this out later for general use
    processedWeight = int(re.search(r"\d*", requestData["weight"]))
    requestData["weight"] = processedWeight
    fileName, ext = os.path.splitext(file)
    requestData["image_name"] = fileName+".jpg"
    response = requests.post(url, json=requestData)
    if response.ok:
        print(f"Request completed successfully for {file}")
        success += 1
    else:
        code = response.status_code
        print(f"Request failed for file {file} with status code {code}")
        failed[file] = code

fileList = os.listdir(directory)
for file in fileList:
    processFile(file)
print(f"Successfully proccessed {success} of {len(fileList)} files.")
if len(fileList) != success:
    answer = input("List failed files? (Y/N)\n")
    if answer.lower() == "y":
        for item, code in failed.items():
            print(f"{file} - Status code {code}")
            