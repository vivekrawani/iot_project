
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

def switch_signal():
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        input_state = GPIO.input(SWITCH_PIN)
        if input_state == False:
            print('Button Pressed')
            # beep()
            coodss = get_coods()
            print(coodss)
            message = f'I need your help. \nMy location is {coodss}.'
           # email_alert(subject=subject, body=message, to=email_to)
            #send_text(body=message)
            
        time.sleep(0.1)

def get_distance():
    while True:
        k = DistanceMeasure()
        print(f"{k} cm")
        if k <= 20:
            beep()
            coodss = get_coods()
            print(coodss)
            message = f'I need your help. \nMy location is {coodss}.'
           # email_alert(subject=subject, body=message, to=email_to)
            #send_text(body=message)
        time.sleep(0.5)


if __name__ == '__main__':
    
    try:
        while True:
           

                #message = f'I need your help. \nMy location is {coodss}.'
                #email_alert(subject=subject, body=message, to=email_to)
                # send_text(body=message)
            t1 = threading.Thread(target=get_distance)
            t2 = threading.Thread(target=switch_signal)

            t1.start()
            t2.start()

            t1.join()
            t2.join()
            

            time.sleep(0.1)
            
        
    except KeyboardInterrupt:
        print('Interrupted')
        GPIO.cleanup()
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)



        
    