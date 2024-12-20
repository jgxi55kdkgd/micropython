import network

# Initialize the WLAN interface
wlan = network.WLAN(network.STA_IF)

if wlan.isconnected():
    print("Disconnecting from Wi-Fi...")
    wlan.disconnect()  # Disconnect from the current network
    wlan.active(False)  # Deactivate the interface
    print("Wi-Fi disconnected.")
else:
    print("Wi-Fi is already disconnected.")
