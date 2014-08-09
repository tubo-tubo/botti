#!coding:utf-8
import os
import sys
import math
import time
if os.getlogin() == 'pi':
    import RPi.GPIO as IO
else:
    sys.path.append(os.path.dirname(__file__))
    from RpiTest import GPIO as IO

import go_f
import logging


class GPIO:  # GPIOをTurtleに

    def __init__(self, leftmotor=[15, 16], rightmotor=[17, 22], goalpos=[], gps=None, ratio=3):
        gof = go_f.getdistance()
        gof.goal = goalpos
        self.gps = gps
        self.ratio = ratio
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        IO.setmode(IO.BCM)
        IO.setup(self.leftmotor[0], IO.OUT)
        IO.setup(self.leftmotor[1], IO.OUT)
        IO.setup(self.rightmotor[0], IO.OUT)
        IO.setup(self.rightmotor[1], IO.OUT)
        logging.info("GPIOInit")

    def forward(self):
        IO.output(self.leftmotor[0], False)
        IO.output(self.leftmotor[1], True)
        IO.output(self.rightmotor[0], False)
        IO.output(self.rightmotor[1], True)
        time.sleep(0.01)
        logging.info("Forward")

    def back(self):
        IO.output(self.leftmotor[0], True)
        IO.output(self.leftmotor[1], False)
        IO.output(self.rightmotor[0], True)
        IO.output(self.rightmotor[1], False)
        time.sleep(0.01)
        logging.info("back")

    def left(self, azimath):
        start = time.time()
        while True:
            IO.output(self.leftmotor[0], True)
            IO.output(self.leftmotor[1], False)
            IO.output(self.rightmotor[0], False)
            IO.output(self.rightmotor[1], True)
            if time.time() - start >= math.fabs(azimath)/self.ratio:
                break
        time.sleep(0.01)
        logging.info("left")

    def right(self, azimath):
        start = time.time()
        while True:
            IO.output(self.leftmotor[0], False)
            IO.output(self.leftmotor[1], True)
            IO.output(self.rightmotor[0], True)
            IO.output(self.rightmotor[1], False)
            if time.time() - start >= math.fabs(azimath)/self.ratio:
                break
        time.sleep(0.01)
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
            time.sleep(0.01)
            logging.info("bomp")
            return True
        else:
            return False

    def angle(self):
        self.gapazimath = self.gps.goalazimath() - self.fazimath
        if self.gapazimath > 0:
            self.left(math.fads(self.gps.goalazimath()-self.gapazimath))
        elif self.gapazimath < 0:
            self.right(math.fads(self.gps.goalazimath()-self.gapazimath))
        elif self.gapazimath == 0:
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
                time.sleep(0.01)
                self.angle()
                time.sleep(0.01)
                self.forward(self.gps.goaldistance())
                time.sleep(0.01)
            self.gps.goal.pop(0)
