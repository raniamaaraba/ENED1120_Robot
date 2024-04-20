#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""


from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.display import Display
import time
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_A,OUTPUT_B,OUTPUT_C, MediumMotor, MoveDifferential, SpeedRPM
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.wheel import EV3Tire
import time 
from time import sleep 
from ev3dev2.display import Display

# Initialize the color sensor connected to any sensor port on the EV3 brick
color_sensor = ColorSensor(INPUT_1)
# Initialize the display
display = Display()

# Set the color sensor mode to COL-COLOR to detect colors
color_sensor.mode = 'COL-COLOR'

# Main loop to continuously read barcode
try:
    while True:
        # Read the color detected by the sensor
        color = color_sensor.color

        # Check if a color change is detected indicating a barcode
        if color == color_sensor.COLOR_BLACK:  
            # Display the detected barcode on the robot's screen
            barcode_value = color_sensor.reflected_light_intensity
            display.clear()
            display.text_grid([["Barcode: " + str(barcode_value)]])
            time.sleep(2)  # Display for 2 seconds

        # Wait for a brief moment to avoid detecting the same barcode multiple times
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program stopped by user")
