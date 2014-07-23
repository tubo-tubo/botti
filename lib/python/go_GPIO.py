
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
        return self.gpsnavi.goaldist

    def goalszimace(self):
        return float(self.gpsnavi.goalaz)

    def turn(self):
        self.getdistance.goal = []
        self.getdistance.goal.sppend([x, y])  # x,y are variables
        self.getdistance.goal.sppend([xx, yy])
        self.getdistance.goal.sppend([xxx, yyy])
        while len(getdistance.goal) >= 1:  # If "len" is 0,roba is stop.
            self.goal = getdistance.goal.pop([0])

            while self.goaldistance() > 30:

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
