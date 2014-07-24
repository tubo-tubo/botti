
class GPIO:  # GPIOをTurtleに
    import RPi.GPIO as IO
    import go_f
    import math
    
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

    def goalszimath(self):
        return float(self.gpsnavi.goalaz)

    def x_coordinates(self):
        return self.gpsnavi.goalhorizontaldistance

    def y_coordinates(self):
        return self.gpsnavi.goalverticaldistance

    def turn(self):
        self.getdistance.goal = []
        self.getdistance.goal.sppend([x, y])  # x,y are variables
        self.getdistance.goal.sppend([xx, yy])
        self.getdistance.goal.sppend([xxx, yyy])
        self.x_coord = []
        self.y_coord = []

        while len(self.getdistance.goal) >= 1:  # If "len" is 0,roba is stop.
            self.goal = self.getdistance.goal.pop([0])
            
            while self.goal > 30:
                self.go_f.nowpos.pop([0])                 
                self.go_f.nowpos.append([self.goalazimath])
                self.x_coord.pop([0])
                self.x_coord.append([self.x_coordinates])                        
                self.y_coord.pop([0])
                self.y_coord.append([self.y_coordinates])                                     
                self.forward(50)
                self.time.sleep(0.01)
                self.atan = self.math.atan("("[self.y_coordinates - self.y_coord]")" / "("[self.x_coordinates - self.x_coord]")")

                if 0 < self.goalszimath < 90 or 270 < self.goalszimath < 360  and "("[self.x_coordinates - self.x_coord]")" < 0: 
                    self.right(180 - self.atan)    
                elif 0 < self.goalszimath < 90 or 270 < self.goalszimath < 360 and "("[self.x_coordinates - self.x_coord]")" > 0:
                    self.left(180 - self.atan)    
                elif 90 < self.goalszimath < 270 and "("[self.x_coordinates - self.x_coord]")" < 0: #
                    self.left(180 - self.atan)                    
                elif 90 < self.goalszimath < 270 and "("[self.x_coordinates - self.x_coord]")" > 0: #
                    self.right(180 - self.atan) 
                else :
                    self.right(180 - self.atan)                    

                self.forward(self.getdistance.goal)
                self.time.sleep(0.01)
