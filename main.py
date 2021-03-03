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
# It must be made into a micropython (.mpy) file to clear up data.

# The link to adafruit_hcsr04:
# https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py

# time.monotonic() will be tried in place of time.time().
# time.monotonic() is a float, whereas time.time() is an integer,
# so time.monotonic should hopefully be more accurate.

# Note - As of now, for a lack of identical continuous rotation servos, two different models are being used for testing.
# There is the FITEC FS90R continuous rotation servo (from the Engineering III box) and the FEETECH FT90R continuous
# rotation servo (from the Dr. Shields' summer camp).

# -------------- LCD Setup Start  --------------

i2c = board.I2C()
i2c.unlock()  # In case it was the i2c was just used, it needs to be unlocked.

device_address = None

while not i2c.try_lock():
    pass  # I do not know how to explain this.

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
lcd = LCD(I2CPCF8574Interface(device_address), num_rows=2, num_cols=16)

# -------------- LCD Setup End  --------------

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)
my_servo.angle = 0

activation_alarm = True

# It is better for alarm to be a boolean data value than a 0 or 1.

# Digital IO pins that work with PWM: 1, 2, 3, 4, 5, 7, 9, 11, 12, and 13.
# Not 0, 6, 8, and 10.

# Set the servo angle to a starting position.

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)


print("Starting Code...")

while True:

    distance = sonar.distance
    # This must be in the while True loop.

    if distance <= 12.5 and activation_alarm:
        wait = 5. + time.monotonic()
        lcd.clear()
        lcd.print("Servo Forward")
        print("Servo forward")
        my_servo.angle = 90

        if wait - time.monotonic() <= 0.:
            lcd.clear()
            lcd.print("Servo Forward")
            my_servo.angle = 0
            activation_alarm = False

    if not activation_alarm:
        alarm_wait = 20. + time.monotonic()
        print_time = 2. + time.monotonic()

        if print_time - time.monotonic() <= 0.:
            lcd.clear()
            print("Time Left" + str(round(alarm_wait - time.monotonic())))
            lcd.print("Ready in: \n")
            lcd.print(str(round(alarm_wait - time.monotonic())))
            print_time = time.monotonic() + 2.

        if alarm_wait <= 0.:
            alarm = True
