import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


GPIO_PIN1 = 5
GPIO_PIN2 = 6

GPIO.cleanup()

GPIO.setup(GPIO_PIN1, GPIO.OUT)
GPIO.output(GPIO_PIN1, GPIO.LOW)
GPIO.setup(GPIO_PIN2, GPIO.IN)
GPIO.setup(25, GPIO.IN)

while True:
    
    input_state = GPIO.input(GPIO_PIN2)
    print(input_state)
    input1 = GPIO.input(25)

    print("6", input_state, "25", input1)
    
    try:
        if input_state == GPIO.LOW:
            print('Button Pressed')
        
    except KeyboardInterrupt:
        print("Exit")
        GPIO.cleanup()
    time.sleep(1)




