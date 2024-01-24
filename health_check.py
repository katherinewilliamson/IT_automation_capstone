#!/usr/bin/env python3

import subprocess
import sys
import socket
import emails
try:
    import psutil
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psutil'])
    import psutil

def checkCPU():
    cpuPercentage = psutil.cpu_percent(interval=1)
    if cpuPercentage > 80:
        error = "Error - CPU usage is over 80%"
        return error
    else:
        return None


def checkHost():
    try:
        resolvedAddress = socket.gethostbyname("localhost")
        if resolvedAddress != "127.0.0.1":
            raise socket.error
        return None
    except socket.error:
        error = "Error - localhost cannot be resolved to 127.0.0.1"
        return error

def checkMemory():
    memory = psutil.virtual_memory()
    threshold = 500 * 1024 * 1024
    if memory.available <= threshold:
        error = "Error - Available memory is less than 500MB"
        return error
    else:
        return None
    
def checkDisk():
    diskUsage = psutil.disk_usage('/')
    if diskUsage.percent >= 80:
        error = "Error - Available disk space is less than 20%"
        return error
    else:
        return None

def reportError(message):
    sender = "automation@example.com"
    recipient ="username@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    email = emails.generate_email(sender, recipient, message, body)
    emails.send_email(email)

if __name__ == "__main__":
    errorMessages = []
    cpuError = checkCPU()
    if cpuError:
        errorMessages.append(cpuError)
    hostError = checkHost()
    if hostError:
        errorMessages.append(hostError)
    memoryError = checkMemory()
    if memoryError:
        errorMessages.append(memoryError)
    diskError = checkDisk()
    if diskError:
        errorMessages.append(diskError)
    if errorMessages:
        for error in errorMessages:
            reportError(error)