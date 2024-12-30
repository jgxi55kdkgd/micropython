#!/usr/bin/env python3
# installs the WiFi SSID and password into the secrets.py file on the ESP32

import time
import os
import subprocess
import sys
import re


def main():
    # Default USB value
    usb_val = "u0"

    # Check if an argument is provided
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if re.match(r"^u[0-9]$", arg):
            usb_val = arg
        else:
            print("Error: Argument must match the pattern 'u[0-9]'.")
            sys.exit(1)

    # Prompt for WiFi credentials
    ssid = input("Enter WiFi SSID: ")
    password = input("Enter WiFi Password: ")

    # Create a temporary secrets file outside of the repo folder
    temp_path = "/tmp/micropython_secrets.py"
    with open(temp_path, "w") as f:
        f.write(f"WIFI_SSID = '{ssid}'\nWIFI_PASS = '{password}'\n")

    # Use mpremote (installed via pip install mpremote) to copy it to the MicroPython device
    try:
        subprocess.run(
            ["mpremote", usb_val, "cp", temp_path, ":secrets.py"], check=True
        )
        print(f"File now updated on microcontroller {usb_val} - contents shown below")
        time.sleep(1)
        subprocess.run(["mpremote", usb_val, "cat", "secrets.py"], check=True)
    finally:
        os.remove(temp_path)


if __name__ == "__main__":
    main()
