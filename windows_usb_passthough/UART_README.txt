The two common flavors of UART drivers for the ESP32, depending on the USB-to-UART chip used on the development board, are:

1. Silicon Labs CP210x
Chip: CP2102, CP2104, or similar variants.
Driver: Silicon Labs provides official drivers for the CP210x series.
Platforms:
Native support in most Linux distributions.
Requires driver installation for macOS and Windows (download from the Silicon Labs website).
Common Use:
Widely used in development boards like ESP32 DevKitC and others.
Driver Identifier (e.g., in Linux): /dev/ttyUSBx.
2. FTDI FT232
Chip: FT232R, FT231X, or similar FTDI UART chips.
Driver: FTDI provides Virtual COM Port (VCP) drivers.
Platforms:
Native support in most Linux distributions.
Requires driver installation for macOS and Windows (download from the FTDI website).
Common Use:
Found in certain ESP32 boards, particularly higher-end ones or older designs.
Driver Identifier (e.g., in Linux): /dev/ttyUSBx.
Other Less Common UART-to-USB Chips:
CH340/CH341:

Commonly found in inexpensive ESP32 clone boards.
Drivers may need manual installation on macOS and Windows (available from the WCH website).
Driver Identifier: /dev/ttyUSBx.
Prolific PL2303:

Occasionally found on some ESP32 boards.
Drivers are provided by Prolific Technology (Prolific website).
How to Determine Your UART Chip:
Check Board Specifications:

Most boards specify the USB-to-UART chip used.
Inspect the Chip:

Look for labels like CP210x, FT232, CH340, or PL2303 on the USB-to-UART chip.
Identify the Driver in Your OS:

Linux: Use dmesg | grep tty after connecting the board.
Windows: Check the device in Device Manager.
macOS: Use ioreg -p IOUSB or check /dev/tty.*.
Summary:
The two most common drivers are:

Silicon Labs CP210x.
FTDI FT232.
Other options like CH340 or PL2303 are less frequent but can appear in some boards.