#!coding:utf-8

import go_GPIO
import time
import gpsnavi
import logging
import datetime


def landing(gps, groundalt, gogpio):
    count = 0
    while True:
        gps.gpsupdate()
        if count >= 3:
            break
        if gps.altitude() >= groundalt + 50:
            count += 1

    count = 0
    while True:
        gps.gpsupdate()
        if count >= 10:
            break
        if groundalt - 10 <= gps.altitude() <= groundalt + 10:
            count += 1
    time.sleep(30)
    gogpio.forward(20)


def travel(gps, gogpio):
    gogpio.turn()


def arrive(gps, gogpio):
    pass

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s', filename="botti"+str(time.strftime('%H-%M-%S', datetime.datetime.now().timetuple()))+'.log', level=logging.INFO)
    logging.info('Started')
    goal = []
    goal.append([141.24322166666667, 43.123041666666666])
    goal.append([139.649867, 35.705385])
    gpsport = None

    gps = gpsnavi.gpsparser(portname=gpsport, goal=goal)
    gps.gpsupdate()
    gogpio = go_GPIO.GPIO(goalpos=goal, gps=gps)
    groundalt = gps.altitude()  # 現地で計測する予定
    landing(gps, groundalt, gogpio)
    logging.info('landing finish')
    logging.info('travel start')
    travel(gps, gogpio)
    logging.info('travel finish')
    logging.info('arrive start')
    arrive(gogpio)
    logging.info('Finished')
