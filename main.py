import time
import board
import pulseio
from adafruit_motor import servo

# Note - As of now, for a lack of identical continuous rotation servos, two different models are being used for testing.
# There is the FITEC FS90R continuous rotation servo (from the Engineering III box) and the FEETECH FT90R continuous
# rotation servo (from the Dr. Shields' summer camp).

# Create PWMOut objects on pins A2 and A4.
pwm_1 = pulseio.PWMOut(board.A2, frequency=50)
pwm_2 = pulseio.PWMOut(board.A4, frequency=50)

# Create servo objects from those PWMOut objects.
servo_1 = servo.ContinuousServo(pwm_1)
servo_2 = servo.ContinuousServo(pwm_2)

Servo_Wait_Time = 10 + time.time()
Print_Time = 2 + time.time()
Message_Time = 1

while True:

    Remaining_Servo_Wait = Servo_Wait_Time - time.time()

    if Print_Time - time.time() <= 0:
        print("Time until servo turn: " + str(Remaining_Servo_Wait))
        Print_Time = time.time() + 2

# Note - The original code for turning the servos (unrevised):

# if Remaining_Servo_Time <= 0:  # (==) does not work.
#   print("Servos are turning.")
#   servo_1.throttle = 0.1
#   servo_2.throttle = -0.1
#   time.sleep(1)
#   servo_1.throttle = 0.
#   servo_2.throttle = -0.
#   Servo_Wait_Time = time.time() + 10

# Note - The revised code for turning the servos. It uses two if statements two set a time duration for the servos to
# turn. It was chosen because a time.sleep() command makes it so that the code basically does nothing for one second,
# whereas the revised code allows for other actions to happen.

    if Remaining_Servo_Wait <= 0:  # (==) does not work.

        if Message_Time == 1:
            print("The servos are turning.")
            Message_Time = 0

        servo_1.throttle = 0.1
        servo_2.throttle = -0.1
        # The servos will be facing each other. For them to turn the food wheel in one direction, they
        # must turn opposite directions.

    if Remaining_Servo_Wait <= -3:
        servo_1.throttle = 0.
        servo_2.throttle = -0.
        Message_Time = 1
        Servo_Wait_Time = time.time() + 10
        Print_Time = time.time() + 2
