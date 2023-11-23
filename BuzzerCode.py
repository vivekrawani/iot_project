import RPi.GPIO as GPIO
import time



def beep():
  buzzPin =22
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(buzzPin, GPIO.OUT)

  def turn_on_buzzer():
    GPIO.output(buzzPin, GPIO.HIGH)

  def turn_off_buzzer():
    GPIO.output(buzzPin, GPIO.LOW)
 
  try:   
    # GPIO.output(buzzPin, True)
    turn_on_buzzer()
    time.sleep(2)
    print("errot") 
    turn_off_buzzer()
    GPIO.cleanup()
  except:
   
    GPIO.cleanup()
  

beep()