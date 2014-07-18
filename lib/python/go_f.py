#!coding:utf-8

import time
import RPI.GPIO
import math
import pynmea2
from pyproj import Geod

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

    def Alysis(self, data):          #GPS値取得
        return pynmea2.parse(data)


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

    
    def turn(self):
        g = Geod(ellps='WGS84')
        self.goalaz, self.goalbackaz, self.goaldist = g.inv(self.goal[0], self.goal[1], nowpos[0], nowpos[1])    #彼我の方位を求めた


        while goalaz > 10 and goalaz < 350 and goaldist > 30:
            
            if 0 < goalaz <= 90:
                self.right(30)
            
            elif 90 < goalaz <= 180:
                 self.right(150)
            
            elif 180 < goalaz <= 270:
                self.left(150)
            
            else:
                self.left(30)

            self.time.sleep(0.01)

            self.forward(50)

            self.time.sleep(0.01)
            




