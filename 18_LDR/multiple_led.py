import machine
import time
import neopixel

# Define the LDR module and LED pins
LDR_PIN = machine.Pin(1, machine.Pin.IN)
LED_PIN = machine.Pin(4, machine.Pin.OUT)
LED_PIN1 = machine.Pin(15, machine.Pin.OUT)
LED_PIN2 = machine.Pin(8, machine.Pin.OUT)
np = neopixel.NeoPixel(machine.Pin(48), 1)  # 1 NeoPixel LED connected to GPIO pin 13
led = machine.PWM(LED_PIN, freq=1000)
led2 = machine.PWM(LED_PIN1, freq=1000)
led3 = machine.PWM(LED_PIN2, freq=1000)

while True:
    # Read the LDR value
    ldr_value = LDR_PIN.value()
#     r = int((ldr_value / 4095) * 255)
#     g = 255 - r
#     b = 0

    # Control the LED state based on the LDR value
    if ldr_value == 0:
        led.duty(1023)# Turn the LED on
        led2.duty(1023)
        led3.duty(1023)
        np[0] = (0, 255, 0)
        np.write()
    else:
        led.duty(0)# Turn the LED off
        led2.duty(0)
        led3.duty(0)
        np[0] = (255, 0, 0)
        np.write()

    # Print the LDR value to the console
    print("LDR Value:", ldr_value)

    # Sleep for a short time to avoid rapid value changes
    time.sleep(1)

