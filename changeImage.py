#!/usr/bin/env python3

import os

import PIL
from PIL import Image
import sys

try:
    directory = sys.argv[1]
except IndexError:
    raise Exception("No directory path provided")

while True:
    try:
        x = int(input("Provide x value for intended image size\n"))
        break
    except ValueError:
        print("Invalid input")
while True:
    try:
        y = int(input("Provide y value for intended image size\n"))
        break
    except ValueError:
        print("Invalid input")
imageSize = (x,y)

fileList = os.listdir(directory)

for file in fileList:
    try:
        filename, ex = os.path.splitext(file)
        filepath = os.path.join(directory, file)
        with Image.open(filepath) as image:
            finalpath=os.path.join(directory, filename+".jpg")
            image.resize(imageSize).convert("RGB").save(finalpath, "JPEG")
    except PIL.UnidentifiedImageError:
        pass
