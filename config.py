#!/usr/bin/python

# Which board pin is the pump control connected to?
PUMP_PIN = 13

# Which board pin is the lights control connected to?
LIGHTS_PIN = 11

# Is the pump plugged into the normally-on socket?
PUMP_DEFAULT_ON = False

# Are the lights plugged into the normally-on socket?
LIGHTS_DEFAULT_ON = True

# How long should the pump run when engaged (in seconds)?
PUMP_TIME = 300

# At what hour should the lights turn on?  An integer 0-23.
LIGHTS_TIME_ON = 6

# At what time should the lights turn off?  An integer 0-23.
LIGHTS_TIME_OFF = 22

# Which port should be used by the HydroponicsServer?
PORT = 18861
