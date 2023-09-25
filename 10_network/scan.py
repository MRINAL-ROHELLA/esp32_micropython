import network
import time
import sys

try:
    wlan = network.WLAN(network.STA_IF)#object
    wlan.active(False)#active driver
    time.sleep(1)
    wlan.active(True)
    networks = wlan.scan()# nearby network scan
    print(networks)
except Exception as e:
    print(f"Error > {e}")
sys.exit()