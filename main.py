# This file is for micro servo code. The beginning code used a continuous rotation servo,
# but the project plan has switched to using a micro servo because micro servos are more precise.

import time
import board
import pulseio
from adafruit_motor import servo
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import LCD
import adafruit_hcsr04

# Currently, adafruit_hcsr04 is a python (.py) file and goes beyond the capacity for storage.
# It must be compiled into a micropython (.mpy) file to be more compact.

# The link to adafruit_hcsr04.py source code:
# https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py

# time.monotonic() will be tried in place of time.time().
# time.monotonic() is a float, whereas time.time() is an integer,
# so time.monotonic should hopefully be more accurate.

# Note - As of now, for a lack of identical continuous rotation servos, two different models are being used for testing.
# There is the FITEC FS90R continuous rotation servo (from the Engineering III box) and the FEETECH FT90R continuous
# rotation servo (from the Dr. Shields' summer camp).

# constants are usually UPPER CASE by convention.
TRIGGER_DISTANCE = 12.5
CYCLE_TIME = 5.0  # in seconds
TIME_BTW_FEEDS = 20.0
LCD_REFRESH_TIMER = 1.0
OPEN_ANGLE = 90.0
CLOSED_ANGLE = 0.0

# This code defines functions that are modular and reusable in future projects.

# Function to initialize the lcd driver. We hand the function an object of 'board' and it returns
# an object for the lcd that is used in the main code.
# This function could be used in any other project.
def initialize_lcd(board, rows=2, columns=16):

    print("Initializing LCD")
    i2c = board.I2C()
    i2c.unlock()  # In case it was the i2c was just used, it needs to be unlocked.

    device_address = None

    while not i2c.try_lock():
        pass  # this continues to try that command to obtain access to the i2c device, and when the device answers,
        # the i2c.try_lock() function returns True and execution can continue below.

    try:
        while not device_address:
            device_address_list = i2c.scan()
            # The i2c.scan() returns a LIST of addresses.
            # I just want the first address. So:
            device_address = device_address_list[0]
            print("I2C interface found at: ", hex(device_address))
            time.sleep(2)

    finally:
        i2c.unlock()
        i2c.deinit()
        # This releases the SCL (Serial Clock Wire) pin so that the LCD can use it.
        # I found that here:
        # https://circuitpython.readthedocs.io/en/5.3.x/shared-bindings/busio/I2C.html#busio.I2C

    # OK, now talk to the LCD at the address we just found by scanning.
    lcd = LCD(I2CPCF8574Interface(device_address), num_rows=rows, num_cols=columns)

    return lcd


def feed_cycle(duration, open_angle, closed_angle, lcd):

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


#  Initialize devices
lcd = initialize_lcd(
    board
)  # This is how to call the function that initializes the lcd.
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
my_servo = servo.Servo(pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50))
# Digital IO pins that work with PWM: 1, 2, 3, 4, 5, 7, 9, 11, 12, and 13.
# Not 0, 6, 8, and 10.

# Set the servo angle to a starting position
my_servo.angle = CLOSED_ANGLE

# Side note on Pycharm shortcuts: refactor (for renaming a variable) is shift-F6
print("Starting Main Loop...")
ready_to_feed = True
print_time = time.monotonic()
last_feed_time = time.monotonic()

while True:
    time_remaining = last_feed_time + TIME_BTW_FEEDS - time.monotonic()
    ready_to_feed = time_remaining < 0.0

    # get distance from ultrasound sensor
    try:
        distance = (
            sonar.distance
        )  # Continuously read distance every time loop executes.
    except RuntimeError:
        distance = (
            TRIGGER_DISTANCE + 1.0
        )  # This ensures that we have a value for distance if the sensor throws error.
        print("Error - object too close to the ultrasound sensor")

    if distance <= TRIGGER_DISTANCE and ready_to_feed:  # feed now
        last_feed_time = feed_cycle(
            duration=CYCLE_TIME,
            open_angle=OPEN_ANGLE,
            closed_angle=CLOSED_ANGLE,
            lcd=lcd,
        )

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
