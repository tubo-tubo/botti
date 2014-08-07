#!coding:utf-8

import unittest
import flagjudge
import os


class flagjudgeTest(unittest.TestCase):
    def setUp(self):
        self.cap = flagjudge.flagcapture()

    def testcapture(self):
        with self.assertRaises(ValueError):
            self.cap.capture()
            self.imagename = self.cap.imagename
            print(self.cap.judge())

    #def testjudge(self):
    #    self.cap.imagename = os.path.dirname(__file__)+'/colorcone2.jpg'
    #    print(self.cap.imagename)
    #    print(self.cap.judge())


if __name__ == '__main__':
    unittest.main()
