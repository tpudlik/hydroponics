"""The Flask web application serving an interface for entering quiet mode.
"""

import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, redirect, url_for, render_template, flash

from config import (PUMP_PIN, LIGHTS_PIN, PUMP_DEFAULT_ON, LIGHTS_DEFAULT_ON,
                    PUMP_TIME, LIGHTS_TIME_ON, LIGHTS_TIME_OFF)
from hydroponics import MockHydroponicsController


# HACK These app attributes keeps track of whether quiet mode has been
# engaged.
app = Flask(__name__)
app.secret_key = "SJDFAIVCMAIOEJEOGKATBKPFK"
app.QUIET_MODE = False
app.RESUME_TIME = None
app.RESUME_JOB = None

@app.route('/')
def welcome_page():
    # TO DO: Allow extending the current pause without unpausing
    if app.QUIET_MODE:
        return render_template("welcome_page_quiet.html", resume=app.RESUME_TIME)
    else:
        return render_template("welcome_page.html")

@app.route('/pause', methods=['POST'])
def pause_page():
    pause_duration = request.form["duration"]
    app.RESUME_TIME = get_resumption_time(pause_duration)

    app.QUIET_MODE = True

    app.config["hydroponics"].lights_off()
    app.config["hydroponics"].pump_off()
    
    for job in app.config["scheduler"].get_jobs():
        job.pause()
    app.RESUME_JOB = app.config["scheduler"].add_job(resume_jobs, 'date',
                                    run_date=app.RESUME_TIME,
                                    args=(app.config["scheduler"].get_jobs(),
                                          app.config["hydroponics"]))
    return redirect(url_for('welcome_page'))

@app.route('/unpause', methods=['POST'])
def unpause_page():
    app.RESUME_JOB.remove()
    resume_jobs(app.config["scheduler"].get_jobs(), app.config["hydroponics"])
    return redirect(url_for('welcome_page'))


def resume_jobs(jobslist, h):
    """Resume jobs, then turn lights on if they should be on."""
    app.QUIET_MODE = False

    for job in jobslist:
        job.resume()

    current_hour = datetime.datetime.now().time()
    time_on = datetime.time(LIGHTS_TIME_ON,0)
    time_off = datetime.time(LIGHTS_TIME_OFF,0)
    if current_hour > time_on and current_hour < time_off:
        h.lights_on()

def get_resumption_time(pause_duration):
    # TO DO: Perform some type of validation of pause_duration?
    pause_datetime = datetime.timedelta(minutes=int(pause_duration))
    return datetime.datetime.now() + pause_datetime


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
            app.run(host='0.0.0.0', debug=True)
        finally:
            print "Shutting down scheduler."
            scheduler.shutdown()
