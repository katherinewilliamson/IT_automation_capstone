#! /usr/bin/env python3

import requests
import sys
import os

try:
    directory = sys.argv[1]
except IndexError:
    raise Exception("No directory provided")
    pass

url = input("Provide destination address\n")

success = 0
fail = {}

for file in os.listdir(directory):
    filepath = os.join.path(directory, file)
    with open(filepath, "rb") as openfile:
        response = requests.post(url, files={'file': openfile})
    if response.ok:
        print(f"POST request successful for {file}")
        success += 1
    else:
        print(f"POST request failed for {file}, status code {response.status_code}")
        fail[file] = response.status_code

print(f"Complete. Successfully processed {success} out of {len(os.listdir(directory))} files")
if len(list(fail.keys())) > 0:
    print("List unsuccessful file(s)? (Y/N)")
    answer = input()
    if answer.lower == "y":
        for item, code in fail.items():
            print(f"{item} - Status code {code}")
            