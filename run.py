#! /usr/bin/env python3

import requests
import os
import sys
import re

try:
    directory = sys.argv[1]
except IndexError:
    raise Exception("No directory path provided")


url = input("Provide destination address:\n")

fields = []
fieldNumber = int(input("Enter amount of expected fields in the file to be processed.\n"))
for x in range(1, fieldNumber+1):
    field = input(f"Name for field {x}:\n")
    fields.append(field)

success = 0
failed = {}

def processFile(file):
    failed = ()
    filePath = os.path.join(directory, file)
    with open(filePath, "r") as openFile:
        parsedData = openFile.readlines()
    requestData = {}
    for index, field in enumerate(fields):
        try:
            requestData[field] = parsedData[index]
        except IndexError:
            continue
    # take this out later for general use
    matchedWeight = re.search(r"\d*", requestData["weight"])
    processedWeight = int(matchedWeight[0])
    requestData["weight"] = processedWeight
    fileName, ext = os.path.splitext(file)
    requestData["image_name"] = fileName+".jpeg"
    response = requests.post(url, json=requestData)
    if response.ok:
        print(f"Request completed successfully for {file}")
        return 0
    else:
        code = response.status_code
        print(f"Request failed for file {file} with status code {code}")
        failed = (file, code)
        return failed

fileList = os.listdir(directory)
for file in fileList:
    processStatus = processFile(file)
    if processStatus == 0:
        success += 1
    else:
        failed[processStatus[0]] = processStatus[1]

print(f"Successfully processed {success} of {len(fileList)} files.")
if len(fileList) != success:
    answer = input("List failed files? (Y/N)\n")
    if answer.lower() == "y":
        for item, code in failed.items():
            print(f"{item} - Status code {code}")
