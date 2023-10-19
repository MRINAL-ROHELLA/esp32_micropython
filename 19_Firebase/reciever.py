#fire base real time data management
#LED control using ultrasonic distance sensor
#reciever for firebase

import machine
import network
import time
import urequests
import ujson

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Tifac-Core","Tifac@akg321#")  # Replace with your Wi-Fi SSID and password

while not wlan.isconnected():
    pass

print("Wi-Fi connected")

# Initialize onboard LED (Pin 2)
led = machine.Pin(2, machine.Pin.OUT)

# Firebase configuration
FIREBASE_URL = "https://gang-7664f-default-rtdb.firebaseio.com/"  # Replace with your Firebase URL
FIREBASE_API_KEY = "AIzaSyCpdfL3P75hXTbV01bT8P0CFrtG1jGeeQU"  # Replace with your Firebase API Key
NODE_PATH = "14"  # Node path to store button state

previous_state = -1  # Initialize to an invalid state

# Helper function to read the button state from Firebase
def read_firebase():
    auth_url = f"{FIREBASE_URL}{NODE_PATH}.json?auth={FIREBASE_API_KEY}"
    response = urequests.get(auth_url)
    data = ujson.loads(response.text)
    response.close()
    return data.get(NODE_PATH, -1)

# Main loop
while True:
    current_state = read_firebase()
    
    if current_state == 1:
        # Button press detected, toggle LED
        led.value(1)
        print("Button Pressed, LED Toggled")
    elif current_state == 0:
        led.value(0)