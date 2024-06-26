##################################################
##################################################
##########                              ##########
##########     DISTANCE SETTINGS        ##########
##########                              ##########
##################################################
##################################################


# Distances are in centimeters
RED_LED_MAX_DISTANCE = 60
GREEN_LED_MAX_DISTANCE = 90
YELLOW_LED_MAX_DISTANCE = 150
ORANGE_LED_MAX_DISTANCE = 300


##################################################
##################################################
##########                              ##########
##########     UTRASONIC SENSOR         ##########
##########                              ##########
##################################################
##################################################

# This is the time (in seconds) given to the trigger to "settle" after switching on or off
TRIGGER_SETTLE_TIME = 0.000001

# These variables represent the pins assigned to the distance sensor
TRIG = 13
ECHO = 23
PULSE_DURATION_MULTIPLIER = 17165

##################################################
##################################################
##########                              ##########
##########     LED PIN ASSIGNMENTS      ##########
##########                              ##########
##################################################
##################################################

ORANGE_LED = 17
YELLOW_LED = 27
GREEN_LED = 22
RED_LED = 5

LED_ARRAY = [ORANGE_LED, YELLOW_LED, GREEN_LED, RED_LED]


##################################################
##################################################
##########                              ##########
##########     LED PIN ASSIGNMENTS      ##########
##########                              ##########
##################################################
##################################################

# The refresh rate when an object is detected.
ACTIVE_SLEEP_TIME = 0.1

# The refresh rate when an object HAS NOT been detected.
PASSIVE_SLEEP_TIME = 1