Question - how do we pass through devices connected to the Windows USB port to our Docker devcontainer?

Answer below....

*** IMPORTANT - WINDOWS DOES NOT HAVE A UART DRIVER FOR ESP32 BY DEFAULT - YOU NEED TO INSTALL IT ****
If the UART chip on your esp32 is a Silicon Labs CP210x - you can download the CP210x driver from their website. 
See the other README in this folder for more details.

**** YOU MUST RUN THE "USBIPD ATTACH" COMMAND BEFORE STARTING THE DOCKER CONTAINER OR IT WILL FAIL TO START **** 

The python script in this folder is not required but I find it useful. If you prefer you can run the usbipd commands manually as listed here.

Get and install the Microsoft usbipd msi file from https://github.com/dorssel/usbipd-win/releases. Then run...
1. usbipd list (and note the hardware address of your board)
2. usbipd bind --hardware-id 10c4:ea60 (needs windows admin rights - use your own hardware id)
3. usbipd attach --wsl --hardware-id 10c4:ea60 (do NOT run with admin rights if you run vscode as another user)

You only need to bind your board once. Removing the USB device automatically detaches it.

Or...if it is easier, use the controller.py menu based script....

1. You need python installed on your windows host.

2. Get and install the Microsoft usbipd msi file from https://github.com/dorssel/usbipd-win/releases

3. The python script in this directory can be copied to your Windows docker host and run from there (eg "PS C:\Users\Me\Desktop> python .\controller.py"). 

4. Optionally - edit controller.py to add the board you are looking (use "usbipd list" on windows to identify your board).
Then edit the line that will match part of the string to your board: 
MCU_SUBSTRINGS = ("Silicon Labs CP210x", "USB-SERIAL CH340", "Arduino", "ESP32", "My New Board String")

This script in this folder automates the process of identifying and managing USB devices (specifically, microcontroller boards) through the usbipd tool on Windows. 
It searches the output of usbipd list for lines containing particular strings that identify boards such as CP210x, CH340, Arduino, or ESP32. 
Once a matching board is found, it prompts the user for actions: bind and attach; detach only; or detach and unbind.
To access the USB device in your devcontainer you need to Bind and Attach *BEFORE YOU OPEN THE DEVCONTAINER*.

The script works by:

Running "usbipd list" and parsing the “Connected:” section for a line that includes any of the target substrings (e.g., "Silicon Labs CP210x").
Determining the board’s state from the final column (Not shared, Shared, or Attached).
Prompting the user for an operation. 
"Binding and Unbinding" needs ***admin privileges*** (the script uses PowerShell with Start-Process and -Verb RunAs).
You only have to bind a board once - unless you select "unbind" it will be bound forever via its hardware address.
Whereas "Attaching and Detaching" must be done under your normal windows user account (assuming you are not admin).
If you have a different board with a new device string identifier, update the MCU_SUBSTRINGS list near the top of the script.
This ensures the script recognizes your board when it appears in usbipd list.