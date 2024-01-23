#!/usr/bin/env python3

import os
import datetime
from datetime import date
import reports
import emails

def getDate():
    capturedTime = datetime.date.today()
    currentDate = capturedTime.strftime("%B %d, %Y")
    return currentDate
 
def processFiles(directory):
    contentItems = []
    for file in os.listdir(directory):
        filePath = os.path.join(directory, file)
        supplierData = {}
        fields = ["name", "weight", "description"]
        with open(filePath, "r") as currentFile:
            parsedData = currentFile.readlines()
        for index, field in enumerate(fields):
            supplierData[field] = parsedData[index]
        contentItems.append(["name: {}\nweight: {}".format(supplierData["name"], supplierData["weight"])])
    content = "<br>".join(contentItems)
    return content
        
if __name__ == "__main__":
    paragraph = processFiles(directory = "supplier-data/descriptions/")
    currentDate = getDate()
    title = f"Processed Update on {currentDate}"
    atatchment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)
    email = emails.generate_email("automation@example.com", "<username>@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", attachment)
    emails.send_email(email)
    