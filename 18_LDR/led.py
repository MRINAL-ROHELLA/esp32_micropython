import machine
import time
import neopixel

# Define the LDR module and LED pins
LDR_PIN = machine.Pin(1, machine.Pin.IN)
LED_PIN = machine.Pin(4, machine.Pin.OUT)
np = neopixel.NeoPixel(machine.Pin(48), 1)  # 1 NeoPixel LED connected to GPIO pin 13
led = machine.PWM(LED_PIN, freq=1000)

while True:
    # Read the LDR value
    ldr_value = LDR_PIN.value()
#     r = int((ldr_value / 4095) * 255)
#     g = 255 - r
#     b = 0

    # Control the LED state based on the LDR value
    if ldr_value == 0:
        led.duty(1023)# Turn the LED on
        np[0] = (0, 255, 0)
        np.write()
    else:
        led.duty(0)# Turn the LED off
        np[0] = (255, 0, 0)
        np.write()

    # Print the LDR value to the console
    print("LDR Value:", ldr_value)

    # Sleep for a short time to avoid rapid value changes
    time.sleep(1)
