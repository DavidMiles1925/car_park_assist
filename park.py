import RPi.GPIO as GPIO
import time
import os

from config import ACTIVE_SLEEP_TIME, PASSIVE_SLEEP_TIME, RED_LED_MAX_DISTANCE, GREEN_LED_MAX_DISTANCE, YELLOW_LED_MAX_DISTANCE, ORANGE_LED_MAX_DISTANCE

TRIG = 13
ECHO = 23

ORANGE_LED = 17
YELLOW_LED = 27
GREEN_LED = 22
RED_LED = 5

LED_ARRAY = [ORANGE_LED, YELLOW_LED, GREEN_LED, RED_LED]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def set_up_sensor_pins():
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)


def set_up_led_pins():

    for led in LED_ARRAY:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)



def determine_led_color(num):
    set_up_led_pins()
    if num < RED_LED_MAX_DISTANCE:
        print("RED")
        GPIO.output(RED_LED, GPIO.HIGH)
    elif num < GREEN_LED_MAX_DISTANCE:
        GPIO.output(GREEN_LED, GPIO.HIGH)
        print("GREEN")
    elif num < YELLOW_LED_MAX_DISTANCE:
        GPIO.output(YELLOW_LED, GPIO.HIGH)
        print("YELLOW")
    elif num < ORANGE_LED_MAX_DISTANCE:
        GPIO.output(ORANGE_LED, GPIO.HIGH)
        print("ORANGE")
    else:
        set_up_led_pins



def run_sensor():
    distance = 0

    while True:
            if distance > 200:
                time.sleep(PASSIVE_SLEEP_TIME)
            else:
                time.sleep(ACTIVE_SLEEP_TIME)

            GPIO.output(TRIG, True)

            time.sleep(0.00001)

            GPIO.output(TRIG, False)

            while GPIO.input(ECHO)==0:
                pulse_start = time.time()

            while GPIO.input(ECHO)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17165

            distance = round(distance, 1)

            os.system("clear")
            print ('Distance:',distance,'cm')
            determine_led_color(distance)


if __name__ == "__main__":
    try:
        set_up_sensor_pins()
        set_up_led_pins()
        
        run_sensor()

    except KeyboardInterrupt:
        GPIO.cleanup() 
        print("\nDone")


