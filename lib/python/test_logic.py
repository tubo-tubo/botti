#!coding:utf-8

import unittest
#import go_GPIO
import gpsnavi
import time

class test_logic(unittest.TestCase):
	goal = [139.9873791954023,40.14224106321837]
	gps = gpsnavi.gpsparser(goal=goal)

	def setUp(self):
		leftmotor = [17, 18]
		rightmotor = [19, 20]
		#self.go = go_GPIO.GPIO(leftmotor=leftmotor, rightmotor=rightmotor, goalpos=goal,ratio=96.0,rate=0.0164)	
		self.gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
		self.gps.goalcalc()
		self.distance1 = self.gps.goaldistance()
		self.azimath1 = self.gps.goalazimath()   #=17.1205055555556
		self.gps.gpsupdate(debuggpsvalue='$GPGGA,035658.00,4307.5545,N,14114.6469,E,1,00,0.0,-1.3,M,0.0,M,,*73')
		self.gps.goalcalc()
		self.distance2 = self.gps.goaldistance()
		self.azimath2 = self.gps.goalazimath()   #=17.121125
		#self.gogpio = go_GPIO.GPIO(goalpos=self.goal, gps=self.gps, ratio=self.ratio, rate=self.rate)

	def test_turn1(self):
		gapaz1 = self.azimath2 - self.azimath1
		#self.gogpio.turn(gapaz1)
		self.assertEqual(self.gogpio.turn(gapaz1),"left")
		#self.gogpio.forward(self.distance2)
		self.assertEqual(first, [139.9873791954023,40.14224106321837])
		
	def test_turn2(self):
		gapaz2 = self.azimath1 - self.azimath2
		#self.gogpio.turn(gapaz2)
		self.assertEqual(self.gogpio.turn(gapaz2),"right")
		#self.gogpio.forward(self.distance1)
		self.assertEqual(first, [139.9873791954023,40.14224106321837])

if __name__ == '__main__':
    unittest.main()