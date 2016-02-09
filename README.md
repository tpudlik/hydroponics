# Simple hydroponics system #

A Raspberry-Pi based controller for a hydroponics system, turning the lights on
and off at set times of day and running the pump every hour.


## Hardware ##

### Parts list ###

1.  A pair of relays for controlling the lights and pumps.  The easiest and
    safe (but certainly not cheapest) solution is to get two "IoT Relays" from
    Digital Loggers Inc.
2.  A pump for aerating the water.
3.  Lamps for illuminating the plants.  We used a 5 meter Toogod red:blue 4:1
    LED roll, with 2.5 meters of LEDs (about 30 W) per container.
4.  IKEA **** cabinet, to serve as frame, with matching containers with lids
    to hold the plants.
5.  Baskets for the plants [what kind did we use?]
6.  Clay pellets.

### Assembly ###

1.  Assemble the IKEA cabinet.
2.  Cut seven 2.75" holes in each container lid.  This is most easily done
    using a hole saw.


## Software ##

There are two versions of the software.

1.  The basic version runs the pump and lights on a schedule, but does not
    provide any convenient interface for suspending operation.
2.  The web app version provides a Flask web application, accessible from the
    browser, which allows you to turn off the lights and stop running the
    pump for a period of time ("quiet mode"), and then resumes regular
    programming.


### Dependencies ###

The basic version depends only on `apscheduler`, the Advanced Python
Scheduler.

The web app version requires the `apscheduler` and
[Flask](http://flask.pocoo.org/).


### Installation ###

To have access to the GPIO, we need to run the application as root, so all of
the packages must be installed into the `sudo` Python (rather than the user
Python or some virtualenv).

1.  Install Flask via `sudo pip install Flask`.
2.  Install the Advanced Python Scheduler via `sudo pip install apscheduler`.
3.  Clone this repository.


### Usage ###

After setting the values in `config.py`, run either,

1.  `sudo python main.py &` for the basic version, or,
2.  `sudo python webapp.py &` for the web app version.

Don't forget to do `disown -h %1` to keep the job running after you log off.
