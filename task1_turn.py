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

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


# TODO: Add code here

#basic movement features below ^^

#y/2n 

#LAP 1
# 20cm for 215
# Go forward and backwards for one meter.
robot.straight(2621.28)
ev3.speaker.beep()
# Turn clockwise by 360 degrees and back again.
robot.turn(217)
ev3.speaker.beep()

robot.straight(2621.28)
ev3.speaker.beep()




#LAP 2

# 20cm for 215
# Go forward and backwards for one meter.
# Turn clockwise by 360 degrees and back again.
#robot.turn(200)
#ev3.speaker.beep()

#robot.straight(968)
#ev3.speaker.beep()



#LAP 3
# 20cm for 215
# Go forward and backwards for one meter.
# Turn clockwise by 360 degrees and back again.
#robot.turn(200)
#ev3.speaker.beep()

#robot.straight(968)
#ev3.speaker.beep()



#LAP 4
# 20cm for 215
# Go forward and backwards for one meter.
# Turn clockwise by 360 degrees and back again.
#robot.turn(200)
#ev3.speaker.beep()

#robot.straight(968)
#ev3.speaker.beep()



#LAP 5
# 20cm for 215
# Go forward and backwards for one meter
# Turn clockwise by 360 degrees and back again.
#robot.turn(200)
#ev3.speaker.beep()

#robot.straight(968)
#ev3.speaker.beep()







# Turn clockwise by 360 degrees and back again.
#robot.turn(360)
#ev3.speaker.beep()

#robot.turn(-360)
#ev3.speaker.beep()

# Go forward and backwards for one meter.
#robot.straight(1000)
#ev3.speaker.beep()

#robot.straight(-1000)
#ev3.speaker.beep()

# Turn clockwise by 360 degrees and back again.
#robot.turn(360)
#ev3.speaker.beep()

#robot.turn(-360)
#ev3.speaker.beep()