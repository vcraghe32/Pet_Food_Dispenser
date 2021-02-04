import time
import board
import pulseio
from adafruit_motor import servo

# time.monotonic() will be tried in place of time.time().
# time.monotonic() is a float, whereas time.time() is an integer,
# so time.monotonic should hopefully be more accurate.

# Note - As of now, for a lack of identical continuous rotation servos, two different models are being used for testing.
# There is the FITEC FS90R continuous rotation servo (from the Engineering III box) and the FEETECH FT90R continuous
# rotation servo (from the Dr. Shields' summer camp).

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

while True:

    Remaining_Servo_Wait = Servo_Wait_Time - time.monotonic()

    if Remaining_Servo_Wait > 0.:

        if Print_Time - time.monotonic() <= 0.:
            print("Time until servo turn: " + str(round(Remaining_Servo_Wait)))
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
            # if Message_Time == True is not correct. The above way is.
            # If the code was supposed to be if Message_Time == False, then
            # if not Message_Time would be used.
            print("The servos are turning.")
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
