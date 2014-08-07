#!coding:utf-8

import unittest
import flagjudge
import os


class MyException(Exception):
    pass


class flagjudgeTest(unittest.TestCase):

    def testcapture(self):
        cap = flagjudge.flagcapture()
        if cap.capture() is True:
            print(cap.judge())

    def testjudge1(self):
        cap = flagjudge.flagcapture()
        cap.imagename = os.path.dirname(__file__)+'/testimage/colorcone.jpg'
        print(cap.imagename)
        direction, count = cap.judge()
        self.assertEqual(direction, 'right')
        self.assertEqual(count, '4923')
        self.assertNotEqual(count, 4923)

    def testjudge2(self):
        cap = flagjudge.flagcapture()
        cap.imagename = os.path.dirname(__file__)+'/testimage/colorcone2.jpg'
        print(cap.imagename)
        direction, count = cap.judge()
        self.assertEqual(direction, 'center')
        self.assertEqual(count, '3328')
        self.assertNotEqual(count, 3328)


if __name__ == '__main__':
    unittest.main()
