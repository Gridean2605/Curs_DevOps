#!/usr/bin/python3
import time #Import pentru functia sleep
import platform #Import pentru info OS
import psutil #Import pentru info hardware(RAM/Disk"
from datetime import datetime #Import pentru info data

#Intervalul de timp la care se repeta executia
freq=5

#Identificare distributie linux
def get_linux_distribution():
    distribution = "N/A"
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("PRETTY_NAME"):
                    distribution = line.strip().split("=")[1].strip('"')
                    break
    except FileNotFoundError:
        distribution = "Unknown Distribution"
    return distribution


# Bucla infinită
while True:
    # Ora și data curentă
    print(f"Timestamp: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    
    # Informații despre sistemul de operare
    print(f"Operating System: {platform.system()}")
    print(f"Distribution: {get_linux_distribution()}")
    
    # Informații despre CPU
    cpu_info = platform.processor()
    print(f"CPU: {cpu_info if cpu_info else 'N/A'}")
    
    # Informații despre RAM (memorie totală și liberă)
    mem = psutil.virtual_memory()
    print(f"Memory (RAM): Total: {mem.total / (1024 ** 3):.2f} GB, Used: {mem.used / (1024 ** 3):.2f} GB, Free: {mem.available / (1024 ** 3):.2f} GB")
    
    # Informații despre Disk (spațiu total și disponibil)
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: Total: {disk.total / (1024 ** 3):.2f} GB, Used: {disk.used / (1024 ** 3):.2f} GB, Available: {disk.free / (1024 ** 3):.2f} GB")
    
    print(f"\n")
    
    # Pauză de x secunde
    time.sleep(freq)


