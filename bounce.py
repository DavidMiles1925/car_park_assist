import RPi.GPIO as GPIO
import time
import os



ORANGE_LED = 17
YELLOW_LED = 27
GREEN_LED = 22
RED_LED = 5

LED_ARRAY = [ORANGE_LED, YELLOW_LED, GREEN_LED, RED_LED]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def set_up_led_pins():

    for led in LED_ARRAY:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)

if __name__ == "__main__":
    try:
        set_up_led_pins()
        while True:
            for led in LED_ARRAY:
                GPIO.output(led, GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(led, GPIO.LOW)

            for led in reversed(LED_ARRAY):
                GPIO.output(led, GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(led, GPIO.LOW)

    except KeyboardInterrupt:
        GPIO.cleanup()