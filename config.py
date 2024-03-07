##################################################
##################################################
##########                              ##########
##########     DISTANCE SETTINGS        ##########
##########                              ##########
##################################################
##################################################

# Distances are in centimeters

# Settings for my garage
#RED_LED_MAX_DISTANCE = 20
#GREEN_LED_MAX_DISTANCE = 28
#YELLOW_LED_MAX_DISTANCE = 100
#ORANGE_LED_MAX_DISTANCE = 200


# Settings for Dad's garage
RED_LED_MAX_DISTANCE = 20
GREEN_LED_MAX_DISTANCE = 40
YELLOW_LED_MAX_DISTANCE = 100
ORANGE_LED_MAX_DISTANCE = 200


##################################################
##################################################
##########                              ##########
##########     UTRASONIC SENSOR         ##########
##########                              ##########
##################################################
##################################################

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