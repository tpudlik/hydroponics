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
PUMP_TIME = 300

# At what time should the lights turn on?  A string such as "6:00" (use 24h
# clock).
LIGHTS_TIME_ON = "6:00"

# At what time should the lights turn off?
LIGHTS_TIME_OFF = "23:00"
