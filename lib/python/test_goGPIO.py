#!coding:utf-8
import unittest
import go_GPIO
import gpsnavi
import time


class testgo_GPIO(unittest.TestCase):
    def setUp(self):
        leftmotor = [17, 18]
        rightmotor = [19, 20]
        goal = []
        goal.append([141.24322166666667, 43.123041666666666])
        goal.append([139.649867, 35.705385])
        gps = gpsnavi.gpsparser(goal=goal, debugmode=True)
        gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
        gps.goalcalc()
        self.go = go_GPIO.GPIO(leftmotor=leftmotor, rightmotor=rightmotor, gps=gps,  goalpos=goal)

    def test_forward(self):
        print("test_forward start")
        self.go.forward()
        print("test_forward end")

    def test_back(self):
        print("test_back start")
        self.go.back()
        print("test_back end")

    def test_left(self):
        print("test_left start")
        start = time.time()
        self.go.left(3)
        print(int(time.time()-start)//1, 3//self.go.ratio)
        start = time.time()
        self.go.left(2.0)
        print(int(time.time()-start)//1, 2//self.go.ratio)
        start = time.time()
        self.go.left(-1)
        print(int(time.time()-start)//1, 1//self.go.ratio)
        print("test_left end")

    def test_right(self):
        print("test_right start")
        start = time.time()
        self.go.right(3)
        print(int(time.time()-start)//1, 3//self.go.ratio)
        start = time.time()
        self.go.right(2.0)
        print(int(time.time()-start)//1, 2//self.go.ratio)
        start = time.time()
        self.go.right(-1)
        print(int(time.time()-start)//1, 1//self.go.ratio)
        print("test_right end")


if __name__ == '__main__':
    unittest.main()
