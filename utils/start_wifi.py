import network
import secrets  # Import the secrets.py file

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


