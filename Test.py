from gps_output import get_coods
import RPi.GPIO as GPIO
import time
from BuzzerCode import beep


if __name__ == "__main__":  
    print(get_coods())
    beep()
    time.sleep(4)
    print("exit")
    beep()


 

