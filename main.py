# This file is the code used in Violet's and Luke's pet food dispenser project.
# The code utilizes an LCD, ultrasonic distance sensor, micro servo, and an Adafruit Metro MO Express.

import time
import board
import pulseio
from adafruit_motor import servo
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import LCD
import adafruit_hcsr04

# adafruit_hcsr04.mpy instead of adafruit_hcsr04.py was needed to prevent a memory allocation error. The
# adafruit_hcsr04.mpy library can be found on the project repository:
# https://github.com/vcraghe32/Pet_Food_Dispenser/blob/main/adafruit_hcsr04.mpy

# The .mpy-cross program, which is linux-based, was used to convert -.py to .mpy.

# The link to adafruit_hcsr04.py source code:
# https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py

# By convention, constant variables, meaining variables that are set to numbers that do not change,
# are usually UPPER CASE.

TRIGGER_DISTANCE = 12.5
CYCLE_TIME = 5.0
TIME_BTW_FEEDS = 20.0
LCD_REFRESH_TIMER = 1.0
OPEN_ANGLE = 90.0
CLOSED_ANGLE = 0.0

# A period is listed after the constant variables because they will be coupled with the time.monotonic() library, which
# is a floating point number data type.

# This code is unique from previous Engineering III coding assignments in that it uses functions that are defined in
# the main.py file. Functions are a very useful way to organize code into a series of manageable groups. They make
# code easier to understand by seperating certain tasks. Each function should be designated to a specific task,
# such as initializing the LCD or moving a servo.

# Also, functions are reusable in other code files. They can be copied and pasted or called using
# "from (file) import (function)".


def initialize_lcd(board, rows=2, columns=16):

    # This function initializes the LCD.

    print("Initializing LCD")
    i2c = board.I2C()
    i2c.unlock()  # In case it was the i2c was just used, it needs to be unlocked.

    device_address = None

    while not i2c.try_lock():
        pass
        # This continues to try that command to obtain access to the i2c device, and when the device answers,
        # the i2c.try_lock() function returns True and execution can continue below.

    try:
        while not device_address:
            device_address_list = i2c.scan()
            # The i2c.scan() returns a LIST of addresses.
            # Only the first address is wanted. So:
            device_address = device_address_list[0]
            print("I2C interface found at: ", hex(device_address))
            time.sleep(2)

    finally:
        i2c.unlock()
        i2c.deinit()
        # This releases the SCL (Serial Clock Wire) pin so that the LCD can use it.
        # This can be found here:
        # https://circuitpython.readthedocs.io/en/5.3.x/shared-bindings/busio/I2C.html#busio.I2C

    # OK, now talk to the LCD at the address that was just found by scanning.

    lcd = LCD(I2CPCF8574Interface(device_address), num_rows=rows, num_cols=columns)

    return lcd


def feed_cycle(duration, open_angle, closed_angle, lcd):
    # This function opens and closes the servo while displaying LCD messages.

    # time_to_return = time.monotonic() + duration
    print("Activating feed cycle")
    lcd.clear()
    lcd.print("Servo\nForward")
    print("Servo forward")
    my_servo.angle = open_angle
    time.sleep(duration)
    lcd.clear()
    lcd.print("Servo\nBackward")
    print("Servo backward")
    my_servo.angle = closed_angle

    return time.monotonic()  # as a return value, we hand back the time of the last feed cycle


# Okay, the functions have been defined. Now, similar to how to an object is created from a library, objects will be
# created from the functions.

lcd = initialize_lcd(board)  # This is how to call the function that initializes the lcd. Note that the other arguments,
# rows and columns, do not need to be specified because they are set to a default in the function. However, the defaults
# could be changed by listing one of those arguments and setting it equal to a new number.

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

my_servo = servo.Servo(pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50))
# This line of code is basically using an external function. It lists the library then class and then arguments of that
# class. Th

# Important - The Digital IO pins that work with PWM: 1, 2, 3, 4, 5, 7, 9, 11, 12, and 13.
# Not 0, 6, 8, and 10.

# Set the servo angle to a starting position
my_servo.angle = CLOSED_ANGLE
# Note how CLOSED_ANGLE was used instead of a number because it makes the code easier to understand.

# Side note on Pycharm shortcuts: refactor (for renaming a variable) is shift-F6

print("Starting Main Loop...")

ready_to_feed = True
print_time = time.monotonic()
last_feed_time = time.monotonic()

while True:
    time_remaining = last_feed_time + TIME_BTW_FEEDS - time.monotonic()
    ready_to_feed = time_remaining < 0.0

    # Get the distance from ultrasound sensor. This could be made into a function.
    try:
        distance = (
            sonar.distance
        )  # Continuously read distance every time loop executes.
    except RuntimeError:
        distance = (
                TRIGGER_DISTANCE + 1.0
        )  # This ensures that we have a value for distance if the sensor throws error.
        print("Error - object too close to the ultrasound sensor")

    if distance <= TRIGGER_DISTANCE and ready_to_feed:
        # Note that the boolean (ready_to_feed) is set to true because, sensibly enough, it means that the code is ready
        # to feed. If it was actrivated by (not read_to_feed), that would be confusing.

        last_feed_time = feed_cycle(
            duration=CYCLE_TIME,
            open_angle=OPEN_ANGLE,
            closed_angle=CLOSED_ANGLE,
            lcd=lcd,
        )

        # The things on the left side of the equals signs are the arguments mentioned in the function.
        # THe things on the right side of the equals signs are the constants that the arguments are set eqaul to.

    if print_time - time.monotonic() <= 0.0:  # print an update of status every few seconds
        lcd.clear()
        if time_remaining > 0.0:
            print("Time left: " + str(round(time_remaining)) + ". Closest object: " + str(distance))
            lcd.print("Ready in: \n")
            lcd.print(str(round(time_remaining)))
        else:
            print("Ready to feed when distance sensor is triggered. Closest object: " + str(distance))
            lcd.print("Ready\nto feed")
        print_time = LCD_REFRESH_TIMER + time.monotonic()  # next print time
