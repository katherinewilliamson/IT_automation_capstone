#!/usr/bin/env python3

import psutil

cpuPercentage = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory()

threshold = 500 * 1024 * 1024
if memory.available <= threshold:
    
    
    
diskUsage = psutil.disk_usage('/')
if diskUsage.percent >= 80:
    
