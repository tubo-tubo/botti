#coding:utf-8
import unittest
import go_GPIO
import time


class testgo_GPIO(unittest.TestCase):
    def setUp(self):
        leftmotor = [17, 18]
        rightmotor = [19, 20]
        goal = []
        goal.append([141.24322166666667, 43.123041666666666])
        goal.append([139.649867, 35.705385])
        self.go = go_GPIO.GPIO(leftmotor=leftmotor, rightmotor=rightmotor, goalpos=goal)

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
        start = time.time()
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


if __name__ == '__main__':
    unittest.main()
