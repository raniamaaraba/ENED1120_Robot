#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase


# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


# Initalize the gyro sensor
gyro = GyroSensor(Port.S3)

Distance = 700

# Auto correction code
gyro.reset_angle(0)
while robot.distance() <= 700:
    correction = (0 - gyro.angle() )*2.5
    robot.drive(250,correction)
robot.stop()
left_motor.brake()
right_motor.brake()
