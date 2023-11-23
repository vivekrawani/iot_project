import RPi.GPIO as GPIO
import time


def switch_signal():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    input_state = GPIO.input(6)
    return input_state


# while True:
#     input_state = GPIO.input(6)
#     if input_state == False:
#         print('Button Pressed')
#         time.sleep(0.3)
