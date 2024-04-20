

#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor

# Initialize motors and color sensor
tank = MoveTank(OUTPUT_B, OUTPUT_C)
color_sensor = ColorSensor()

# Constants
speed = 5
target_distance = 2 * 360
barcode_length = 5400

# Move from start box
tank.on_for_degrees(speed, speed, target_distance)

# Wait until color sensor detects value less than or equal to 99
while color_sensor.reflected_light_intensity > 99:
    print("ColorValue", color_sensor.reflected_light_intensity)
    tank.on(speed, speed)

# Stop at the start of the barcode
tank.off()
tank.wait_until_not_moving()

print("BARCODE READ")

# Open datalog file
with open('datalog.txt', 'w') as datalog:
    datalog.write("ColorValue\n")
    
    # Move forward while logging data
    while tank.left_motor.position < barcode_length:
        tank.on(speed * 3.2, speed * 3.2)
        datalog.write(str(color_sensor.reflected_light_intensity) + '\n')
        sleep(0.3)
        
# Close datalog file
print("Datalog closed")
