import RPi.GPIO as GPIO

PUMP_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)

def control_pump(state):
    GPIO.output(PUMP_PIN, state)
