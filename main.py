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

# The .mpy-cross program, which is linux-based, was used to convert -.py to -.mpy.

# The link to adafruit_hcsr04.py source code:
# https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py

# By convention, constant variables, meaning variables that are set to numbers that do not change,
# are usually UPPER CASE.

TRIGGER_DISTANCE = 12.5
CYCLE_TIME = 5.0
TIME_BTW_FEEDS = 6
LCD_REFRESH_TIMER = 1.0
OPEN_ANGLE = 45.
CLOSED_ANGLE = 135.
NUMBER_OF_CYCLES = 1


# A period is listed after the constant variables because they will be coupled with the time.monotonic() library, which
# is a floating point number data type.

# This code is unique from previous Engineering III coding assignments in that it uses functions that are defined in
# the main.py file. Functions are a very useful way to organize code into a series of manageable groups. They make
# code easier to understand by separating certain tasks. Each function should be designated to a specific task,
# such as initializing the LCD or moving a servo.

# Also, functions are reusable in other code files. They can be copied and pasted or called using
# "from (file) import (function)".

# The functions could also be placed in an external file and imported like a library. They are put here for
# convenience. If put in a library, such as LukeProject.py, they would be imported in this file like:
# from LukeProject import initialize_lcd, feed_cycle


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

    return LCD(I2CPCF8574Interface(device_address), num_rows=rows, num_cols=columns)
    # The return statement of a function is what it answers or hands back to the code that called it. In this case,
    # it returns the initialized lcd object. The calling code can assign that to a variable and use it later to
    # write to the LCD.


def feed_cycle(duration, open_angle, closed_angle, lcd):
    # This function opens and closes the servo while displaying LCD messages.

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
    time.sleep(2)

    return (
        time.monotonic()
    )  # As a return value, the time of the last feed cycle is handed back.


# Okay, the functions have been defined. Now, similar to how to an object is created from a library, objects will be
# created from the functions.

lcd = initialize_lcd(
    board
)  # This is how to call the function that initializes the lcd. Note that the other arguments,
# rows and columns, do not need to be specified because they are set to a default in the function. However, the defaults
# could be changed by listing one of those arguments and setting it equal to a new number.

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

my_servo = servo.Servo(pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50))
# This line of code is basically using an external function. It lists the library, then class, and then arguments of
# that class.

# Important - The Digital IO pins that work with PWM: 1, 2, 3, 4, 5, 7, 9, 11, 12, and 13.
# Digital IO pins 0, 6, 8, and 10 do not work.

# Set the servo angle to a starting position
my_servo.angle = CLOSED_ANGLE
# Note how CLOSED_ANGLE was used instead of a number because it makes the code easier to understand.

# Side note on Pycharm shortcuts: refactor (for renaming a variable) is shift-F6.

print("Starting Main Loop...")

ready_to_feed = False
print_time = time.monotonic()
last_feed_time = time.monotonic()

while True:
    time_remaining = last_feed_time + TIME_BTW_FEEDS - time.monotonic()
    # Could time.monotonic() be compounding to make the time remaining value inaccurate?

    ready_to_feed = time_remaining < 0.0
    # The above line isn't a calculation, it is an abbreviated "if" statement. The expression on the right of the equals
    # is evaluated and the result is a yes or no (True or False). This means that ready_to_feed is set of that
    # result of True or False. The line could be stated more verbosely like:

    # if time_remaining < 0.0:
    #    ready_to_feed = True
    # else:
    #    ready_to_feed = False

    # The code below gets the distance from the ultrasound sensor. This could be made into a function.
    try:
        distance = (
            sonar.distance
        )  # This continuously reads the distance measured every time the loop executes.

    except RuntimeError:
        distance = TRIGGER_DISTANCE + 1.0

        # This code is very useful, as, without it, the code enters a blocked state with a RuntimeError when the
        # ultrasonic distance reads something too close. By setting the distance to 1 more than the triggering distance
        # when there is a RuntimeError, the distance will be converted into a "safe" value that will not trigger an
        # error nor activate the code.

        print("Error - object too close to the ultrasonic distance sensor")

    if (
            print_time - time.monotonic() <= 0.0
    ):  # This prints an update of the timer status every few seconds.
        lcd.clear()

        if time_remaining > 0.0:
            print(
                "Time left: "
                + str(round(time_remaining))
                + ". Closest object: "
                + str(distance)
            )
            lcd.print("Ready in: \n")
            lcd.print(str(round(time_remaining)))

        else:
            print(
                "Ready to feed when distance sensor is triggered. Closest object: "
                + str(distance)
            )
            lcd.print("Ready\nto feed")

        print_time = (
                LCD_REFRESH_TIMER + time.monotonic()
        )  # This is the next print time.

    if distance <= TRIGGER_DISTANCE and ready_to_feed:
        # Note that the boolean (ready_to_feed) is set to true because, sensibly enough, it means that the code is ready
        # to feed. If it was activated by a variable called "not read_to_feed," that would be confusing.

        # The things on the left side of the equals signs are the variable names used in the function's arguments list.
        # The things on the right side of the equals signs are the constants that the arguments are set equal to.

        # In the code below, the range() function is set up in order to allow the dispensing cycle to be repeated if
        # necessary, in case more food must be dispensed when the pet food dispenser is activated. Also,
        # "NUMBER_OF_CYCLES" is a a constant specified at the beginning of the code file, and "counter" is a filler
        # variable that does not have to be set to a specific value.

        for counter in range(NUMBER_OF_CYCLES):
            last_feed_time = feed_cycle(
                duration=CYCLE_TIME,
                open_angle=OPEN_ANGLE,
                closed_angle=CLOSED_ANGLE,
                lcd=lcd,

            )

        # The feed_cycle function could also have no return value and just be executed without assigning any values
        # to last_feed_time. If this were the case, the code would look like:

        # feed_cycle(
        #     duration=CYCLE_TIME,
        #     open_angle=OPEN_ANGLE,
        #     closed_angle=CLOSED_ANGLE,
        #     lcd=lcd,
        # )
        # last_feed_time = time.monotonic()
        # Since we always want to know when the last feed was completed, it is more efficient to put a return value in
        # feed_cycle that gets time.monotonic() and hands it back to the calling code, where it can be assigned to a
        # variable - in this case, last_feed_time.
