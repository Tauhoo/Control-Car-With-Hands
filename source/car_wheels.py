import time
import network
from esp import espnow
from machine import Pin

right_hand_mac_addr = '24:0A:C4:9F:50:30'
left_hand_mac_addr = '24:6F:28:50:BA:4C'
sensor_mac_addr = '24:6F:28:28:99:9C'

## initializing pin ##

left_control_pin = (Pin(2, Pin.OUT), Pin(0, Pin.OUT))

right_control_pin = (Pin(4, Pin.OUT), Pin(16, Pin.OUT))

######################

forward_direction = 1
curve_direction = 0

def byte_to_string(val, delimeter = ":"):
    return delimeter.join(["{:02X}".format(x) for x in val])

        
def set_wheel(direction, control_pin):
    if direction == -1:
        control_pin[0].value(1)
        control_pin[1].value(0)
    elif direction == 0:
        control_pin[0].value(0)
        control_pin[1].value(0)
    elif direction == 1:
        control_pin[0].value(0)
        control_pin[1].value(1)

def receive_right_hand_callback(data):
    direction = data['direction']
    print("right",direction)
    global forward_direction
    forward_direction = direction
    
def receive_left_hand_callback(data):
    direction = data['direction']
    print("left",direction)
    global curve_direction
    curve_direction = direction

def receive_sensor_callback(data):
    direction = data['direction']
    print("sensor",direction)
    global forward_direction
    if direction == 0:
        forward_direction = direction

def receive_callback(*dobj):
    mac, msg = dobj[0]
    sender_mac_addr = byte_to_string(mac)
    try:
        data = eval(msg)
    except:
        return
    
    if sender_mac_addr == right_hand_mac_addr:
        receive_right_hand_callback(data)
    elif sender_mac_addr == left_hand_mac_addr:
        receive_left_hand_callback(data)
    elif sender_mac_addr == sensor_mac_addr:
        receive_sensor_callback(data)
        
def set_all_wheels(left_control_pin, right_control_pin):
    global forward_direction
    global curve_direction
    
    left_pin = forward_direction
    right_pin = forward_direction
    
    if curve_direction == 1:
        right_pin = 0
    elif curve_direction == -1:
        left_pin = 0
    
    set_wheel(left_pin, left_control_pin)
    set_wheel(right_pin, right_control_pin)
    
    

## initializing network##
    
w = network.WLAN()
w.active(True)
espnow.init()
espnow.on_recv(receive_callback)

##################

while True:
    set_all_wheels(left_control_pin, right_control_pin) 
