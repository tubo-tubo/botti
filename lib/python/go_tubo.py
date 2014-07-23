#!coding:utf-8


class Line:
    def __init__ (self, slp, x0, y0):
        self.slp = float(slp)
        self.x0 = float(x0)
        self.y0 = float(y0)

import RPI.GPIO
import time
import math


class GPIO(RPI.GPIO):  # GPIOをTurtleに
    def __init__(self):
        super(). __init__()
        self.setmode(GPIO.BCM)
        self.setup(4, GPIO.OUT)
        self.setup(17, GPIO.OUT)
        self.setup(21, GPIO.OUT)
        self.setup(22, GPIO.OUT)

    def forward(self):  # 前進
        self.output(4, False)
        self.output(17, True)
        self.output(21, False)
        self.output(22, True)
        self.time.sleep(0.1)

    def left(self):  # 左旋回
        self.output(4, False)
        self.output(17, False)
        self.output(21, False)
        self.output(22, True)
        self.time.sleep(0.1)

    def revice(self):  # 軌道修正
        while True:
            self.line = Line(math.tan(math.atan((self.goaly-self.ycor())/(self.goalx-self.xcor()))), self.xcor(), self.ycor())  # 現在地取得
            self.goal = (100, 100)  # ゴール位置指定
            first_x = self.gps.x1/10-self.Line.x0/10
            self.forward(first_x)
            if math.pow(100-first_x, 2) < math.pow(100-self.xcor(), 2):  # 大会で目標値の座標を「100」に代入
                self.time.sleep(3)
            elif math.pow(100-self.xcor(), 2) < 20 and math.pow(100-self.ycor(), 2) < 20:
                break
            else:
                self.left(30)
            self.time.sleep(0.1)
