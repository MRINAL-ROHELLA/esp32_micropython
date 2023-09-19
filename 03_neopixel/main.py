# micropython script
# Mrinal
# led blinking script
import machine
import neopixel
import time


# object for neopixel
np= neopixel.NeoPixel(machine.Pin(48),1)
delay=2
while True:
    try:
        np[0]=(255,0,0)
        np.write()
        time.sleep(0.1)
        np[0]=(0,255,0)
        np.write()
        time.sleep(0.1)
        np[0]=(0,0,255)
        np.write()
        time.sleep(0.1)
        np[0]=(255,0,255)
        np.write()
        time.sleep(0.1)
        np[0]=(255,255,0)
        np.write()
        time.sleep(0.1)
        np[0]=(0,255,255)
        np.write()
        time.sleep(0.1)
        #np[0]=(200,100,0)
        #np.write()
        #time.sleep(2)
        #np[0]=(100,0,100)
        #np.write()
        #time.sleep(5)
    except KeyboardInterrupt:
        print("EXIT!!!")
        break
    