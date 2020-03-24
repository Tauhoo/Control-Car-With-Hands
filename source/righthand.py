from machine import ADC, Pin
import network
from esp import espnow
import time

w = network.WLAN()
w.active(True)

light = ADC(Pin(34))
light.atten(ADC.ATTN_11DB)
light.width(ADC.WIDTH_12BIT)

BROADCAST = b'\xFF' * 6

espnow.init()
espnow.add_peer(BROADCAST)

while True:
    lumen = light.read()
    # 1 = go, 0 = stop
    if (lumen > 20):
        status = 1
    else:
        status = 0
    righthand = {"direction" : status}
    print("Light: ", lumen)
    print("Check: ", str(righthand))
    espnow.send(BROADCAST, str(righthand))
    time.sleep(0.5)