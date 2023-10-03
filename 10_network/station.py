import network
import time
import sys

ssid = "Semaphore"
psk = "Mrinal@16"

try:
    wlan = network.WLAN(network.STA_IF)#object
    wlan.active(False)#active driver
    time.sleep(1)
    wlan.active(True)
#    networks = wlan.scan()# nearby network scan
 #   print(networks)
    wlan.connect(ssid,psk)
    timeout = 10
    t=0
    while (timeout-t > 0)and(wlan.isconnected() == False):
        print(t)
        t+=1
        time.sleep(1)
    if wlan.isconnected()==True:
        print("connected with wifi")
        print(wlan.ifconfig())
    else:
        print("TimOUT , could not connect")
except Exception as e:
    print(f"Error > {e}")
sys.exit()
    
        
