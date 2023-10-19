import machine
import time
import neopixel

# Define the LDR module and LED pins
LDR_PIN = machine.Pin(1, machine.Pin.IN)
LED_PIN = machine.Pin(4, machine.Pin.OUT)
np = neopixel.NeoPixel(machine.Pin(48), 1) 

while True:
    # Read the LDR value
    ldr_value = LDR_PIN.value()

    # Control the LED state based on the LDR value
    if ldr_value == 1:
        LED_PIN.on()# Turn the LED ON when LDR detects darkness
        np[0] = (255, 0, 0)
        np.write()
    else:
        LED_PIN.off()# Turn the LED OFF when LDR detects light
        np[0] = (0, 255, 0)
        np.write()

    # Print the LDR value to the console
    print("LDR Value:", ldr_value)

    # Sleep for a short time to avoid rapid value changes
    time.sleep(1)
