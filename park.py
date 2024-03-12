import RPi.GPIO as GPIO
import time
import os

# These values are all imported from config.py.
# See that file for descriptions.
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


##################################################
## Functions are listed in alphabetical order.  ##
##################################################

# Visually indicate that the program has started successfully.
def bounce_leds(number):
    for x in range(number):
        for led in LED_ARRAY:
            GPIO.output(led, GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(led, GPIO.LOW)

        for led in reversed(LED_ARRAY):
            GPIO.output(led, GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(led, GPIO.LOW)


# Calculates the distance from the sensor in centimeters.
def calculate_distance(pulse_start=0, pulse_end=-1):
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * PULSE_DURATION_MULTIPLIER

    distance = round(distance, 1)

    return distance


# Determines which (if any) LED should be active.
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


# Outputs the measured distance to the console.
def display_distance(distance):
    os.system("clear")
    print ('Distance:',distance,'cm')
    determine_led_color(distance)


# This function gathers sensor data
def run_sensor():
    try:
        distance = 0

        while True:
                if distance > ORANGE_LED_MAX_DISTANCE:
                    time.sleep(PASSIVE_SLEEP_TIME)
                else:
                    time.sleep(ACTIVE_SLEEP_TIME)

                GPIO.output(TRIG, True)

                time.sleep(0.000001)

                GPIO.output(TRIG, False)

                time.sleep(0.000001)

                while GPIO.input(ECHO)==0:
                    pulse_start = time.time()

                while GPIO.input(ECHO)==1:
                    pulse_end = time.time()

                distance = calculate_distance(pulse_start, pulse_end)

                display_distance(distance)

    except Exception as e:
        print("An error occurred in sensor function")
        print(e)


# This function sets the board mode (BCM as opposed to BOARD)
# This is how we will identify the pin numbers on the Raspberry Pi
def set_mode_and_warnings():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)


# This function uses a loop to set the pins for the LED indicators    
def set_up_led_pins():

    for led in LED_ARRAY:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)


#This function sets up the pins for the HC-SR04 ultrasonic sensor    
def set_up_sensor_pins():
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)



##################################################
##################################################
###                                            ###
###                MAIN FUNCTION               ###
###                                            ###
##################################################
##################################################


if __name__ == "__main__":
    try:
        set_mode_and_warnings()
        set_up_sensor_pins()
        set_up_led_pins()
        
        bounce_leds(3)

        run_sensor()

    except KeyboardInterrupt:
        GPIO.cleanup() 
        print("\nDone")
    
    except Exception as e:
        print(f"An error occured: {e}")



