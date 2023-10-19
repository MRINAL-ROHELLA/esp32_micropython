import machine
import time

# Define the LDR module and LED pins
LDR_PIN = machine.Pin(17, machine.Pin.IN)
LED_PIN = machine.Pin(17, machine.Pin.OUT)
led = machine.PWM(LED_PIN, freq=1000)

while True:
    # Read the LDR value
    ldr_value = LDR_PIN.value()

    # Control the LED state based on the LDR value
    if ldr_value == 0:
        led.duty(1023)  # Turn the LED on
        print("LED IS ON")
    else:
        led.duty(0)     # Turn the LED off
        print("LED IS OFF")
    # Print the LDR value to the console
    print("LDR Value:", ldr_value)

    # Sleep for a short time to avoid rapid value changes
    time.sleep(1)
