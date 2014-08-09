#!coding:utf-8
import os
import sys
import math
if os.getlogin() == 'pi':
    import RPi.GPIO as IO
else:
    sys.path.append(os.path.dirname(__file__))
    from RpiTest import GPIO as IO

import go_f
import logging


class GPIO:  # GPIOをTurtleに

    def __init__(self, leftmotor=[15, 16], rightmotor=[17, 22], goalpos=[], gps=None):
        gof = go_f.getdistance()
        gof.goal = goalpos
        self.gps = gps
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        self.IO.setmode(self.IO.BCM)
        self.IO.setup(self.leftmotor[0], self.IO.OUT)
        self.IO.setup(self.leftmotor[1], self.IO.OUT)
        self.IO.setup(self.rightmotor[0], self.IO.OUT)
        self.IO.setup(self.rightmotor[1], self.IO.OUT)
        logging.info("GPIOInit")

    def forward(self): 
        self.IO.output(self.leftmotor[0], False)
        self.IO.output(self.leftmotor[1], True)
        self.IO.output(self.rightmotor[0], False)
        self.IO.output(self.rightmotor[1], True)
        self.time.sleep(0.01)
        logging.info("Forward")

    def back(self):
        self.IO.output(self.leftmotor[0], True)
        self.IO.output(self.leftmotor[1], False)
        self.IO.output(self.rightmotor[0], True)
        self.IO.output(self.rightmotor[1], False)
        self.time.sleep(0.01)
        logging.info("back")

    def left(self,azimath):
        self.start = self.time.time()
        while True :
            self.IO.output(self.leftmotor[0], True)
            self.IO.output(self.leftmotor[1], False)
            self.IO.output(self.rightmotor[0], False)
            self.IO.output(self.rightmotor[1], True)
            if self.time.time() - self.start == azimath/3: #１秒で３°回転すると仮定
                break
        self.time.sleep(0.01)
        logging.info("left")

    def right(self,azimath):
        self.start = self.time.time()
        while True:
            self.IO.output(self.leftmotor[0], False)
            self.IO.output(self.leftmotor[1], True)
            self.IO.output(self.rightmotor[0], True)
            self.IO.output(self.rightmotor[1], False)
            if self.time.time() - self.start == azimath/3: #１秒で３°回転すると仮定
                break
        self.time.sleep(0.01)
        logging.info("right")

    def y_coordinates(self):
        self.gps.gpsupdate()
        self.gps.goalcalc()
        logging.info("y_coordinates:"+self.gps.goalverticaldistance())
        return self.gps.goalverticaldistance()

    def _bump(self, before, after):
        if before == after:
            self.back(50)
            self.left(30)
            self.time.sleep(0.01)
            logging.info("bomp")
            return True
        else:
            return False

    def angle(self):
        self.gapazimath = self.gps.goalazimath() - self.fazimath
        if self.gapazimath > 0 :
            self.left(math.fads(self.gps.goalazimath()-self.gapazimath))
        elif self.gapazimath < 0 :
            self.right(math.fads(self.gps.goalazimath()-self.gapazimath))
        elif self.gapazimath == 0 :
            self.right(math.fads(self.gps.goalazimath))

    def turn(self):
        while len(self.gps.goal) > 0:  # If "len" is 0,roba is stop.
            while self.gps.goaldistance() > 30:
                while True:
                    self.y_coord = self.y_coordinates()
                    self.forward(50)
                    if not self._bump(self.y_coord, self.y_coordinates()):
                        break
                self.fazimath = self.gps.goalazimath()
                self.time.sleep(0.01)
                self.angle()
                self.time.sleep(0.01)
                self.forward(self.gps.goaldistance())
                self.time.sleep(0.01)
            self.gps.goal.pop(0)
