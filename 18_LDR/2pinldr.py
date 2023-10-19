import machine
import time

# Define the LDR and LED pins
LDR_PIN = machine.Pin(1, machine.Pin.IN)
LED_PIN = machine.Pin(4, machine.Pin.OUT)

while True:
    # Read the LDR value
    ldr_value = LDR_PIN.value()

    # Control the LED state based on the LDR value
    if ldr_value == 1:
        LED_PIN.on()  # Turn the LED ON when LDR detects darkness
    else:
        LED_PIN.off()  # Turn the LED OFF when LDR detects light

    # Print the LDR value to the console
    print("LDR Value:", ldr_value)

    # Sleep for a short time to avoid rapid value changes
    time.sleep(1)
