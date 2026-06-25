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
    print("Test 1: IN1 HIGH, IN2 LOW")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(5)

    print("Stop")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(2)

    print("Test 2: IN1 LOW, IN2 HIGH")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    time.sleep(5)

    print("Stop")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

finally:
    GPIO.cleanup()
