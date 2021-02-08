# This file will be used for making LCD code.

import time
import board
import pulseio
from adafruit_motor import servo
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import LCD

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

# Create PWMOut objects on pins A2 and A4.
pwm_1 = pulseio.PWMOut(board.A2, frequency=50)
pwm_2 = pulseio.PWMOut(board.A4, frequency=50)

# Create servo objects from those PWMOut objects.
servo_1 = servo.ContinuousServo(pwm_1)
servo_2 = servo.ContinuousServo(pwm_2)

Servo_Wait_Time = 10. + time.monotonic()
Print_Time = 2. + time.monotonic()
Message_Time = True
# It is better for Message_Time to be a boolean data value than a 0 or 1.

r1 = board.D1
g1 = board.D2
b1 = board.D4

# Digital IO pins that work with PWM: 1, 2, 3, 4, 5, 7, 9, 11, 12, and 13.
# Not 0, 6, 8, and 10.

myRGB1 = RGB_PWM(r1, g1, b1)

while True:

    Remaining_Servo_Wait = Servo_Wait_Time - time.monotonic()

    if Remaining_Servo_Wait > 0.:

        if Print_Time - time.monotonic() <= 0.:
            lcd.clear()
            print("Time until servo turn: " + str(round(Remaining_Servo_Wait)))
            lcd.print("Turn In: \n")
            lcd.print(str(round(Remaining_Servo_Wait)))
            Print_Time = time.monotonic() + 2.

    # Note - The original code for turning the servos (unrevised):

    # if Remaining_Servo_Time <= 0:  # (==) does not work.
    #   print("Servos are turning.")
    #   servo_1.throttle = 0.1
    #   servo_2.throttle = -0.1
    #   time.sleep(1)
    #   servo_1.throttle = 0.
    #   servo_2.throttle = -0.
    #   Servo_Wait_Time = time.time() + 10

    # Note - The revised code for turning the servos. It uses two if statements two set a time duration for the
    # servos to turn. It was chosen because a time.sleep() command makes it so that the code basically does nothing
    # for one second, whereas the revised code allows for other actions to happen.

    if Remaining_Servo_Wait <= 0.:  # (==) does not work.

        if Message_Time:
            lcd.clear()
            # if Message_Time == True is not correct. The above way is.
            # If the code was supposed to be if Message_Time == False, then
            # if not Message_Time would be used.
            print("The servos are turning.")
            lcd.print("Turn \n")
            lcd.print("Servos")
            Message_Time = False

        if not Message_Time:
            servo_1.throttle = 0.1
            servo_2.throttle = -0.1
            # The servos will be facing each other. For them to turn the food wheel in one direction, they
            # must turn opposite directions.

    if Remaining_Servo_Wait <= -3.:
        servo_1.throttle = 0.
        servo_2.throttle = -0.
        Message_Time = True
        Servo_Wait_Time = time.monotonic() + 10.
        Print_Time = time.monotonic() + 2.
