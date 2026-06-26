import RPi.GPIO as GPIO
import time

ENA = 12   # GPIO12 -> L293D pin 1
IN1 = 5    # GPIO5  -> L293D pin 2
IN2 = 6    # GPIO6  -> L293D pin 7

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

try:
    print("Enable motor")
    GPIO.output(ENA, GPIO.HIGH)

    print("Forward: IN1 HIGH, IN2 LOW")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(5)

    print("Stop")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(2)

    print("Reverse: IN1 LOW, IN2 HIGH")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    time.sleep(5)

    print("Stop")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(ENA, GPIO.LOW)

finally:
    GPIO.cleanup()
