#!coding:utf-8

import serial
import math
import pynmea2
from pyproj import Geod
import gpsnavi


class getdistance():
    def __init__(self):
    
    @property
    def goal(self):
        return self._goal
   
    @goal.setter
    def goal(self, value):
        self._goal = value

    @property
    def nowpos(self):
        return self._nowpos
   
    @nowpos.setter
    def nowpos(self, value):
        self._nowpos = value

     @property
    def checkpoint(self):
        return self._nowpos
   
    @checkpoint.setter
    def checkpoint(self, value):
        self._checkpoint = value
  


class GPIO(RPI.GPIO):  # GPIOをTurtleに

    def __init__(self, leftmotor=[15, 16], rightmotor=[17, 22]):
        super().__init__()
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        self.setmode(GPIO.BCM)
        self.setup(self.leftmotor[0], GPIO.OUT)
        self.setup(self.leftmotor[1], GPIO.OUT)
        self.setup(self.rightmotor[0], GPIO.OUT)
        self.setup(self.rightmotor[1], GPIO.OUT)

    def forward(self):  # 前進
        self.output(self.leftmotor[0], False)
        self.output(self.leftmotor[1], True)
        self.output(self.rightmotor[0], False)
        self.output(self.rightmotor[1], True)

        self.time.sleep(0.1)

    def back(self):  # 後進
        self.output(self.leftmotor[0], True)
        self.output(self.leftmotor[1], False)
        self.output(self.rightmotor[0], True)
        self.output(self.rightmotor[1], False)

        self.time.sleep(0.1)

    def left(self):  # 左旋回
        self.output(self.leftmotor[0], True)
        self.output(self.leftmotor[1], False)
        self.output(self.rightmotor[0], False)
        self.output(self.rightmotor[1], True)

        self.time.sleep(0.1)

    def right(self):  # 右旋回
        self.output(self.leftmotor[0], False)
        self.output(self.leftmotor[1], True)
        self.output(self.rightmotor[0], True)
        self.output(self.rightmotor[1], False)

    def goaldistance(self):
        return self.gpsnavi.gpsparser.goaldist

    def goalszimace(self):
        return float(self.gpsnavi.gpsparser.goalaz)



    def turn(self):       
         while True:

            if 0 < self.goalazimace <= 90:
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
            
            if goalazimace > 10 and goalazimace < 350 and goaldistance > 30:
                break



