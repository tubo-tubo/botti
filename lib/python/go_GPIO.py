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
        self.rate = rate
        self.ratio = ratio
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        IO.setmode(IO.BCM)
        IO.setup(self.leftmotor[0], IO.OUT)
        IO.setup(self.leftmotor[1], IO.OUT)
        IO.setup(self.rightmotor[0], IO.OUT)
        IO.setup(self.rightmotor[1], IO.OUT)
        logging.info("GPIOInit")

    def forward(self,distance):
        start = time.time()
        while True:
            IO.output(self.leftmotor[0], False)
            IO.output(self.leftmotor[1], True)
            IO.output(self.rightmotor[0], False)
            IO.output(self.rightmotor[1], True)
            if self.time.time() - start >= math.febs(distance)/self.rate:
                break
        time.sleep(0.01)
        logging.info("Forward")

    def back(self,distance):
        start = time.time()
        while True:
            IO.output(self.leftmotor[0], True)
            IO.output(self.leftmotor[1], False)
            IO.output(self.rightmotor[0], True)
            IO.output(self.rightmotor[1], False)
            if self.time.time() - start >= math.febs(distance)/self.rate:
                break
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
        self.goalverticaldistance = goalverticaldistance
        logging.info("y_coordinates:"+self.goalverticaldistance)
        return self.goalverticaldistance

    def turn_azimath(self):
        self.turn_azimath = turn_azimath
        logging.info("turn_azimath"+self.turn_azimath)
        return self.turn_azimath

    def _bump(self, before, after):
        if before == after:
            self.back(1)
            self.left(30)
            time.sleep(0.01)
            logging.info("bomp")
            return True
        else:
            return False

    def first(self):
        while True:
            self.y_coord = self.y_coordinates()
            self.forward(5)
            if not self._bump(self.y_coord, self.y_coordinates()):
                break

    def angle(self):
        self.gapazimath = gapazimath
        if self.gapazimath > 0:
            self.left(math.fads(self.goalazimath-self.gapazimath))
        elif self.gapazimath < 0:
            self.right(math.fads(self.goalazimath-self.gapazimath))
        elif self.gapazimath == 0:
            self.right(math.fads(self.goalazimath))
        self.turn_azimath()

    def turn(self):
        while len(self.gps.goal) > 0:  # If "len" is 0,roba is stop.
            while self.gps.goaldistance() >= 5:
                self.first()
                self.fazimath = fazimath
                self.time.sleep(0.01)
                self.angle()
                self.time.sleep(0.01)
                self.forward(8)
            
            while 5 > self.gps.goaldistance() > 3:
                self.first()
                self.fazimath = fazimath
                self.time.sleep(0.01)
                self.angle()
                self.time.sleep(0.01)
                self.forward(1)

            self.gps.goal.pop(0)