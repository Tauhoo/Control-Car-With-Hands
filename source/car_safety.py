import network
from esp import espnow
import time
import machine
import utime

w = network.WLAN()
w.active(True)

BROADCAST = b'\xFF' * 6

espnow.init()
espnow.add_peer(BROADCAST)

count = 0

while True:
  trig=machine.Pin(15, machine.Pin.OUT)
  trig.off()
  utime.sleep_us(2)
  trig.on()
  utime.sleep_us(10)
  trig.off()
  echo=machine.Pin(14, machine.Pin.IN)
  while echo.value() == 0:
    pass
  t1 = utime.ticks_us()
  while echo.value() == 1:
    pass
  t2 = utime.ticks_us()
  cm = (t2 - t1) / 58.0
  if cm <= 4:
      value = 0
  else:
      value = 1
  msg = str({'direction': value})
  print(msg)
  espnow.send(BROADCAST, msg)
  utime.sleep(1)
