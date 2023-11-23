
import time
import os
import sys
import threading
import RPi.GPIO as GPIO

from gps_output import get_coods
from ultrasonic import DistanceMeasure
from B import beep
from send_email import email_alert
from text_sms import send_text
from Switch import switch_signal



email_to = '2021ugec015@nitjsr.ac.in'
subject = 'Alert !!!'
SWITCH_PIN = 6

def check_distance():
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        input_state = GPIO.input(SWITCH_PIN)
        if input_state == False:
            print('Button Pressed')
            beep()
            coodss = get_coods()
            print(coodss)
            
        time.sleep(0.2)


def check_switch():
    while True:
        k = DistanceMeasure()
        print(f"{k} cm")
        if k <= 20:
            beep()

        time.sleep(0.3)
            

if __name__ == '__main__':

    try:
        
            t1 = threading.Thread(target=check_switch)
            t2 = threading.Thread(target=check_distance)
            
            t1.start()
            t2.start()

            t1.join()
            t2.join()

            
    except KeyboardInterrupt:
        print('Interrupted')
        GPIO.cleanup()
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)



        
    