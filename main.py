import time
import board
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.

pwm_1 = pulseio.PWMOut(board.A2, frequency=50)
pwm_2 = pulseio.PWMOut(board.A4, frequency=50)

servo_1 = servo.ContinuousServo(pwm_1)
# servo_2 = servo.ContinuousServo(pwm_2)

while True:

    print("Servos are turning.")
    servo_1.throttle = 1.0

    # servo_2.throttle = -1.0

    time.sleep(1.0)

    print("Servos are waiting.")
    servo_1.throttle = 0

    # servo_2.throttle = 0

    time.sleep(10)



