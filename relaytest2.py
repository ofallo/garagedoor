print(" Control + C to exit Program")

import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)    # the pin numbers refer to the board connector not the chip
GPIO.setwarnings(False)
GPIO.setup(31, GPIO.OUT)     # sets the pin input/output setting to OUT
GPIO.output(31, GPIO.HIGH)   # sets the pin output to high
GPIO.setup(33, GPIO.OUT)
GPIO.output(33, GPIO.HIGH)
GPIO.setup(35, GPIO.OUT)
GPIO.output(35, GPIO.HIGH)
GPIO.setup(37, GPIO.OUT)
GPIO.output(37, GPIO.HIGH)

try:
  while 1 >=0:
    GPIO.output(31, GPIO.LOW)   # turns the first relay switch ON
    time.sleep(.5)             # pauses system for 1/2 second
    GPIO.output(31, GPIO.HIGH)  # turns the first relay switch OFF
    GPIO.output(33, GPIO.LOW)  # turns the second relay switch ON
    time.sleep(.5)
    GPIO.output(33, GPIO.HIGH)
    GPIO.output(35, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(35, GPIO.HIGH)
    GPIO.output(37, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(37, GPIO.HIGH)
    time.sleep(.5)

except KeyboardInterrupt:     # Stops program when "Control + C" is entered
  GPIO.cleanup()               # Turns OFF all relay switches
