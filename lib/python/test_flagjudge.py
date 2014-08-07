#!coding:utf-8

import unittest
import flagjudge
import os


class MyException(Exception):
    pass


class flagjudgeTest(unittest.TestCase):
    def setUp(self):
        self.cap = flagjudge.flagcapture()

    def testcapture(self):
        if self.cap.capture() is True:
            self.imagename = self.cap.imagename
            print(self.cap.judge())

    def testjudge(self):
        self.cap.imagename = os.path.dirname(__file__)+'/colorcone2.jpg'
        print(self.cap.imagename)
        print(self.cap.judge())


if __name__ == '__main__':
    unittest.main()
