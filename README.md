# Simple hydroponics system #

A Raspberry-Pi based controller for a hydroponics system, turning the lights
on and off at set times of day and running the pump every hour.


## Hardware ##

### Parts list ###

1.  A pair of relays for controlling the lights and pumps.  The easiest and
    safe (but certainly not cheapest) solution is to get two "IoT Relays" from
    Digital Loggers Inc.
2.  A pump for aerating the water [and tubing---how much, which did we get?].
3.  Lamps for illuminating the plants.  We used a 5 meter Toogod red:blue 4:1
    LED roll, which gives 2.5 meters of LEDs (about 30 W) per container.
    You will also want two packs of the [15 cm connectors][led_connectors]
    for these.
4.  [IKEA TROFAST cabinet][trofast] (yes, the toy storage one), to serve as
    frame, with two matching shallow storage boxes to hold the water, two
    lids to hold the plants, and two shelves for adjustable-height lighting.
5.  Baskets for the plants.
6.  Clay pellets.


### Tools ###

1.  A 2.75" hole saw (for cutting holes in container lids).
2.  Soldering iron and solder (for soldering the LED strips).
3.  A utility knife (for stripping rubber insulation from the LED strips).
4.  Glue for the LED strips.  The Toogod strips come with adhesive on the
    backside, but it is not sufficiently strong to hold their weight for more
    than a few hours.


### Assembly ###

1.  Assemble the IKEA cabinet.
2.  Cut seven 2.75" holes in each container lid.  This is most easily done
    using a hole saw.
3.  Wash the pellets.
4.  Cut the LED roll into 14 strips of 7 segments each.  (You will have two
    segments leftover.  If you cut 7 strips, then 2 segments, and then another
    7 strips, you will not have to cut through the manufacturer's solder,
    which appears every 10th segment.)
5.  Glue 7 LED strips to the backside of each of the TROFAST shelves and
    connect them in series using the connectors.  Solder the connectors. (The
    connectors appear to work without solder at first, but in our experience
    fail after a couple of days.)


### Figures needed ###

1.  Container lid with holes cut.
2.  Assembled lighting panel, with at least one connector open to show solder
    job.
3.  Assembled lighting panel, showing the "serial" nature of the circuit.


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

The web app version requires the `apscheduler`,
[Flask](http://flask.pocoo.org/), and `rpyc`.


### Installation ###

To have access to the GPIO, we need to run the application as root, so all of
the packages must be installed into the `sudo` Python (rather than the user
Python or some virtualenv).

1.  Install Flask via `sudo pip install Flask`.
2.  Install the Advanced Python Scheduler via `sudo pip install apscheduler`.
3.  Install RPyC via `sudo pip install rpyc`.
4.  Clone this repository.


### Usage ###

After setting the values in `config.py`, run either,

1.  `sudo python main.py &` for the basic version, or,
2.  `sudo python hydroponics_server.py &`, followed by
    `sudo python webapp.py &`, for the web app version.

Don't forget to do `disown` to keep the job(s) running after you log off.


[led_connectors]: https://www.amazon.com/gp/product/B013YL51E6/
[trofast]: http://www.ikea.com/us/en/catalog/categories/series/19027/
