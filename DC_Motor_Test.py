import RPi.GPIO as GPIO
import time

ENA = 18
IN1 = 23
IN2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

GPIO.output(ENA, GPIO.HIGH)

try:
    print("FORWARD TEST: IN1 HIGH, IN2 LOW")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(8)

    print("STOP")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(3)

    print("REVERSE TEST: IN1 LOW, IN2 HIGH")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    time.sleep(8)

    print("STOP")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

finally:
    GPIO.cleanup()
