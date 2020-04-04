# Team Title: HandOFGod

Project Title: Control Car with Hands <br/>
Subject: Embedded System (01204322) <br/>
Semister: Second <br/>
Year: 2019 <br/>

## Developer

    Mr. Kunanon Chankanasuk (6010505666)
    Mr. Thanakrit Naprasert (6010505879)
    Mr. Wachirawit Wacharak (6010506204)
    Mr. Prakrid Kanokpongsakorn (5910501992)

Student of Department of Computer Engineering, Faculty of Engineering, Kasetsart University

## Advisor

    Asst. Prof. Chaiporn Jaikaeo

## Description

At present there are many devices that can control the movement in long distances or wireless movement. So there are more people interested in it. Which most of those devices are drone, remote control car, pilotless aircraft, etc. And we are interested in making a remote control car. The Embedded System course is set to use 4 boards to develop devices for communication. And then we study and learn the equipment regarding all parts of vehicles. In the end, we concluded that we would cut off the joystick, and we replace the joystick with hand control. In the car we will be equipped accessory for each devices can communicate with each other, And enhance the safety performance of the car.

## Features

Use hands gesture to control the car instead of a joystick.

- The left hand is used to control the car's direction by The 3D tilting sensor on the glove. When you slop the left hand to the right, The car will turn right. And turn left when slop to the left.
- Forward and stop the car by opening and closing the palm of the right hand. The action can be detected by the light sensor on the right hand.
- The car can stop automatically when it encounters obstacles. the barrier can be caught by Ultrasonic Sensor. The system will stop the car when obstacles are too close.

## Source Code

In "source" directory
| filename | description |
|---------------|-----------------------------------------------|
| car_safety.py | Controlling safety system of car |
| car_wheels.py | Controlling the direction and movement of car|
| lefthand.py | Controlling the direction of car |
| righthand.py | Controlling the movement of car |

## Board Schematic

In "[schematic](https://github.com/Tauhoo/Control-Car-With-Hands/tree/master/schematic)" directory

## Equipment

     - NodeMCU ESP-32S x3 pcs
     - GY-291 ADXL345 3-axis Accelerometer Module x1 pc
     - 7805 Voltage Regulator IC 5V 1.5A TO-220 x1 pc
     - IC L293D 4.5-36Vdc 600mA Motor Driver x1 pc
     - Smart Robot Car Gear Motor with Tire 3V - 12V 1:120 x2 pcs
     - HY-SRF05 Ultrasonic Sensor Module x1 pc
     - LDR Photoresistor 10mm x1 pc
     - Ball Wheel x1 pc

## Video

[Code explaination](https://youtu.be/wOnyEVgWpVA) - Explanation of how code work.<br/>
[Project presentation](https://youtu.be/XpA377lBA1Q) - Present project concept and tools.
