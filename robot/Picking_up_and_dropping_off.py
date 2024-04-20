#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
my_motor = Motor(Port.D)
color_sensor = ColorSensor(Port.C)
    
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
#Add code here 


# it is going to be a lift 
#moves motor 200 rpm for 5 sec




#color sensor 

while True:
    if color_sensor.color() == Color.Black:
        robot.drvie(100,35)
        my_motor.run_target(50,50,then=stop.HOLD,wait=true)
    else:
        robot.straight(967.5)






