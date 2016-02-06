"""Run the hydroponics system."""

import schedule
import time

from hydroponics import run_pump, lights_on, lights_off, cleanup

schedule.every().hour(run_pump)
schedule.every().day.at("6:00").do(lights_on)
schedule.every().day.at("23:00").do(lights_off)

if __name__ == '__main__':
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    finally:
        cleanup()
