import network
import time
import sys



#ssid = "Semaphore"
#psk = "Mrinal@16"#

try:
    wlan = network.WLAN(network.AP_IF)#object
    wlan.active(False)#active driver
    time.sleep(1)
    wlan.active(True)
    wlan.config(essid="ESPSEMAPHORE" , password="mrinal54" , authmode=network.AUTH_WPA_WPA2_PSK)
except Exception as e:
    print(f"Error > {e}")
sys.exit()
    
        