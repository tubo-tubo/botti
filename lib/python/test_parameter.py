#coding:utf-8

import unittest
import math
import gpsnavi

class testParameter(unittest.TestCase):
	lon = 141.24322166666667
	lat = 43.123041666666666
	goal = [[lon, lat]]
	gps = gpsnavi.gpsparser(goal=goal)
 	goalverticaldistance = gos.goalverticaldistance()
 	fazimath = gps.goalazimath()
 	gapazimath = gps.goalazimath() - fazimath
 	turn_azimath = math.fads(gps.goalazimath() - gapazimath)

 	def test_y_coordinates(self):
 		self.assertEqual(goalverticaldistance, 300.2753247263464)

 	def test_turn_azimath(self):
 		self.assertEqual(fazimath, -167.59266836658236)
 		self.assertEqual(gapazimath, 0)
 		self.assertEqual(turn_azimath, 167.59266836658236)

 if __name__ == '__main__':
    unittest.main()
