#!/usr/bin/python

""" Simple hydroponics system controls.

"""

import time

import RPi.GPIO as GPIO

from config import (PUMP_PIN, LIGHTS_PIN, PUMP_DEFAULT_ON, LIGHTS_DEFAULT_ON,
                    PUMP_TIME)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(PUMP_PIN, GPIO.OUT)
GPIO.setup(LIGHTS_PIN, GPIO.OUT)

def pump_on():
    if PUMP_DEFAULT_ON:
        GPIO.output(PUMP_PIN, GPIO.LOW)
    else:
        GPIO.output(PUMP_PIN, GPIO.HIGH)

def pump_off():
    if PUMP_DEFAULT_ON:
        GPIO.output(PUMP_PIN, GPIO.HIGH)
    else:
        GPIO.output(PUMP_PIN, GPIO.LOW)

def run_pump():
    pump_on()
    time.sleep(PUMP_TIME)
    pump_off()

def lights_on():
    if LIGHTS_DEFAULT_ON:
        GPIO.output(LIGHTS_PIN, GPIO.LOW)
    else:
        GPIO.output(LIGHTS_PIN, GPIO.HIGH)

def lights_off():
    if LIGHTS_DEFAULT_ON:
        GPIO.output(LIGHTS_PIN, GPIO.HIGH)
    else:
        GPIO.output(LIGHTS_PIN, GPIO.LOW)

def cleanup():
    GPIO.cleanup()
