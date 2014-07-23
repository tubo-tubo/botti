#!coding:utf-8
#import serial
#import math
#import pynmea2
#from pyproj import Geod


class getdistance:

    def __init__(self):
        pass

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, value):
        self._goal = value

    @property
    def checkpoint1(self):
        return self._nowpos

    @checkpoint1.setter
    def checkpoint1(self):
        return self._nowpos

    @property
    def nowpos(self):
        return self._nowpos

    @nowpos.setter
    def nowpos(self, value):
        self._nowpos = value

    @property
    def checkpoint2(self):
        return self._nowpos

    @property
    def checkpoint(self, value):
        self._checkpoint = value

    @checkpoint.setter
    def checkpoint(self, value):
        self._checkpoint = value


class GPIO:  # GPIOをTurtleに

    import RPi.GPIO as IO

    def __init__(self, leftmotor=[15, 16], rightmotor=[17, 22]):
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        self.IO.setmode(self.IO.BCM)
        self.IO.setup(self.leftmotor[0], self.IO.OUT)
        self.IO.setup(self.leftmotor[1], self.IO.OUT)
        self.IO.setup(self.rightmotor[0], self.IO.OUT)
        self.IO.setup(self.rightmotor[1], self.IO.OUT)

    def forward(self):  # 前進
        self.IO.output(self.leftmotor[0], False)
        self.IO.output(self.leftmotor[1], True)
        self.IO.output(self.rightmotor[0], False)
        self.IO.output(self.rightmotor[1], True)

        self.time.sleep(0.1)

    def back(self):  # 後進
        self.IO.output(self.leftmotor[0], True)
        self.IO.output(self.leftmotor[1], False)
        self.IO.output(self.rightmotor[0], True)
        self.IO.output(self.rightmotor[1], False)

        self.time.sleep(0.1)

    def left(self):  # 左旋回
        self.IO.output(self.leftmotor[0], True)
        self.IO.output(self.leftmotor[1], False)
        self.IO.output(self.rightmotor[0], False)
        self.IO.output(self.rightmotor[1], True)

        self.time.sleep(0.1)

    def right(self):  # 右旋回
        self.IO.output(self.leftmotor[0], False)
        self.IO.output(self.leftmotor[1], True)
        self.IO.output(self.rightmotor[0], True)
        self.IO.output(self.rightmotor[1], False)

    def goaldistance(self):
        return self.gg.goaldist

    def goalszimace(self):
        return float(self.gg.goalaz)

    def go_check1(self):
        while True:
            if 0 < self.gc1.goalazimace <= 90:
                self.right(30)
            elif 90 < self.gc1.goalazimace <= 180:
                self.right(150)
            elif 180 < self.gc1.goalazimace <= 270:
                self.left(150)
            else:
                self.left(30)
            self.time.sleep(0.01)
            self.forward(50)
            self.time.sleep(0.01)
            if self.gc1.goalazimace > 10 and self.gc1.goalazimace < 350 and self.gc1.goaldistance > 30:
                break

    def go_check2(self):
        while True:
            if 0 < self.gc2.goalazimace <= 90:
                self.right(30)
            elif 90 < self.gc2.goalazimace <= 180:
                self.right(150)
            elif 180 < self.gc2.goalazimace <= 270:
                self.left(150)
            else:
                self.left(30)
            self.time.sleep(0.01)
            self.forward(50)
            self.time.sleep(0.01)
            if self.gc2.goalazimace > 10 and self.gc2.goalazimace < 350 and self.gc2.goaldistance > 30:
                break

    def turn(self):
        while True:

            if 0 < self.gg.goalazimace <= 90:
                self.right(30)
            elif 90 < self.goalazimace <= 180:
                self.right(150)
            elif 180 < self.goalazimace <= 270:
                self.left(150)
            else:
                self.left(30)
            self.time.sleep(0.01)
            self.forward(50)
            self.time.sleep(0.01)
            if self.goalazimace > 10 and self.goalazimace < 350 and self.goaldistance > 30:
                break
