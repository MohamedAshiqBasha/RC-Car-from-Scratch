import RPi.GPIO as GPIO

ENA = 12   # GPIO12 -> L293D pin 1
IN1 = 5    # GPIO5  -> L293D pin 2
IN2 = 6    # GPIO6  -> L293D pin 7

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Force everything OFF
GPIO.output(ENA, GPIO.LOW)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)

GPIO.cleanup()
