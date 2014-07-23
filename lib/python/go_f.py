#!coding:utf-8

import serial
import math
import pynmea2
from pyproj import Geod
import gpsnavi


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
   
    @checkpoint.setter
    def checkpoint1(self, value):
        self._checkpoint1 = value

     @property
    def checkpoint2(self):
        return self._nowpos
   
    @checkpoint.setter
    def checkpoint2(self, value):
        self._checkpoint2 = value
  


class GPIO(RPI.GPIO):  # GPIOをTurtleに

    def __init__(self, leftmotor=[17, 18], rightmotor=[22, 27]):
        super().__init__()
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        self.setmode(GPIO.BCM)
        self.setup(self.leftmotor[0], GPIO.OUT)
        self.setup(self.leftmotor[1], GPIO.OUT)
        self.setup(self.rightmotor[0], GPIO.OUT)
        self.setup(self.rightmotor[1], GPIO.OUT)      
        gg = gpsnavi.gpsparser
        gc1 = gpsnavi.gpsparser_c1
        gc2 = gpsnavi.gpsparser_c2

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
            
            if gc1.goalazimace > 10 and gc1.goalazimace < 350 and gc1.goaldistance > 30:
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
            
            if gc2.goalazimace > 10 and gc2.goalazimace < 350 and gc2.goaldistance > 30:
                break



    def go_goal(self):       
        while True:

            if 0 < self.gg.goalazimace <= 90:
                self.right(30)
            
            elif 90 < self.gg.goalazimace <= 180:
                 self.right(150)
            
            elif 180 < self.gg.goalazimace <= 270:
                self.left(150)
            
            else:
                self.left(30)

            self.time.sleep(0.01)

            self.forward(50)

            self.time.sleep(0.01)
            
            if gg.goalazimace > 10 and gg.goalazimace < 350 and gg.goaldistance > 30:
                break



