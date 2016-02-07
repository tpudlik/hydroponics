"""The Flask web application serving an interface for entering quiet mode.
"""

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from config import (PUMP_PIN, LIGHTS_PIN, PUMP_DEFAULT_ON, LIGHTS_DEFAULT_ON,
                    PUMP_TIME, LIGHTS_TIME_ON, LIGHTS_TIME_OFF)
from hydroponics import MockHydroponicsController


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    kwargs = {"pump_pin": PUMP_PIN,
              "lights_pin": LIGHTS_PIN,
              "pump_default_on": PUMP_DEFAULT_ON,
              "lights_default_on": LIGHTS_DEFAULT_ON}
    
    with MockHydroponicsController(**kwargs) as h:
        # TO DO: I should name jobid's here, so that I can pause and resume
        # them later as needed.
        scheduler.add_job(h.run_pump, 'interval', hours=1, args=(PUMP_TIME,))
        scheduler.add_job(h.lights_on,  'cron', hour=LIGHTS_TIME_ON)
        scheduler.add_job(h.lights_off, 'cron', hour=LIGHTS_TIME_OFF)
        scheduler.start()

        # This makes the scheduler and HydroponicsController objects
        # accessible from requests
        app.config["scheduler"] = scheduler
        app.config["hydroponics"] = h

        try:
            app.run(host='0.0.0.0')
        finally:
            print "Shutting down scheduler."
            scheduler.shutdown()
