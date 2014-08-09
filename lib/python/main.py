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


def run():
    logging.basicConfig(format='%(asctime)s %(message)s', filename="botti"+str(time.strftime('%H-%M-%S', datetime.datetime.now().timetuple()))+'.log', level=logging.INFO)
    logging.info('Started')
    goal = []
    goal.append([141.24322166666667, 43.123041666666666])
    goal.append([139.649867, 35.705385])  # 現地で計測する予定
    gpsport = None
    ratio = 3  #１秒で３°回転すると仮定
    rate = 0.1 #１秒で 0.1m 前進すると仮定
    gps = gpsnavi.gpsparser(portname=gpsport, goal=goal)
    gps.gpsupdate()
    gps.goalcalc()
    gogpio = go_GPIO.GPIO(goalpos=goal, gps=gps, ratio=ratio)
    groundalt = gps.altitude()  # 現地で計測する予定
    goalazimath = gps.goalazimath()
    fazimath = gps.goalazimath()
    gapazimath = gps.goalazimath() - fazimath
    goalverticaldistance = gos.goalverticaldistance()
    turn_azimath = math.fads(gps.goalazimath() - gapazimath)
    landing(gps, groundalt, gogpio)
    logging.info('landing finish')
    logging.info('travel start')
    travel(gps, gogpio)
    logging.info('travel finish')
    logging.info('arrive start')
    arrive(gogpio)
    logging.info('Finished')
if __name__ == '__main__':
    run()
