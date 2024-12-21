import machine
import time

# Initialize the onboard LED (commonly on GPIO 2 for ESP32 boards)
led = machine.Pin(2, machine.Pin.OUT)

# Blink loop
while True:
    led.value(1)  # Turn LED on
    time.sleep(0.5)  # Wait for 0.5 seconds
    led.value(0)  # Turn LED off
    time.sleep(2.5)  # Wait for 0.5 seconds
