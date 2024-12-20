import network
import sys

try:
    import secrets
except ImportError:
    print("The 'secrets' module is not available. Run mpwifipw to ensure you have set up your Wi-Fi SSID and password first.")
    sys.exit(1)  # Exit the program if the module is not available


# Retrieve SSID and password from secrets.py
ssid = secrets.WIFI_SSID
password = secrets.WIFI_PASS

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print("Connecting to Wi-Fi...")
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass

print("Network connected:", wlan.ifconfig())
print("IP address is connected:", wlan.ifconfig()[0])


