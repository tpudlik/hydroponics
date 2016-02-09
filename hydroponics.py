#!/usr/bin/python

""" Simple hydroponics system controls.  Defines a class Hydroponics which can
be used to turn the pump and lights on and off.
    
Both the pump and lights are controlled by relays connected to Raspberry Pi
GPIO pins.  These relays may be "default on" (device is turned on when GPIO
pin is set to low) or "default off" (device is turned off when GPIO pin is
set to low).
    
You should always use the Python 'with' statement when creating an instance of
the Hydroponics class to ensure that GPIO pins are properly cleaned up if an
exception occurs.  Since the system is usually set up to operate indefinitely
from the time it is set up, an exception is the only way for it to terminate!
Cleaning up after the class is critical, since otherwise a 3V3 GPIO signal
will continue being sent on one or both pins; this may damage any other
component connected to the pin.  An example of proper syntax is in the "if
__name__ == '__main__'" block at the end of the module.

The class constructor takes five keyword arguments, all required:
    pump_pin : int
        The number of the GPIO pin controlling the pump, in the BOARD
        numbering scheme (i.e., the number on the GPIO header).
    lights_pin : int
        The number of the GPIO pin controlling the lights.
    pump_default_on : bool
        Is the pump on or off when the GPIO pin is set to low?
    lights_default_on : bool
        Are the lights on or off when the GPIO pin is set to low?

"""

import time
import RPi.GPIO as GPIO


class HydroponicsController(object):
    """Object for controlling hydroponics setup.  See module docstring for
    more details.

    """
    def __init__(self, **kwargs):
        self.pump_pin = kwargs["pump_pin"]
        self.lights_pin = kwargs["lights_pin"]
        self.pump_default_on = kwargs["pump_default_on"]
        self.lights_default_on = kwargs["lights_default_on"]

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pump_pin, GPIO.OUT)
        GPIO.setup(self.lights_pin, GPIO.OUT)

    def pump_on(self):
        if self.pump_default_on:
            GPIO.output(self.pump_pin, GPIO.LOW)
        else:
            GPIO.output(self.pump_pin, GPIO.HIGH)

    def pump_off(self):
        if self.pump_default_on:
            GPIO.output(self.pump_pin, GPIO.HIGH)
        else:
            GPIO.output(self.pump_pin, GPIO.LOW)

    def run_pump(self, pump_time):
        """Run the pump for `pump_time` seconds."""
        self.pump_on()
        time.sleep(pump_time)
        self.pump_off()

    def lights_on(self):
        if self.lights_default_on:
            GPIO.output(self.lights_pin, GPIO.LOW)
        else:
            GPIO.output(self.lights_pin, GPIO.HIGH)

    def lights_off(self):
        if self.lights_default_on:
            GPIO.output(self.lights_pin, GPIO.HIGH)
        else:
            GPIO.output(self.lights_pin, GPIO.LOW)

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        GPIO.cleanup()


class MockHydroponicsController(object):
    """Test object with the same interface as HydroponicsController, but
    with methods that print to console instead of accessing the GPIO.

    """
    def __init__(self, **kwargs):
        self.pump_pin = kwargs["pump_pin"]
        self.lights_pin = kwargs["lights_pin"]
        self.pump_default_on = kwargs["pump_default_on"]
        self.lights_default_on = kwargs["lights_default_on"]

        print "GPIO.setmode(GPIO.BOARD)"
        print "GPIO.setup({}, GPIO.OUT)".format(self.pump_pin)
        print "GPIO.setup({}, GPIO.OUT)".format(self.lights_pin)

    def pump_on(self):
        msg = "Pump turned on by setting pin {} to {}"
        if self.pump_default_on:
            print msg.format(self.pump_pin, "GPIO.LOW")
        else:
            print msg.format(self.pump_pin, "GPIO.HIGH")

    def pump_off(self):
        msg = "Pump turned off by setting pin {} to {}"
        if self.pump_default_on:
            print msg.format(self.pump_pin, "GPIO.HIGH")
        else:
            print msg.format(self.pump_pin, "GPIO.LOW")

    def run_pump(self, pump_time):
        """Run the pump for `pump_time` seconds."""
        self.pump_on()
        time.sleep(pump_time)
        self.pump_off()

    def lights_on(self):
        msg = "Lights turned on by setting pin {} to {}"
        if self.lights_default_on:
            print msg.format(self.lights_pin, "GPIO.LOW")
        else:
            print msg.format(self.lights_pin, "GPIO.HIGH")

    def lights_off(self):
        msg = "Lights turned off by setting pin {} to {}"
        if self.lights_default_on:
            print msg.format(self.lights_pin, "GPIO.HIGH")
        else:
            print msg.format(self.lights_pin, "GPIO.LOW")

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        print "GPIO.cleanup()"


if __name__ == '__main__':
    kwargs = {"pump_pin": 13,
              "lights_pin": 11,
              "pump_default_on": False,
              "lights_default_on": True}
    
    with HydroponicsController(**kwargs) as h:
        print "Hit Ctrl + C to interrupt process."
        while True:
            h.lights_on()
            time.sleep(5)
            h.lights_off()
            time.sleep(5)
