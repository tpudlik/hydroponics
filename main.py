"""Run the hydroponics system."""

import schedule
import time

from config import LIGHTS_TIME_ON, LIGHTS_TIME_OFF
from hydroponics import run_pump, lights_on, lights_off, cleanup

schedule.every().hour.do(run_pump)
schedule.every().day.at(LIGHTS_TIME_ON).do(lights_on)
schedule.every().day.at(LIGHTS_TIME_OFF).do(lights_off)

if __name__ == '__main__':
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    finally:
        cleanup()
