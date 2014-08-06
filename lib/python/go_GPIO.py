#!coding:utf-8

import RPi.GPIO as IO
import go_f
import gpsnavi


class GPIO:  # GPIOをTurtleに

    def __init__(self, leftmotor=[15, 16], rightmotor=[17, 22], goalpos=[]):
        gof = go_f.getdistance()
        gof.goal = goalpos
        self.gps = gpsnavi.gpsparser(goal=gof.goal)
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        self.IO.setmode(self.IO.BCM)
        self.IO.setup(self.leftmotor[0], self.IO.OUT)
        self.IO.setup(self.leftmotor[1], self.IO.OUT)
        self.IO.setup(self.rightmotor[0], self.IO.OUT)
        self.IO.setup(self.rightmotor[1], self.IO.OUT)

    def forward(self): # 前進
        self.IO.output(self.leftmotor[0], False)
        self.IO.output(self.leftmotor[1], True)
        self.IO.output(self.rightmotor[0], False)
        self.IO.output(self.rightmotor[1], True)
        self.time.sleep(0.01)

    def back(self): # 後進
        self.IO.output(self.leftmotor[0], True)
        self.IO.output(self.leftmotor[1], False)
        self.IO.output(self.rightmotor[0], True)
        self.IO.output(self.rightmotor[1], False)
        self.time.sleep(0.01)

    def left(self): # 左旋回
        self.IO.output(self.leftmotor[0], True)
        self.IO.output(self.leftmotor[1], False)
        self.IO.output(self.rightmotor[0], False)
        self.IO.output(self.rightmotor[1], True)
        self.time.sleep(0.01)

    def right(self): # 右旋回
        self.IO.output(self.leftmotor[0], False)
        self.IO.output(self.leftmotor[1], True)
        self.IO.output(self.rightmotor[0], True)
        self.IO.output(self.rightmotor[1], False)

    def y_coordinates(self):
        self.gps.gpsupdate()
        self.gps.goalcalc()
        return self.gps.goalverticaldistance()

    def _bump(self, before, after):
        if before == after:
            self.back(50)
            self.left(30)
            self.time.sleep(0.01)
            return True
        else:
            return False

    def turn(self):
        while len(self.gps.goal) > 0:  # If "len" is 0,roba is stop.
            while self.gps.goaldistance > 30:
                while True:
                    self.y_coord = self.y_coordinates()
                    self.forward(50)
                    if not self._bump(self.y_coord, self.y_boordinates()):
                        break

                self.time.sleep(0.01)

                if 0 <= self.gps.goalazimath < 90 or 270 < self.gps.goalazimath <= 360 and self.y_coordinates() < self.y_coord:    #1st quadrant , 4th quadrant , south direction
                    self.right(self.gps.goalazimath)
                elif 0 <= self.gps.goalazimath < 90 or 270 < self.gps.goalazimath <= 360 and self.y_coordinates() > self.y_coord:   #1nd quadrant , 4rd quadrant , north direction
                    self.left(self.gps.goalazimath)
                elif 90 <= self.gps.goalazimath <= 270 and self.y_coordinates() < self.y_coord:     #2nd quadrant , 3rd quadrant , south direction
                    self.left(self.gps.goalazimath)
                elif 90 <= self.gps.goalazimath <= 270 and self.y_coordinates() > self.y_coord:     #2nd quadrant , 3rd quadrant , north direction
                    self.right(self.gps.goalszimath)

                self.time.sleep(0.01)
                self.forward(self.gps.goaldistance())
                self.time.sleep(0.01)
            self.gps.goal.pop(0)
