import RPi.GPIO as GPIO
import time

ENA = 18  # GPIO18 -> L293D pin 1
IN1 = 23  # GPIO23 -> L293D pin 2
IN2 = 24  # GPIO24 -> L293D pin 7

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

try:
    # Enable the channel
    GPIO.output(ENA, GPIO.HIGH)

    # Forward for 3 seconds
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(3)

    # Stop 1 second
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(1)

    # Backward for 3 seconds
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    time.sleep(3)

    # Stop
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

finally:
    GPIO.cleanup()
