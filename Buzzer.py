import RPi.GPIO as GPIO
import time

buzzPin = 22

def turn_on_buzzer():
  GPIO.output(buzzPin, GPIO.HIGH)

def turn_off_buzzer():
  GPIO.output(buzzPin, GPIO.LOW)

def beep():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(buzzPin, GPIO.OUT)
  turn_on_buzzer()
  time.sleep(1)
  turn_off_buzzer()
  time.sleep(1)
  
if __name__ == '__main__':    
  beep()
   
