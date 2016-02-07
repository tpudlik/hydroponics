#!/usr/bin/python

# Which board pin is the pump control connected to?
PUMP_PIN = 0

# Which board pin is the lights control connected to?
LIGHTS_PIN = 0

# Is the pump plugged into the normally-on socket?
PUMP_DEFAULT_ON = False

# Are the lights plugged into the normally-on socket?
LIGHTS_DEFAULT_ON = True

# How long should the pump run when engaged (in seconds)?
PUMP_TIME = 3

# At what hour should the lights turn on?  An integer 0-23.
LIGHTS_TIME_ON = 6

# At what time should the lights turn off?  An integer 0-23.
LIGHTS_TIME_OFF = 23
