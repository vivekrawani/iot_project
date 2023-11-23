from gpiozero import DistanceSensor
import time
import os
import sys
import RPi.GPIO as GPIO

from gps_output import get_coods
from ultrasonic import DistanceMeasure
from B import beep
from send_email import email_alert


email_to = '2021ugec015@nitjsr.ac.in'
subject = 'Alert !!!'


if __name__ == '__main__':

    try:

        while True:
            k = DistanceMeasure()
            print(f"{k} cm")
            if k <= 20:
                beep()
                coodss = get_coods()
                print(coodss)
                message = f'I need your help. \nMy location is {coodss}.'
                email_alert(subject=subject, body=message, to=email_to)

            time.sleep(0.5)
        
    except KeyboardInterrupt:
        print('Interrupted')
        GPIO.cleanup()
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)



        
    