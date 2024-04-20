#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

#from pybricks.hubs import EV3Brick
#from pybricks.ev3devices import Motor
#from pybricks.parameters import Port
#from pybricks.robotics import DriveBase



#!/usr/bin/env python3

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
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Initialize the color sensor.
color_sensor = ColorSensor(1)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Define barcode patterns.
barcode_patterns = {
    "101": "A",
    "110": "B",
    "111": "C",
    "010": "D",
    "011": "E",
    "100": "F",
    "001": "G"
}

# Function to read barcode using color sensor.
def read_barcode():
    barcode = ""
    while len(barcode) < 3:  # Assuming barcode consists of 3 segments
        reflection = color_sensor.reflection()
        if reflection < 30:  # Black line detected
            barcode += "0"
        else:  # White space detected
            barcode += "1"
        robot.drive(30, 0)  # Adjust speed and turn as needed
    return barcode

# Function to interpret barcode pattern.
def interpret_barcode(barcode):
    if barcode in barcode_patterns:
        return barcode_patterns[barcode]
    else:
        return "Unknown"

# Main code
for lap in range(5):  # Assuming 5 laps
    ev3.speaker.beep()
    barcode = read_barcode()
    ev3.speaker.beep()
    result = interpret_barcode(barcode)
    print("Barcode:", barcode, "Result:", result)
    robot.drive(100, 0)  # Adjust speed and turn as needed for next lap

robot.stop(Stop.BRAKE)
