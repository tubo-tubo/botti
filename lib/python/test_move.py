#coding:utf-8

import unittest
import gpsnavi
import go_GPIO
import math

class test_move(unittest.TestCase):
	gps = gpsnavi.gpsparser(goal=goal)

	def testNorth(self):
		goal = [141.24411667,43.126030655]
		gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
		gps.goalcalc()
		#nowpos = [141.24411667,43.126021667]
		self.assertEqual(gps.goaldistance(), 1)

	def testEast(self):
		goal = [141.244125653,43.126021667]
		gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
		gps.goalcalc()
		#nowpos = [141.24411667,43.126021667]
		self.assertEqual(gps.goaldistance(), 1)

	def testwest(self):
		goal = [141.244107687,43.126021667]
		gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
		gps.goalcalc()
		#nowpos = [141.24411667,43.126021667]
		self.assertEqual(gps.goaldistance(), 1)

	def testSouth(self):
		goal = [141.24411667,43.126012679]
		gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
		gps.goalcalc()
		#nowpos = [141.24411667,43.126021667]
		self.assertEqual(gps.goaldistance(), 1)

	def testTurn(self):
		goal = [141.24411667,43.126030655]
		gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
		gps.goalcalc()
		gps.goalazimath()
		azimath = gopsgoalazimath()
		goal = [141.235132742,43.126021667]
		gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
		gps.goalcalc()
		self.assertEqual(math.fabs(azimath - gps.goalazimath(), 0.05732173)

if __name__ == " __main__ " :
	unittest.main()