import RPi.GPIO as GPIO
import time
import os

from config import \
    TRIG,\
    ECHO,\
    PULSE_DURATION_MULTIPLIER,\
    ORANGE_LED,\
    YELLOW_LED,\
    GREEN_LED,\
    RED_LED,\
    LED_ARRAY,\
    ACTIVE_SLEEP_TIME,\
    PASSIVE_SLEEP_TIME,\
    RED_LED_MAX_DISTANCE,\
    GREEN_LED_MAX_DISTANCE,\
    YELLOW_LED_MAX_DISTANCE,\
    ORANGE_LED_MAX_DISTANCE


def set_mode_and_warnings():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)


def set_up_sensor_pins():
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)


    time.sleep(2)


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
        print("OFF")
        set_up_led_pins


def bounce(number):
    for x in range(number):
        for led in LED_ARRAY:
            GPIO.output(led, GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(led, GPIO.LOW)

        for led in reversed(LED_ARRAY):
            GPIO.output(led, GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(led, GPIO.LOW)


def run_sensor():
    try:
        distance = 0

        while True:
                print("loop tarted")
                if distance > ORANGE_LED_MAX_DISTANCE:
                    time.sleep(PASSIVE_SLEEP_TIME)
                else:
                    time.sleep(ACTIVE_SLEEP_TIME)

                print("true")
                GPIO.output(TRIG, True)

                time.sleep(0.00001)

                print("false")
                GPIO.output(TRIG, False)

                time.sleep(0.000001)

                print("echo 0")
                while GPIO.input(ECHO)==0:
                    pulse_start = time.time()
                    print(pulse_start)

                print("echo 1")
                while GPIO.input(ECHO)==1:
                    pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start

                distance = pulse_duration * PULSE_DURATION_MULTIPLIER

                distance = round(distance, 1)

                os.system("clear")
                print ('Distance:',distance,'cm')
                determine_led_color(distance)
    except Exception as e:
        print("An error occurred in sensor function")
        print(e)


if __name__ == "__main__":
    try:
        set_mode_and_warnings()
        set_up_sensor_pins()
        set_up_led_pins()
        
        bounce(3)

        run_sensor()

    except KeyboardInterrupt:
        GPIO.cleanup() 
        print("\nDone")


