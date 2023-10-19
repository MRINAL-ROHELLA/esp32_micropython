import machine
import time
pir_pin = machine.Pin(18,machine.Pin.IN)
relay_pin = machine.Pin(17,machine.Pin.OUT)
def detect_motion():
  while True:
    if pir_pin.value()==1:
        print("Motion detected")
        print("Unlocking solenoid")
        relay_pin.ON()
        time.sleep(2)
    else:
        print("locking Solenoid")
        relay_pin.off()
    time.sleep(1)
    
    
if _name=="__main_":
    detect_motion()