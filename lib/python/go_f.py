#!coding:utf-8


class Line:
    def __init__(self, slp, x0, y0):
        self.slp = float(slp)
        self.x0 = float(x0)
        self.y0 = float(y0)


import RPI.GPIO
import math


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

    def revice(self):  # 軌道修正

        while True:
            self.line = Line(math.tan(math.atan((self.goaly-self.ycor())/(self.goalx-self.xcor()))), self.xcor(), self.ycor())  # 現在地取得
            # self.goal = (100,100)                                                                                               #ゴール位置指定

            first_x = 100/5-self.line.x0/5
            self.forward(self.first_x)

            if math.pow(100-first_x, 2) < math.pow(100-self.xcor(), 2):  # 大会で目標値の座標を「100」に代入
                self.forward(first_x)
            elif math.pow(100-self.xcor(), 2) < 20:  # 目標地へ旋回
                if self.line.y0 - 100 < 0 and self.line.x0 - 100 > 0:  # 第4象限
                    self.left(90)
                    break

                elif self.line.y0 - 100 < 0 and self.line.x0 - 100 < 0:  # 第3象限
                    self.right(90)
                    break

                elif self.line.y0 - 100 > 0 and self.line.x0 - 100 < 0:  # 第2象限
                    self.left(90)
                    break

                elif self.line.y0 - 100 > 0 and self.line.x0 - 100 > 0:  # 第1象限
                    self.right(90)
                    break
            elif math.pow(100-first_x, 2) > math.pow(100-self.xcor(), 2):
                self.left(100)
            self.time.sleep(0.1)

    def go(self):
        self.line = Line(math.tan(math.atan((self.goaly-self.ycor())/(self.goalx-self.xcor()))), self.xcor(), self.ycor())  # 現在地取得
        # while math.pow(100-self.ycor(),2) > 10:
        self.time.sleep(0.1)
        while math.pow(100-self.ycor(), 2) > 10:  # houkou
            if self.line.y0 - 100 < 0:
                self.forward(self.ycor() - 100)
            elif self.line.y0 - 100 > 0:  # houkou
                self.forward(100 - self.ycor())
        self.time.sleep(0.1)
