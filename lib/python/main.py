#!coding:utf-8

import go_GPIO
import time
import gpsnavi
import logging
import datetime


class Main(object):

    def __init__(self, groundalt=0, gpsport=None, gpsbaudrate=9600, maxalt=80, goal=[[139.9873791954023, 40.14224106321837], ratio=96.0, rate=0.0164):
        logging.basicConfig(format='%(asctime)s %(message)s', filename="botti"+str(time.strftime('%H-%M-%S', datetime.datetime.now().timetuple()))+'.log', level=logging.INFO)
        self.gpsdebugvalue = None
        self.maxalt = maxalt
        self.goal = goal
        self.gpsport = gpsport
        self.gpsbaudrate = gpsbaudrate
        self.groundalt = groundalt  # 現地で計測する予定
        self.ratio = ratio  # １秒で３°回転すると仮定
        self.rate = rate  # １秒で 0.1m 前進すると仮定
        self.gps = gpsnavi.gpsparser(portname=self.gpsport, goal=self.goal, baudrate=self.gpsbaudrate)
        self.gogpio = go_GPIO.GPIO(goalpos=self.goal, gps=self.gps, ratio=self.ratio, rate=self.rate)

    @property
    def gpsdebugvalue(self):
        return self._gpsdebugvalue

    @gpsdebugvalue.setter
    def gpsdebugvalue(self, val):
        self._gpsdebugvalue = val

    def landing(self):
        count = 0
        while True:
            if self._gpsdebugvalue is None:
                self.gps.gpsupdate()
            else:
                self.gps.gpsupdate(debuggpsvalue=self._gpsdebugvalue.pop(0))
            if count >= 3:
                break
            print(self.gps.altitude())
            if self.gps.altitude() >= self.groundalt + self.maxalt:
                count += 1
        count = 0
        while True:
            if self._gpsdebugvalue is None:
                self.gps.gpsupdate()
            else:
                self.gps.gpsupdate(debuggpsvalue=self._gpsdebugvalue.pop(0))
            if count >= 10:
                break
            print(self.gps.altitude())
            if self.groundalt - 10 <= self.gps.altitude() <= self.groundalt + 30:
                count += 1
        time.sleep(30)
        self.gogpio.forward(20)

    def travel(self):
        while True:
            if len(self.gps.goal) == 0:
                break
            if self._gpsdebugvalue is None:
                self.gps.gpsupdate()
            else:
                gpsval = self._gpsdebugvalue.pop(0)
                self.gps.gpsupdate(debuggpsvalue=gpsval)
            self.gps.goalcalc()
            fazimath = self.gps.goalazimath()
            goaldistance1 = self.gps.goaldistance()
            self.gogpio.forward(5)
            if self._gpsdebugvalue is None:
                self.gps.gpsupdate()
            else:
                gpsval = self._gpsdebugvalue.pop(0)
                self.gps.gpsupdate(debuggpsvalue=gpsval)
            self.gps.goalcalc()
            print(self.gps.goalazimath())
            print(fazimath)
            gapazimath = self.gps.goalazimath() - fazimath
            if self.gogpio.first(goaldistance1, self.gps.goaldistance()):
                self.gogpio.back(10)
            self.gogpio.turn(gapazimath)

    def arrive(self):
        pass

    def startjudge(self):
        while True:
            if self._gpsdebugvalue is None:
                self.gps.gpsupdate()
            else:
                self.gps.gpsupdate(debuggpsvalue=self._gpsdebugvalue.pop(0))
            if self.gps.sat_receivejudge():
                break

    def run(self):
        logging.info('Started')
        self.startjudge()
        self.landing()
        logging.info('landing finish')
        logging.info('travel start')
        self.travel()
        logging.info('travel finish')
        logging.info('arrive start')
        self.arrive()
        logging.info('Finished')

if __name__ == '__main__':
    main = Main(gpsport='/dev/ttyAMA0')
    main.run()
