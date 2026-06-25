import RPi.GPIO as GPIO
import time

ENA = 18   # L293D pin 1 (Enable) - PWM speed control
IN1 = 23   # L293D pin 2
IN2 = 24   # L293D pin 7

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

pwm = GPIO.PWM(ENA, 1000)   # 1000 Hz PWM
pwm.start(0)

try:
    # Forward at 60% speed
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(60)
    time.sleep(3)

    # Stop
    pwm.ChangeDutyCycle(0)
    time.sleep(1)

    # Backward at 60% speed
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(60)
    time.sleep(3)

    # Stop
    pwm.ChangeDutyCycle(0)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

finally:
    pwm.stop()
    GPIO.cleanup()
