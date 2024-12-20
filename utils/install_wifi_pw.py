#!/usr/bin/env python3
import time
import os
import subprocess

def main():
    # Prompt for WiFi credentials
    ssid = input("Enter WiFi SSID: ")
    password = input("Enter WiFi Password: ")

    # Create a temporary secrets file outside of the repo folder
    temp_path = "/tmp/micropython_secrets.py"
    with open(temp_path, "w") as f:
        f.write(f"WIFI_SSID = '{ssid}'\nWIFI_PASS = '{password}'\n")

    # Use mpremote (installed via pip install mpremote) to copy it to the MicroPython device
    try:
        subprocess.run(["mpremote", "cp", temp_path, ":secrets.py"], check=True)
        print("File now updated on microcontroller - contents shown below")
        time.sleep(1)
        subprocess.run(["mpremote", "cat", "secrets.py"], check=True)
    finally:
        os.remove(temp_path)

if __name__ == "__main__":
    main()


