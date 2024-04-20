#!/usr/bin/env python3

import time
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_A, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3Tire
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.display import Display
from PIL import ImageFont

lcd = Display()

left_motor = LargeMotor(OUTPUT_B)
right_motor = LargeMotor(OUTPUT_A)

tank_drive = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3Tire, 13*8)

color_sensor = ColorSensor(INPUT_1)

color_values = []

reflected_light_intensity = color_sensor.reflected_light_intensity
if reflected_light_intensity >= 33:
    color_values.append(0)
elif reflected_light_intensity < 10:
    color_values.append(1)
tank_drive.on_for_distance(SpeedRPM(50), 55.10400)

eflected_light_intensity = color_sensor.reflected_light_intensity
if reflected_light_intensity >= 33:
    color_values.append(0)
elif reflected_light_intensity < 10:
    color_values.append(1)
tank_drive.on_for_distance(SpeedRPM(50), 55.10400)

eflected_light_intensity = color_sensor.reflected_light_intensity
if reflected_light_intensity >= 33:
    color_values.append(0)
elif reflected_light_intensity < 10:
    color_values.append(1)
tank_drive.on_for_distance(SpeedRPM(50), 55.10400)

eflected_light_intensity = color_sensor.reflected_light_intensity
if reflected_light_intensity >= 33:
    color_values.append(0)
elif reflected_light_intensity < 10:
    color_values.append(1)
tank_drive.on_for_distance(SpeedRPM(50), 55.10400)

lcd.clear()

font = Imagefont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)

lcd.text_pixels(str(color_values), x=0, y=0, font = font)

lcd.update()

time.sleep(10)

