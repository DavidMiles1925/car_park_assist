# Parkinging Assistant

## Table of Contents

[**Project Description**](#project-description)  
[**Building the Project**](#building-the-project)  
&emsp;[Diagram](#diagram)  
&emsp;[Instructional Video](#instructional-video)  
&emsp;[Installing the Code](#installing-the-code)  
[**Using the Device**](#using-the-device)  
&emsp;[Adjusting the Distance Indicators](#adjusting-the-distance-indicators)  
&emsp;[Setting Up](#setting-up)

## Project Description

![Final Product](./readme/car_park_table.png "Final Product")

This project was inspired by the small space in which we park a large van. The space between where the front of the car needs to sit to be able to close the garage, and where the car hits the wall of the garage is relatively small. This sensor was installed to give the driver a visual cue as to where exactly the front of the car is, and how far it is from the wall.

The program is set to only check for a distance every 1 second (this can be adjusted in the `config.py` file) while the distance measured is greater than 300cm (also adjustable).

---

## Building the Project

### Diagram

![Diagram](./readme/car_park_diagram.png "Car Park Assist Diagram")
![Table](./readme/car_park_table.png "Car Park Assist Table")

### Instructional Video

**Watch this video to help you build the device!**

[Link Here]()

### Installing the Code

1. If you haven't already, follow [these instructions](https://github.com/DavidMiles1925/pi_zero_setup?tab=readme-ov-file#setup-procedure) to set up your Raspberry Pi.

2. Boot your Pi, and install git:

```bash
sudo apt install git
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

3. Install the code:

```bash
git clone https://github.com/DavidMiles1925/car_park_assist
```

4. Navigate to the `car_park_assist` directory.

```bash
cd car_park_assist
```

5. Run the program and verify it is working.

```bash
python park.py
```

6. Follow these instructions to set the program to run at boot: [Run Program on Startup](https://github.com/DavidMiles1925/pi_zero_setup?tab=readme-ov-file#configure-a-program-to-run-on-startup)

---

## Using the Device

### Adjusting The Distance Indicators

1. Open the config.py file

```bash
sudo nano config.py
```

**These are the most commonly used values in the configuration file.** These varialbes control the maximum distance (in centimeters) at which that LED will indicate. The order of indication should match the order below. (Red should always be lowest, orange should always be highest.):

**`RED_LED_MAX_DISTANCE`**  
 **`GREEN_LED_MAX_DISTANCE`**  
 **`YELLOW_LED_MAX_DISTANCE`**  
 **`ORANGE_LED_MAX_DISTANCE`**

> **These variables should be left alone unless you have a firm understanding of the code.**
>
> **`ACTIVE_SLEEP_TIME`** - This controls the amount of time between distance checks while someone is actively parking.
>
> **`PASSIVE_SLEEP_TIME`** - This controls the amount of time between distance checks while no object is detected.
>
> **`TRIG`** - Sets the pin for the trigger on the ultrasonic sensor.
>
> **`ECHO`** - Sets the pin for the receiver on the ultrasonic sensor.
>
> **`PULSE_DURATION_MULTIPLIER`** - Sets the multiplier for calculating the distance from the sensor. (34330/2 = 17165)
>
> **`RED_LED`** - Sets the pin number for the orange LED indicator.
>
> **`GREEN_LED`** - Sets the pin number for the orange LED indicator.
>
> **`YELLOW_LED`** - Sets the pin number for the orange LED indicator.
>
> **`ORANGE_LED`** - Sets the pin number for the orange LED indicator.
>
> **`LED_ARRAY`** - An array of all LED values used to loop through values.

### Setting Up

Simply plug the device in to power it up. (MicroUSB port closest to the edge on the Pi Zero.)

As the car approaches the device, the lights will signal in the following order, with their meanings listed beside them:  
&emsp;Orange: The device sees you.  
&emsp;Yellow: Getting close, not in parking zone yet.  
&emsp;Green: Within parking tolerance.  
&emsp;Red: TOO CLOSE. Back up.

**If you do not see an orange light as you approach, assume the device is not working properly.**
