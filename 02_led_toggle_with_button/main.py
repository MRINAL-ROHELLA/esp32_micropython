# micropython script
# Mrinal
# led blinking script
import machine
import time

# object for led pin
led = machine.Pin(8,machine.Pin.OUT)
#object for button
button = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_UP)
count=1

while True:
    try:
        if button.value()==0:
            led.value(not led.value())
            print(f"LED IS ON {count}" if led.value() else f"LED IS OFF {count}")
            count=count+1
            while button.value()==0:
                time.sleep_ms(20)
        #time.sleep(1)
    except KeyboardInterrupt:
        print("EXIT!!!")
        break
    