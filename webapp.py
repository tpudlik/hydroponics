"""The Flask web application serving an interface for entering quiet mode.

The web application communicates with an RPyC server that actually controls
the hardware.  You must start that server via,

    sudo python hydroponics_server.py &

before starting the web application.

"""

import datetime

from flask import Flask, request, redirect, url_for, render_template, flash
import rpyc

from config import PORT


app = Flask(__name__)
app.secret_key = "SJDFAIVCMAIOEJEOGKATBKPFK"

@app.route('/')
def welcome_page():
    # TODO: Allow extending the current pause without unpausing
    c = rpyc.connect("localhost", PORT)
    if c.root.is_paused():
        return render_template("welcome_page_quiet.html",
                               resume=c.root.get_resume_time())
    else:
        return render_template("welcome_page.html")

@app.route('/pause', methods=['POST'])
def pause_page():
    # TODO: Perform some type of validation of pause_duration?
    pause_duration = request.form["duration"]
    c = rpyc.connect("localhost", PORT)
    c.root.pause(pause_duration)
    return redirect(url_for('welcome_page'))

@app.route('/unpause', methods=['POST'])
def unpause_page():
    c = rpyc.connect("localhost", PORT)
    c.root.resume()
    return redirect(url_for('welcome_page'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
