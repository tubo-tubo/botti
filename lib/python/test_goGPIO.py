#!coding:utf-8
import unittest
import go_GPIO
import gpsnavi
import time
import gpsnavi


class testgo_GPIO(unittest.TestCase):
    def setUp(self):
        leftmotor = [17, 18]
        rightmotor = [19, 20]
        goal = []
        goal.append([141.24322166666667, 43.123041666666666])
        goal.append([139.649867, 35.705385])
        self.go = go_GPIO.GPIO(leftmotor=leftmotor, rightmotor=rightmotor, goalpos=goal,ratio=20,rate=20)
        self.gps = gpsnavi.gpsparser(goal=goal)

    def test_forward(self):
        print("test_forward start")
        start = time.time()
        self.go.forward(3)
        print(int(time.time()-start)//1, 3//self.go.rate)
        start = time.time()
        self.go.forward(2.0)
        print(int(time.time()-start)//1, 2//self.go.rate)
        start = time.time()
        self.go.forward(-1)
        print(int(time.time()-start)//1, 1//self.go.rate)
        print("test_forward end")

    def test_back(self):
        print("test_back start")
        start = time.time()
        self.go.back(3)
        print(int(time.time()-start)//1, 3//self.go.rate)
        start = time.time()
        self.go.back(2.0)
        print(int(time.time()-start)//1, 2//self.go.rate)
        start = time.time()
        self.go.back(-1)
        print(int(time.time()-start)//1, 1//self.go.rate)
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

    def test_bump(self):
        print("test_bump start")
        self.gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
        self.gps.goalcalc()
        self.distance = self.gps.goaldistance()
        self.gps.gpsupdate(debuggpsvalue='$GPGGA,102139.552,4308.0643,N,14114.9876,E,0,00,0.0,77.9,M,0.0,M,,0000*51')
        self.gps.goalcalc()
        self.goaldistance = self.gps.goaldistance()
        #self.assertEqual(distance,goaldistance)
        #self.assertEqual(go_GPIO.GPIO_bump(distance,goaldistance),True)
        self.assertNotEqual(self.distance,self.goaldistance)
        self.assertEqual(self.go._bump(self.distance,self.goaldistance),False)
        print("test_bump end")

    def test_first(self):
        print("test_first start")
        self.gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
        self.gps.goalcalc()
        distance = self.gps.goaldistance()
        self.gps.gpsupdate(debuggpsvalue='$GPGGA,102139.552,4308.0643,N,14114.9876,E,0,00,0.0,77.9,M,0.0,M,,0000*51')
        self.gps.goalcalc()
        goaldistance = self.gps.goaldistance()
        self.assertFalse(self.go._bump(distance, goaldistance))
        print("test_first end")

    def test_turn(self):
        print("test_turn start")
        goal = []
        goal.append([141.24322166666667, 43.123041666666666])
        goal.append([139.649867, 35.705385])
        self.assertEqual(self.gps.goal.pop(0),[141.24322166666667, 43.123041666666666])
        print("test_turn end")
    
if __name__ == '__main__':
    unittest.main()
