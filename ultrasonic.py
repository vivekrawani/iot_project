import RPi.GPIO as GPIO
import time
def DistanceMeasure():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    TRIG_PIN = 4
    ECHO_PIN = 17
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.5)
    GPIO.output(TRIG_PIN, True)
    time.sleep(1e-6)
    GPIO.output(TRIG_PIN, False)
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    GPIO.cleanup()
    return distance
