#coding:utf-8

import unittest
import gpsnavi
import go_GPIO


class Testmain(unittest.TestCase):
	def setUp(self):
		leftmotor = [17, 18]
		rightmotor = [19, 20]
		goal = []
		goal.append([141.24322166666667, 43.123041666666666])
		goal.append([139.649867, 35.705385])
		ratio = 3
		rate = 0.1
		#self.go = go_GPIO.GPIO(leftmotor=leftmotor, rightmotor=rightmotor, goalpos=goal,ratio=ratio,rate=rate)
		self.gps = gpsnavi.gpsparser(goal=goal)
		self.gogpio = go_GPIO.GPIO(goalpos=goal, ratio=ratio, rate=rate)
	
	def test_landing(self):
		#count = 0
		#self.gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
		#self.gps.goalcalc()
		#groundalt = self.gps.altitude()
		#self.assertTrue(self.gps.altitude() >= groundalt + 50)
		#count += 1
		#self.assertEqual(count,1)

		count = 0
		self.gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
		self.gps.goalcalc()
		groundalt = self.gps.altitude()
		self.assertTrue(groundalt - 10 <= self.gps.altitude() <= groundalt + 10)
		count += 1
		self.assertEqual(count,1)

	def test_travel(self):
		goal = [141.24322166666667, 43.123041666666666]
		self.gps.gpsupdate(debuggpsvalue='$GPGGA,102139.552,4308.0643,N,14114.9876,E,0,00,0.0,77.9,M,0.0,M,,0000*51')
		self.gps.goalcalc()
		gpsport = None
		gps = gpsnavi.gpsparser(portname=gpsport, goal=goal)
		self.assertEqual(self.gogpio.turn() , go_GPIO.GPIO.turn())
	
	def test_run(self):
		goal = []
		goal.append([141.24322166666667, 43.123041666666666])
		goal.append([139.649867, 35.705385])
		self.assertEqual(goal, [[141.24322166666667, 43.123041666666666],[139.649867, 35.705385]])
		self.gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
		self.gps.goalcalc()
		groundalt = self.gps.altitude()
		goalazimath = self.gps.goalazimath()
		fazimath = self.gps.goalazimath()
		gapazimath = self.gps.goalazimath() - fazimath
		goaldistance = self.gps.goaldistance()
		self.assertEqual(groundalt , self.gps.altitude())
		self.assertEqual(goalazimath , self.gps.goalazimath())
		self.assertEqual(fazimath , self.gps.goalazimath())
		self.assertEqual(gapazimath , self.gps.goalazimath()-fazimath)
		self.assertEqual(goaldistance , self.gps.goaldistance())

if __name__ == '__main__':
    unittest.main()