# micropython script
# Mrinal
# led blinking script
import machine
import time

# object for led pin
led = machine.Pin(8,machine.Pin.OUT)

while True:
    try:
        led.value(not led.value())
        print("LED IS ON" if led.value() else "LED IS OFF")
        time.sleep(1)
    except KeyboardInterrupt:
        print("EXIT!!!")
        break
    