#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_A,OUTPUT_B,OUTPUT_C, MediumMotor, MoveDifferential, SpeedRPM
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.wheel import EV3Tire
import time 
from time import sleep 
from ev3dev2.display import Display

# Initialize color sensor and display
color_sensor = ColorSensor()
screen = Display()

# Define parameters in inches
y1_distance = 0.5
y_distance = 2
STUD_CM = 0.8
# Convert studs to centimeters
WHEEL_DISTANCE = 16 * STUD_CM
COORDINATE_Y1 = y1_distance * 2.54 * 8
COORDINATE_Y = y_distance * 2.54 * 8

# Threshold value to determine black and white
THRESHOLD = 1.5

mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3Tire, WHEEL_DISTANCE)

# Function to read barcode
def read_barcode():
    barcode = ''
    print("Scanning barcode...")
    for _ in range(4):
        # Use odometry to drive to specific coordinates
        print("Moving robot...")
        mdiff.on_for_distance(SpeedRPM(40), -COORDINATE_Y1)
    
        # Stop the robot
        mdiff.stop()

        # wait one second
        time.sleep(1)
        # Read the color of the current bar
        color = color_sensor.color

        # Determine whether the color is black or white
        if color > THRESHOLD:
            barcode += 'W'  # White
        else:
            barcode += 'B'  # Black

    print("Scanned barcode:", barcode)
    return barcode

# Function to display barcode on screen
def display_barcode(barcode):
    print("Displaying barcode on screen:", barcode)
    screen.clear()
    screen.text_grid([barcode], text_size=60)  # Increase text size
    start_time = time.time()  # Get the current time
    while time.time() - start_time < 10:  # Display for 10 seconds
        screen.update()
        sleep(5)  # Add a short delay to avoid flickering

# Function to display barcode type on screen with larger text size and longer duration
def display_barcode_type(barcode_type):
    print("Displaying barcode type on screen:", barcode_type)
    screen.clear()
    screen.text_grid([barcode_type], text_size=60)  # Increase text size
    start_time = time.time()  # Get the current time
    while time.time() - start_time < 10:  # Display for 10 seconds
        screen.update()
        sleep(5)  # Add a short delay to avoid flickering
   
# Function to determine barcode type
def determine_barcode_type(barcode):
    print("Determining barcode type for:", barcode)
    if barcode == 'BWWW':
        return 'Box Type 1: B W W W'
    elif barcode == 'BWBW':
        return 'Box Type 2: B W B W'
    elif barcode == 'BBWW':
        return 'Box Type 3: B B W W'
    elif barcode == 'BWWB':
        return 'Box Type 4: B W W B'
    else:
        return 'Unknown'

# Define the input barcode
input_barcode = 'BWWW'  # Example input barcode, you can change this

# Read the barcode from the color sensor
scanned_barcode = read_barcode()

# Display the scanned barcode
display_barcode(scanned_barcode)


# Display all information on the screen
screen.clear()
screen.text_grid("Scanned barcode:", scanned_barcode, "Barcode Type:", scanned_barcode, text_size=15)
start_time = time.time()  # Get the current time
while time.time() - start_time < 10:  # Display for 10 seconds
    screen.update()
    sleep(1000)  # Add a short delay to avoid flickering
