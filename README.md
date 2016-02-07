# Simple hydroponics system #

A Raspberry-Pi based controller for a hydroponics system, turning the lights on
and off at set times of day and running the pump every hour.


## Dependencies ##

Flask, `virtualenv`, and `apscheduler`.


## Installation ##

1.  Install virtualenv.
2.  Create a virtualenv `venvhydroponics` in the directory that contains
    this repository, and activate it via `. venvhydroponics/bin/activate`.
3.  Install Flask via `pip install Flask`.
4.  Install the Advanced Python Scheduler via `pip install apscheduler`.
5.  `sudo apt-get install python-dev`
6.  `pip install RPi.GPIO` (it's on the RPi default Python, but not in the
    virtualenv).  Makes me wonder if the venv is worth the trouble.



## Usage ##

After setting the values in `config.py`, run `sudo python main.py`.
