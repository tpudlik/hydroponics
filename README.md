# Simple hydroponics system #

A Raspberry-Pi based controller for a hydroponics system, turning the lights
on and off at set times of day and running the pump every hour.


## Hardware ##

### Parts list ###

1.  Raspberry Pi with a charger.
2.  A pair of relays for controlling the lights and pumps.  An easy and safe
    (but certainly not cheapest) solution is to get two
    ["IoT Relays" from Digital Loggers Inc.][IoT_relays].
3.  Ribbon cable and matching header for the Raspberry Pi GPIO, for connecting
    the relays.
4.  A pump, tubing, and valves for aerating the water.  We used,
    *   [Tetra 77851 Whisper Air Pump, 10-Gallon][pump]
    *   [PENN PLAX Standard Airline Tubing, 25-Feet][tubing]
    *   [Jardin Plastic Air Connectors][valves]
    *   [Uxcell Airstones][airstones]
5.  Lamps for illuminating the plants.  We used a
    [5 meter Toogod red:blue 4:1 LED roll][led_roll], which gives 2.5 meters
    of LEDs (about 30 W) per container.  You will also want two packs of the
    [15 cm connectors][led_connectors] for these, and a
    [power supply][led_power_supply].
6.  [IKEA TROFAST cabinet][trofast] (yes, the toy storage one), to serve as
    frame, with two matching shallow storage boxes to hold the water, two
    lids to hold the plants, and two shelves for adjustable-height lighting.
7.  [Baskets for the plants][plant_baskets], approximately 3" in maximum
    diameter.  Each TROFAST box can hold 8 baskets, for a total of 16.
8.  [Clay pellets][clay_pellets].
9.  Liquid plant food.
10. Seeds to plant and [starter plug][starter_plug] to germinate the seeds
    before transferring them to the hydroponics setup.  Or, seedlings to
    place directly in the setup.


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
3.  Cut the LED roll into 14 strips of 7 segments each.  (You will have two
    segments leftover.  If you cut 7 strips, then 2 segments, and then another
    7 strips, you will not have to cut through the manufacturer's solder,
    which appears every 10th segment.)
4.  Glue 7 LED strips to the backside of each of the TROFAST shelves and
    connect them in series using the connectors.  Solder the connectors. (The
    connectors appear to work without solder at first, but in our experience
    fail after a couple of days.)
5.  Wire the electronics.
    *   Plug the LED power supply into a relay driven by the Pi's pin 11.
    *   Plug the pump power supply into a relay driven by the Pi's pin 13.
6.  Glue an airstone to the center of each container box.
7.  Assemble the aeration system: split the output of the pump into two tubes
    using the air connectors, then connect each tube to an airstone.
8.  Wash the pellets and use them to steady the seedlings (still on their 
    pieces of starter plug!) in the baskets.
9.  Fill the storage boxes with a mixture of water and plant food, cover them
    with the lids, and place the baskets in their holes.


### Figures needed ###

1.  Container lid with holes cut.
2.  Assembled lighting panel, with at least one connector open to show solder
    job.
3.  Assembled lighting panel, showing the "serial" nature of the circuit.
4.  Circuit diagram for the wiring?


## Software ##

There are two versions of the software.

1.  The basic version runs the pump and lights on a schedule, but does not
    provide any convenient interface for suspending operation.
2.  The web app version provides a Flask web application, accessible from the
    browser, which allows you to turn off the lights and stop running the
    pump for a period of time ("quiet mode"), and then resumes regular
    programming.


### Dependencies ###

The basic version depends only on `apscheduler`, the
[Advanced Python Scheduler](https://apscheduler.readthedocs.org/en/latest/).

The web app version requires the `apscheduler`,
[Flask](http://flask.pocoo.org/), and
[RPyC](https://rpyc.readthedocs.org/en/latest/).


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
    `sudo python webapp.py &`, for the web app version.  The web app will be
    served at port 5000 by default.

Don't forget to do `disown` to keep the job(s) running after you log off.


[airstones]: https://www.amazon.com/gp/product/B00NQ8C8P8/
[clay_pellets]: https://www.amazon.com/gp/product/B004IAM29K/
[IoT_relays]: https://www.amazon.com/gp/product/B00WV7GMA2/
[led_connectors]: https://www.amazon.com/gp/product/B013YL51E6/
[led_power_supply]: https://www.amazon.com/gp/product/B013I01P5M/
[led_roll]: https://www.amazon.com/gp/product/B00XHRYX2O/
[plant_baskets]: https://www.amazon.com/gp/product/B00UZ0Q4TG/
[pump]: https://www.amazon.com/gp/product/B0009YJ4N6/
[starter_plug]: https://www.amazon.com/gp/product/B00168EO48/
[trofast]: http://www.ikea.com/us/en/catalog/categories/series/19027/
[tubing]: https://www.amazon.com/gp/product/B0002563MW/
[valves]: https://www.amazon.com/gp/product/B0089L3OIW/
