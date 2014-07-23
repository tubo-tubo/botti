import gpsnavi
import unittest
import datetime
import mox3
import go_f

class Testgpsnavi(unittest.TestCase):
    lon = 139.649867
    lat = 35.705385
    goal = [lon, lat]
    gps = gpsnavi.gpsparser(goal=goal)
    #getdis = go_f.getdistance()
    def test_readgps(self):
        self.gps.gpsupdate(debuggpsvalue='$GPGGA,085120.307,3541.1493,N,13945.3994,E,1,08,1.0,6.9,M,35.9,M,,0000*5E')
        self.assertEqual(self.gps.lat(), 3541.1493)
        self.assertEqual(self.gps.lon(), 13945.3994)
        self.assertEqual(self.gps.latitude(), 35.68582166666667)
        self.assertEqual(self.gps.longitude(), 139.75665666666666)
        self.assertEqual(self.gps.timestamp(), datetime.time(8, 51, 20))
        self.assertEqual(self.gps.sat_receivejudge(), True)
        self.assertEqual(self.gps.altitude(), 6.9)
        self.gps.goalcalc()
        self.assertEqual(self.gps.goaldistance(), 9906.151420843888)
        self.assertEqual(self.gps.goalazimath(), 102.62608474251853)
        self.assertEqual(self.gps.goalverticaldistance(), 8575.386912503964)
        self.assertEqual(self.gps.goalhorizontaldistance(), -4959.291811694802)
        #print(self.gps.goalazimath())

    def test_getdistance(self):
        pass
        #self.getdis.goal = [37.0, 139.0]
        #self.assertEqual(self.getdis.goal, [37.0, 139.0])

if __name__ == '__main__':
    unittest.main()

