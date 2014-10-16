import go_GPIO
import time
import gpsnavi
import logging
import datetime
import flagjudge
import main

class testmain(unittest.Testcase):
	lon = 139.9873791954023
	lat = 40.14224106321837
	goal = [[lon,lat]]
	main = main.Main(goal=goal)

	def test_landing(self):
		self.assertEqual(count,0)
		self.assertEqual(self.main.maxalt,80)
		self.assertEqual(self.main.goal,goal)
		self.assertEqual(self.main.gpsport,None)
		self.assertEqual(self.main.gpsbaudrate,9600)
		self.assertEqual(self.main.groundalt,0)
		self.assertEqual(self.main.ratio,96.0)
		self.assertEqual(self.main.rate,0.0164)
		self.assertEqual(self.main.gps,goal)

	def test_